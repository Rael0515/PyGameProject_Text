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
        #------------------턴 관련 스텟 or 상태
        self.turnatk = [] #[[name, num, turn]]
        self.turndef = [] #[[name, num, turn]]

        self.condition = [] #[[condition name, dam, turn]]

        #------------------무기, 아이템 기타 등
        self.floor = 1
        self.money = 1000
        self.weaponName = "청동검"
        self.weaponDam = 20
        self.attackItem = [] #[[name, description, count, power]]
        self.healItem = [] #[[name, description, count, power]]
        self.turnItem = [] #[[name, count, power, turnatk or turndef, turn]]

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
        input("System: 다음으로 진행하고자 하면 Enter를 누르시오.")
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
            totalcount = num
            is_get = 1

        if is_get == 1:
            print(item_name,"을(를)", num,"개 획득했다!")
            print("현재", item_name, "은(는)", totalcount, "개 입니다.")

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
            totalcount = num
            is_get = 1

        if is_get == 1:
            print(item_name,"을(를)", num,"개 획득했다!")
            print("현재", item_name,"은(는)", totalcount,"개 입니다.")

    def GetTurnItem(self, item_name, num, power, aord, turn): #no return ##수정요함!
        is_get = 0
        totalcount = 0
        for item in self.turnItem: #존재시 #[[name, count, power, turnatk or turndef, turn]]
            if item[0] == item_name:
                item[1]+=num
                totalcount = item[1]
                is_get = 1
                break

        if is_get == 0: #부존재
            self.healItem.append([item_name, num, power, aord, turn])
            totalcount = num
            is_get = 1

        if is_get == 1:
            print(item_name,"을(를)", num,"개 획득했다!")
            print("현재", item_name, "은(는)", totalcount, "개 입니다.")

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
    
    def UseTurnItem(self, item_name): #return 0 || return -1 (noItem)
        for item in self.healItem: #[[name, count, power, turnatk or turndef, turn]]
            if item[0] == item_name: #존재
                item[1] -= 1
                if item[3] == "turnatk":#turnatk = [[name, num, turn]]
                    self.turnatk.append([item[0], item[2], item[4]])
                    aord = 1
                else:#turndef = [[name, num, turn]]
                    self.turndef.append([item[0], item[2], item[4]])
                    aord = 0
                
                print(self.name,"은(는)",item[0],"을(를) 사용했다!")
                print(self.name,"은(는) 일시적으로",aord, "이(가)",item[2],"만큼 올랐다!")

                if item[1] <= 0:
                    self.turnItem.remove(item)
                    print("마지막", item[0],"을(를) 사용했다!")
                    return 0
                print("현재", item[0],"은(는)", item[1],"개 남았다.")
                return 0
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
    
    def TotalATK(self): #return atk, is_end #turnatk = [[name, num, turn]]
        totalatk = self.atk + self.weaponDam
        is_end = "no"
        for item in self.turnatk:
            totalatk+= item[1]
            item[2] -= 1
            if item[2] <= 0:
                is_end = item[0]
                self.turnatk.remove(item)
        return totalatk , is_end
    
    def TotalDEF(self): #return def, is_end #turndef = [[name, num, turn]]
        totaldef = self.defen
        is_end = "no"
        for item in self.turndef:
            totaldef += item[1]
            item[2] -= 1
            if item[2] <= 0:
                is_end = item[0]
                self.turndef.remove(item)
        return totaldef , is_end
    
    def GetTotalATK(self): #return totalatk, turn
        totalatk = self.atk + self.weaponDam
        turn = 0
        for item in self.turnatk: #turnatk = [[name, num, turn]]
            totalatk+= item[1]
            turn += item[1]
        return totalatk, turn
    
    def GetTotalDEF(self): #return totaldef, turn
        totaldef = self.defen
        turn = 0
        for item in self.turndef: #turndef = [[name, num, turn]]
            totaldef += item[1]
            turn += item[1]
        return totaldef, turn
    
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
    
    def DoAttack(self): #return atk, is_end
        return self.TotalATK()
    
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
    
    def ShowTurnItem(self): #return -1(err) || return 0(normal)
        if not self.turnItem:
            print("파워 업 아이템이 없습니다.")
            return -1
        else:
            index = 1
            print("-"*50, end="")
            for item in self.attackItem: #[[name, count, power, turnatk or turndef, turn]]
                print("")
                print(index, ". ", item[0])
                if item[3] == "turnatk":
                    print("용도: 공격수치용")
                else:
                    print("용도: 방어수치용")
                print("파워 업 수치: ", item[2])
                print("유지 턴 수: ", item[4])
                print("아이탬 개수: ", item[1])    
                index+=1
                print("-"*30, end="")
            print("-"*20)
        return 0

    def FindHealItem(self, num): #return itemname
        return self.healItem[num - 1][0]
    def FindAttackItem(self, num): #return itemname
        return self.attackItem[num -1][0]
    def FindTurnItem(self, num): #return itemname
        return self.turnItem[num -1][0]