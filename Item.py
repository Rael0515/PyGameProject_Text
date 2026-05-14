from ItemList import *

def ShowAttackItemList(): #no return
    Item = getAttackItemList()
    index = 1
    for i in Item:
        print("-"*50)
        print(index, ". ", i[0])
        print("설명: ", i[1])
        print("데미지: ", i[2])
        print("가격: ", i[3])
        index+=1
    print("-"*50)
    print("0: 종료")

def ShowHealItemList(): #no return
    Item = getHealItemList()
    index = 1
    for i in Item:
        print("-"*50)
        print(index, ". ", i[0])
        print("설명: ", i[1])
        print("회복량: ", i[2])
        print("가격: ", i[3])
        index+=1
    print("-"*50)
    print("0: 종료")
    

def BuyAttackItem(player, num): #return 1 (err, again) || return 0 (stop)
    num-=1
    Item = getAttackItemList()
    if num < 0 or num > len(Item):
        print("해당 번호의 아이템은 판매하지 않는단다. 다시 확인해주렴")
        return 1
    selectItem = Item[num]
    if player.money < selectItem[3]:
        print("저런! 돈이 부족한 것 같구나!")
        return 1
    player.money -= selectItem[3] ##돈 차감
    player.GetAttackItem(selectItem[0], selectItem[1], 1, selectItem[2]) #(self, item_name, description, num, power)
    print("구매해줘서 고마워!")
    print("또 살 거 있니?")
    print("(네: 1, 아니요: 0)")
    while True:
        check = int(input(">> "))
        if check == 1:
            return 1
        elif check == 0:
            return 0
        else:
            print("System: 올바르지 않은 입력입니다. 다시 입력해 주세요.")

def BuyHealItem(player, num): #return 1 (err, again) || return 0 (stop)
    num-=1
    Item = getHealItemList()
    if num < 0 or num > len(Item):
        print("해당 번호의 아이템은 판매하지 않는단다. 다시 확인해주렴")
        return 1
    selectItem = Item[num]
    if player.money < selectItem[3]:
        print("저런! 돈이 부족한 것 같구나!")
        return 1
    player.money -= selectItem[3] ##돈 차감
    player.GetHealItem(selectItem[0], selectItem[1], 1, selectItem[2]) #(self, item_name, description, num, power)
    print("구매해줘서 고마워!")
    print("또 살 거 있니?")
    print("(네: 1, 아니요: 0)")
    while True:
        check = int(input(">> "))
        if check == 1:
            return 1
        elif check == 0:
            return 0
        else:
            print("System: 올바르지 않은 입력입니다. 다시 입력해 주세요.")