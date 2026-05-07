def FinalScore(player):
    num = 0
    for item in player.attackItem:
        num += item[2]*item[3]
    for item in player.healItem:
        num += item[2]*item[3]
    
    score = player.exp + player.level * 100 + player.money/10 + num + player.floor * 10
    return int(score)