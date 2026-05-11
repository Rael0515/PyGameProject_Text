from Enemy import *
from GetValue import *
from random import randint

def PlayerMove(player, enemy, turn):
    while True:
        print(turn,"턴|| 1. 공격 |2. 아이템사용|3. 도망(구현안함)")
        print("|| 적 HP: ", enemy.hp, "| 적 공격력: ", enemy.atk,"| 적 방어력: ", enemy.defen,"||")
        print("||"+player.name,"| HP: ", player.hp,"/",player.maxhp ,
              "| 공격력: ", player.GetTotalATK(), "(파워업: ", player.GetTotalATK() - player.atk - player.weaponDam, ")",
              "| 방어력: ", player.GetTotalDEF(), "(파워업: ", player.GetTotalDEF() - player.defen, ") ||")
        print("-"*50)
        num = GetNumber(1, 3)
        if num == 1: #1. 공격
            print(player.name, "의 공격!")
            dam, is_end = player.DoAttack()
            enemy.GetAttacked(dam)
            if is_end != "no":
                print(is_end,"의 효과가 끝났다!")
            turn += 1
            return turn
        elif num == 2: #2. 아이템사용
            while True:
                print("1. 회복아이템 | 2. 공격아이템 | 3. 파워업 아이템 | 4. 뒤로가기")
                item_num = GetNumber(1, 4)
                if item_num == 1: #회복아이템 이용
                    if player.ShowHealItem() == -1:
                        break
                    end = len(player.healItem)
                    print(end+1, ": 뒤로가기")
                    use_num = GetNumber(1, end+1)
                    if use_num == end+1:
                        break
                    else:
                        player.UseHealItem(player.FindHealItem(use_num))
                        turn+=1
                        return turn
                elif item_num == 2: #공격아이템 이용
                    if player.ShowAttackItem() == -1:
                        break
                    end = len(player.attackItem)
                    print(end+1, ": 뒤로가기")
                    use_num = GetNumber(1, end+1)
                    if use_num == end+1:
                        break
                    else:
                        enemy.GetAttacked(player.UseAttackItem(player.FindAttackItem(use_num)))
                        turn+=1
                        return turn
                elif item_num == 3: #파워업 아이템 이용
                    if player.ShowTurnItem() == -1:
                        break
                    end = len(player.turnItem)
                    print(end+1, ": 뒤로가기")
                    use_num = GetNumber(1, end+1)
                    if use_num == end+1:
                        break
                    else:
                        player.UseAttackItem(player.FindTurnItem(use_num))
                        turn+=1
                        return turn
                elif item_num == 4: #뒤로가기
                    break
                else:#에러
                    print("System: 옳지 않은 입력입니다. 1~4번을 입력해 주세요.")
        else:
            print("System: 아직 구현되지 않은 행동입니다. 다른 행동을 선택해주세요.")
            

def EnemyMove(player, enemy):
    move_num = randint(1, 100)
    if move_num > 20:
        hp, total = player.GetAttacked(enemy.DoAttack())
        print(player.name, "의 남은 hp: ", hp)
        return 0
    else:
        enemy.DoNothing()
        player.TotalDEF() #턴은 지나가니 defturn 아이템 사용으로 인한 호출
        return 0