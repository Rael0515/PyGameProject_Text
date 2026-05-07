from Intro import Intro
from MoveMode import *
from ChoseMode import ChoseMode

def main():

    num = ChoseMode()

    match num:
        case 1:
            score = TestMode(Intro())
        case 2:
            score = NormalMode(Intro())
        case 3:
            score = InfinityMode(Intro())
    print("최종점수: ", score)
    
    input("\n게임을 종료하려면 엔터 키를 누르세요...")
    return 0
  

main()        