def getAttackItemList(): #return (list)Item 
    #[[name, Description, damage, price],]
    Item = [["수류탄","던지기 전에는 손에서 꼭 쥐고 놓지 마렴!", 900, 900], 
            ["화염병","파이어 앤드 저스티스!", 800, 800], 
            ["방패","최고의 공격은 방어다!", 500, 500], 
            ["총","대화(물리)", 700, 700]]
    return Item

def getHealItemList(): #return (list)Item 
    #[[name, Description, healingLevel, price],]
    Item = [["빨간포션","최고급 포션이야!", 1000000, 10000], 
            ["파란포션","약간 애매한 중급 포션이야!", 500, 1000], 
            ["초록포션","저급 포션이지만 가격이 매우 싸단다!", 300, 800]]
    return Item

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