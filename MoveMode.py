from random import randint
from FinalScore import FinalScore
from Encounter import *
def Move(player, mList): #1: CampEncounter, 2: NoramlEnemy, 3: MiddleBoss, 4: FinalBoss 0: End
    for i in mList:
        print("-" * 50)
        print("층수: ", player.floor,"층")
        match i:
            case 1:
                CampEncounter(player)
            case 2:
                EnemyEncounter(1, player, 1)
            case 3:
                EnemyEncounter(1, player, 2)
            case 4:
                EnemyEncounter(1, player, 3)
            case 0:
                print("Boss를 물리쳤습니다.")
                print("축하합니다!")
                return 0
        print("-" * 50)

def TestMode(player): #modenum = 1 #잡캠중캠최
    #NoramlEnemy -> NormalEnemy -> CampEncounter -> MiddleBoss -> CampEncounter -> FinalBoss -> END
    mlist = [2, 2, 1, 3, 1, 4, 0]
    Move(player, mlist)
    return FinalScore(player)

def NormalMode(player): #modenum = 2 #노말적인지 캠프인지 랜덤 사용
    
    print("아직 제작중입니다. 다른 모드를 골라주세요.")
    return 0
    print("Boss를 물리쳤습니다.")
    print("축하합니다!")
    return FinalScore(player)

def InfinityMode(player): #modenum = 3 #랜덤 사용 #hp가 0이 될때까지 반복
    print("아직 제작중입니다. 다른 모드를 골라주세요.")
    return 0
    while player.hp != 0:
        match randint(1, 100):
            case 1:
                NormalEnemy()
        floor += 1
        
    print("Game End")
    return FinalScore(player)