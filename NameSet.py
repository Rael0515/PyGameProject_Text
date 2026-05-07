from CharacterInfo import Character

def MakeName(end):
    while end == 0:
        print("이름을 정해주세요")
        name = input(">>")
        print("당신의 이름은 ", name, "가(이) 맞습니까?")

        while True:
            print("(맞다: y or 다시 고르기: n)")
            check = input(">>")

            if check == 'y' or check == 'Y':
                end = 1
                break
            elif check == 'n' or check == 'N':
                end = 0
                break
            else:
                print("y혹은 n으로 대답해주세요\n")
    player = Character(name)
    return player, name