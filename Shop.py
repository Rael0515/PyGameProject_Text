from Item import *
from GetValue import *

def Shop(player):
    print("상인: 여기는 상점이란다. 무엇을 사러 왔니?")
    num = 0
    
    while num != 3:
        print("1. 회복아이템, 2. 공격아이템 3. 끝내기")
        num = GetNumber(1, 3)
        loop = 1
        if num ==1:
            while loop:
                ShowHealItemList()
                print("소지금: ", player.money)
                shop_item = GetNumber(0, len(getHealItemList()))
                if shop_item != 0:
                    loop = BuyHealItem(player, shop_item)
                else:
                    print("상인: 그래? 안살거니?")
                    loop = 0
            
        elif num == 2:
            while loop:
                ShowAttackItemList()
                print("소지금: ", player.money)
                shop_item = GetNumber(0, len(getAttackItemList()))
                if shop_item != 0:
                    loop = BuyAttackItem(player, shop_item)
                else:
                    print("상인: 그래? 안살거니?")
                    loop = 0

        else:
            print("상인: 또 오렴!")


def EXShop(player):
    print("상인: 안녕~ 여긴 특수상점이란다!")
    print("상인: 뭘 사러 왔니?")
    while True:
        print("1. 파워 업 아이템 | 2. 전투용 아이템 | 3. 이동 아이템 | 4. 향로 아이템")
        num  = GetNumber(1, 4)
        if num == 1:
            getTurnItemList()
        elif num == 2:
            getBattleItemList()
        elif num == 3:
            getMoveItemList()
        elif num == 4:

        else:


    

def WeaponShop(player):
    print("상인: 안녕~ 여긴 무기상점이란다!")
    print("상인: 뭘 사러 왔니?")