import os
import subprocess

def clear_screen():

    command = 'cls' if os.name == 'nt' else 'clear' #os.name을 이용해서 os name을 획득 (Win: nt)
    subprocess.run(command, shell=True) # shell=True는 Win의 cls 명령어 사용을 위해 필요함