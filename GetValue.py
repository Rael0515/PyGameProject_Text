def GetNumber(start, end):
    while True:
        try:
            num = int(input(">> "))
        except ValueError:
            print("숫자를 입력하세요.")
        if num >=start and num <=end:
            return num
        else:
            print(start, "~", end,"사이의 정수를 입력하세요.")