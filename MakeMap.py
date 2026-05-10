from CharacterInfo import Character
from random import randint
from Encounter import *
from Shop import EXShop, WeaponShop
def MakeMap(player, mode):
    num = randint(1, 100)
        #Enemy = 2.Normal, StrongEnemy(5.EXP, 6.Money) || 1. Camp || 7.EXShop 8.WeaponShop
    if num <= 35: EnemyEncounter(1, player, 1)#NormalEnemy #1~35 (35) or firstFloor
    elif num <= 50: CampEncounter(player) #Camp #35~50 (15)
    elif num <= 65: EnemyEncounter(1, player, 5) #EXPEnemy #50~65(15)
    elif num <= 75: EXShop #EXShop #65~75(10)
    elif num <= 95: EnemyEncounter(1, player, 6) #MoneyEnemy #75~95(20)
    elif num <= 100: WeaponShop() #WeaponShop #95~100(5)
    
    return