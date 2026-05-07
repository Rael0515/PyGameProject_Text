from NameSet import MakeName

def Intro():
    print("**턴제 텍스트 게임**")
    player, name = MakeName(0)
    print("안녕!", name,"!")
    print("우리 세계에 잘 왔어!")
    print("지금 이 세상은 마왕에게 점령당해 있어서 너의 도움이 필요해!")
    print("우선 기본검(데미지 20)를 줄게! 이제 너의 모험의 시작이야!")
    print("System:", name,"은(는) 기본검을 손에 넣었다!")
    return player