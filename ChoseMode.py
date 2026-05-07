from GetValue import *
def ChoseMode():
    while True:
        print("어떤 모드로 실행하시겠습니까?")
        print("1. 테스트모드 2. 일반모드(미구현) 3. 무한모드(미구현)")
        num = GetNumber(1,3)
        if num == 1 or num == 2 or num == 3:
            return num
        else:
            print("다시 입력하세요.")