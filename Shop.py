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