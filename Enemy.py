class Enemy:
    def __init__(self, name, hp, atk, defense, money, exp):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.atk = atk
        self.defen = defense
        self.money = money
        self.exp = exp

##상태 출력
    def PrintHP(self): #no return
        print(self.name,"의 남은 체력:",self.hp)

##행동
    def DoAttack(self): #return self.atk
        print(self.name,"의 공격!")
        return self.atk
    
    def DoNothing(self):
        print(self.name,"은(는) 아무것도 안한다!")

    def GetAttacked(self, dam): #return 0, 0 || return self.Killed() (when killed)
        total = dam - self.defen
        if total <= 0:
            print(self.name,"은(는) 공격을 튕겨냈다!")
            return 0, 0
        self.hp -= total
        if self.hp <= 0:
            return 0, 0
        print(self.name,"은(는)", total, "만큼의 데미지를 입었다!")
        self.PrintHP()
        return 0, 0
        
##처치
    def Killed(self): #return money, exp
        print(self.name,"은(는) 쓰러졌다!")
        return self.money, self.exp

##자식클래스
#기본 몬스터
class NormalEnemy(Enemy): #일반몬스터
    def __init__(self):
        super().__init__("일반몬스터", 100, 10, 10, 100, 300) #name, (max, now)hp, atk, defense, money, exp
class MiddleBoss(Enemy): #중간보스
    def __init__(self):
        super().__init__("중간보스", 500, 80, 35, 500, 1000) #name, (max, now)hp, atk, defense, money, exp
class FinalBoss(Enemy): #최종보스
    def __init__(self):
        super().__init__("최종보스", 800, 190, 140, 3000, 3000) #name, (max, now)hp, atk, defense, money, exp
#특수 몬스터
class EXPEnemy(Enemy): #경험치 배수 몬스터
    def __init__(self):
        super().__init___("경험치 기부천사", )