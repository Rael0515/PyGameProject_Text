from random import randint
from FinalScore import FinalScore
from Encounter import *
from GetValue import *
from MakeMap import MakeMap

def Move(player, mList): #1: CampEncounter, 2: NoramlEnemy, 3: MiddleBoss, 4: FinalBoss 0: End
    for i in mList:
        print("-" * 50)
        if i != 0:
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
    
    print("Sysyem: 10층 모드(1) 20층 모드(2) 중 선택하세요.")
    # mList = []
    end = GetNumber(1, 2)
    EnemyEncounter(1, player, 1) ##첫번째 맵은 노말몬스터 고정
    for i in int(player.floor):
        if end == i: EnemyEncounter(1, player, 3) #보스몬스터
        elif end // 2 == i: EnemyEncounter(1, player, 2) #중간보스 몬스터
        elif end - 1 == i or (end // 2) - 1 == i: CampEncounter(player) #보스전 전 캠프 입성
        else:
            MakeMap(player, mode = 2) ##노말모드는 2번 무한은 3번
        
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