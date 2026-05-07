from Item import *
from Enemy import *
from Shop import *
from random import randint
from Move import PlayerMove, EnemyMove

def CampRecoverEncounter(player):
    while True:
        print("1. 많이 회복: 최대 HP의 60%를 회복한다.")
        print("2. 적게 회복: 최대 HP의 10%를 회복하고, 돈을 50% 늘린다.")
        print("3. 주사위를 굴리고 굴린만큼 회복한다: (1~5: 주사위수 * 10% 회복, 6: full-hp회복)")
        print(player.name, "의 HP: ",player.hp, "/", player.maxhp, "|", player.name, "의 소지금: ", player.money)
        try:
            num = int(input(">> "))
        except ValueError:
            print("숫자를 입력 해 주세요.")
            continue
        if num < 1 or num > 3:
            print("1 부터 3까지의 수를 입력해 주세요")
        elif num == 1:
            print("최대HP: ",player.maxhp," 현재 HP: ", player.GetRecover(percent = 60))
            break
        elif num == 2:
            print("최대HP: ",player.maxhp," 현재 HP: ", player.GetRecover(percent = 10))
            print("현재 돈: ", player.GetMoney( percent = 50))
            break
        else:
            print("주사위를 굴려보자...")
            dice = randint(1, 6)
            print("주사위는 ", dice, "이(가) 나왔다!")
            if dice >=1 and dice <= 5:
                print("최대HP: ",player.maxhp," 현재 HP: ", player.GetRecover(percent = dice*10))
            else:
                print("해냈다! 6이(가) 나왔다!!!")
                print("HP를 모두 회복한다!!!")
                print("최대HP: ",player.maxhp," 현재 HP: ", player.GetRecover(percent = 100))
            break

def FightEnemy(player, enemy): #return 0
    print(player.name,"은(는) ", enemy.name,"을(를) 만났다!")
    turn = 1
    while enemy.hp >= 0:
        print("-" * 50)
        turn = PlayerMove(player, enemy, turn)
        print("-" * 50)
        if enemy.hp <= 0:
            break
        EnemyMove(player, enemy)
    money, exp = enemy.Killed()
    print("-" * 50)
    print(enemy.name, "을(를) 쓰러뜨리고 돈을 ", money,"를 얻었다!")
    player.GetMoney(money)
    player.GetEXP(exp)
    return 0
    

def EnemyEncounter(mode, player, enemynum): #Enemynum 1: normal , 2: Middle, 3: Final #return 0 (normal)|| return -1(err)|| return 1 (ending)
    print("적이 나왔다!")
    if enemynum == 1:
        enemy_instance = NormalEnemy()
    elif enemynum == 2:
        enemy_instance = MiddleBoss()
    elif enemynum == 3:
        enemy_instance = FinalBoss()
    else:
        print("System: 잘못된 접근입니다.")
        return -1
    FightEnemy(player, enemy_instance)
    
    if mode != 3 and enemynum == 3:
        return 1
    print("다음 층으로 가자!")
    player.floor += 1
    return 0

def CampEncounter(player): #return 0 (normal)
    print("캠프를 발견했다! 여기서 조금 쉬었다 가자!")
    CampRecoverEncounter(player)
    while True:
        print("상점을 방문할까? (Yes: y No: n)")
        print("소지금:", player.money)
        yorn = input(">> ")
        if yorn == 'Y' or yorn == 'y':
            Shop(player)
            print("다음 층으로 가자!")
            return 0
        elif yorn =='N' or yorn =='n':
            print("다음 층으로 나아가기로 했다!")
            return 0
        else:
            print("y 혹은 n을 입력해주세요.")


