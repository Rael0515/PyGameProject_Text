def GetNumber(start, end):
    while True:
        try:
            num_input = input(">> ").strip() ##strip() -> 공백 제거 처리

            if not num_input:
                print(start, "~", end,"사이의 정수를 입력하세요.")
                continue

            num = int(num_input)

        except ValueError:
            print("숫자를 입력하세요.")

        if num >=start and num <=end:
            return num
        
        else:
            print(start, "~", end,"사이의 정수를 입력하세요.")