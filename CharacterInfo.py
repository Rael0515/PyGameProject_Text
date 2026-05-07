from Item import getAttackItemList, getHealItemList
class Character:
    def __init__(self, name): #캐릭 생성 기본값
        self.name = name
        self.level = 1
        self.exp = 0
        self.maxhp = 100 #최대 hp
        self.hp = 100 #현재 hp
        self.atk = 10
        self.defen = 5

        self.floor = 1
        self.money = 1000
        self.weaponName = "청동검"
        self.weaponDam = 20
        self.attackItem = [] #[[name, description, count, power]]
        self.healItem = [] #[[name, description, count, power]]

##내부 동작들
    def GetEXP(self, exp): #no return
        print( self.name , "은(는)", exp, "만큼의 경험치를 얻었다!")
        self.exp += exp
        before = self.level
        beforehp = self.maxhp
        money = 0
        while (self.exp - 100) >= 0 :
            self.level += 1
            self.maxhp += 50
            self.atk += 10
            self.defen += 5
            self.exp -= 100
            money += 1000
        if before != self.level:
            print(self.name, "은",  before, " -> ", self.level, "으로 레벨업 했다!")
            print("플레이어 Level: ",self.level)
            print("MAX HP: ", beforehp," -> ",self.maxhp)
            self.GetMoney(money)
        print("플레이어 현재 경험치: ", self.exp)
        #return self.level, self.exp, self.maxhp, self.atk, self.defen
    
    def GetMoney(self, money):
        self.money += money
        print("플레이어 현재 돈: ", self.money)

    def ChangeWeapon(self, name, dam): #no return
        self.weaponName = name
        self.weaponDam = dam

    def GetHealItem(self, item_name, description, num, power): #no return ##수정요함!
        is_get = 0
        totalcount = 0
        for item in self.healItem:#[[name, description, count, power]]
            if item[0] == item_name:
                item[2]+=num
                totalcount = item[2]
                is_get = 1
                break

        if is_get == 0:
            self.healItem.append([item_name, description, num, power])
            totalcount = 1
            is_get = 1

        if is_get == 1:
            print(item_name,"을(를)", num,"개 획득했다!")
            print("현재", item_name+"은(는)", totalcount, "개 입니다.")

    def GetAttackItem(self, item_name, description, num, power): #no return
        is_get = 0
        totalcount = 0
        for item in self.attackItem:#[[name, description, count, power]]
            if item[0] == item_name:
                item[2]+=num
                totalcount = item[2]
                is_get = 1
                break

        if is_get == 0:
            self.attackItem.append([item_name, description, num, power])
            totalcount = 1
            is_get = 1

        if is_get == 1:
            print(item_name,"을(를)", num,"개 획득했다!")
            print("현재", item_name,"은(는)", totalcount,"개 입니다.")

    def UseHealItem(self, item_name): #return 0 || return -1 (noItem)
        power = 0
        for item in self.healItem:#[[name, description, count, power]]
            if item[0] == item_name:
                item[2] -= 1
                power = item[3]
                self.hp += power
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
                
                print(self.name,"은(는)",item[0],"을(를) 사용했다!")
                print(self.name,"은(는)",item[3],"만큼 회복했다!")

                if item[2] <= 0:
                    self.healItem.remove(item)
                    print("마지막", item[0],"을(를) 사용했다!")
                    return 0
                print("현재", item[0],"은(는)", item[2],"개 남았다.")
                return 0
        return -1
    def UseAttackItem(self, item_name): #return power || return -1 (noItem)
        power = 0
        for item in self.attackItem:#[[name, description, count, power]]
            if item[0] == item_name:
                item[2] -= 1
                power = item[3]
                print(self.name,"은(는)",item[0],"을(를) 사용했다!")

                if item[2] <= 0:
                    self.attackItem.remove(item)
                    print("마지막", item[0],"을(를) 사용했다!")
                    return power
                print("현재", item[0],"은(는)", item[2],"개 남았다.")
                return power
        return -1

##기초치 획득
    def GetRecover(self, recover = 0, percent = 0): #return int(self.hp)
        if recover == 0:
            recover = int(self.maxhp * percent / 100)
        self.hp += recover
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return int(self.hp)
    
    def GetMoney(self, earn = 0, percent= 0):#return int(self.money)
        if earn == 0:
            earn = int(self.money*(percent/100))
        self.money+=earn
        return int(self.money)
    
##실제 동작들

    def GetAttacked(self, dam): #return self.hp, 0 (no damage) || return self.hp, total (get damage)
        print(self.name,"은(는)", dam, "만큼의 데미지를 입었다!")
        total = dam - self.defen
        if total <= 0:
            return self.hp, 0
        self.hp -= total
        if self.hp <= 0:
            self.hp = 0
        while self.hp == 0:
            if self.ShowHealItem() == -1:
                self.Died()
            else:
                print(self.name, "은(는) 체력이 다할것 같다!")
                print("사용할 아이템을 입력해주세요.")
                while True:
                    num = int(input(">> "))
                    name = self.FindHealItem(num)
                    for item in self.healItem:
                        if item[0] == name:
                            self.UseHealItem(name)
                            break
                        else:
                            print("존재하지 않는 아이템입니다.")
                            print("다시 입력해주세요.")
          
        return self.hp, total
    
    def DoAttack(self): #return total
        total = self.atk + self.weaponDam
        return total
    
    def Died(self): #exit(0)
        from FinalScore import FinalScore
        print(self.name,"의 체력이 0이 되었습니다.")
        print("GAME OVER")
        print("최종점수: ", FinalScore(self))

        input("\n게임을 종료하려면 엔터 키를 누르세요...")
        exit(0)

##아이템 리스트 확인

    def ShowHealItem(self): #return -1(err) || return 0(normal)
        if not self.healItem:
            print("회복 아이템이 없습니다.")
            return -1
        else:
            index = 1
            print("-"*50, end="")
            for item in self.healItem: #[[name, description, count, power]]
                print("")
                print(index, ". ", item[0])
                print("설명: ", item[1])
                print("회복량: ", item[3])
                print("아이탬 개수: ", item[2])    
                index+=1
                print("-"*30, end="")
            print("-"*20)
        return 0
    
    def ShowAttackItem(self): #return -1(err) || return 0(normal)
        if not self.attackItem:
            print("공격 아이템이 없습니다.")
            return -1
        else:
            index = 1
            print("-"*50, end="")
            for item in self.attackItem: #[[name, description, count, power]]
                print("")
                print(index, ". ", item[0])
                print("설명: ", item[1])
                print("데미지: ", item[3])
                print("아이탬 개수: ", item[2])    
                index+=1
                print("-"*30, end="")
            print("-"*20)
        return 0
    def FindHealItem(self, num): #return itemname
        return self.healItem[num - 1][0]
    def FindAttackItem(self, num): #return itemname
        return self.attackItem[num -1][0]