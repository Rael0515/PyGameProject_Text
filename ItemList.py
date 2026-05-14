def getAttackItemList(): #return (list)Item 
    #[[name, Description, damage, price],]
    Item = [["수류탄","던지기 전에는 손에서 꼭 쥐고 놓지 마렴!", 900, 900], 
            ["화염병","파이어 앤드 저스티스!", 800, 800], 
            ["방패","최고의 공격은 방어다!", 500, 500], 
            ["총","대화(물리)", 700, 700]]
    return Item

def getHealItemList(): #return (list)Item 
    #[[name, Description, healingLevel, price],]
    Item = [["빨간포션","최고급 포션이야!", 1000000, 10000], 
            ["파란포션","약간 애매한 중급 포션이야!", 500, 1000], 
            ["초록포션","저급 포션이지만 가격이 매우 싸단다!", 300, 800]]
    return Item

def getTurnItemList():
    #[[name, power, turnatk or turndef, turn, price]]
    Item = [["플러스파워", 10, "turnatk", 5, 800],
            ["디펜드업", 10, "turndef", 5, 800]]
    return Item
    
def getBattleItemList():
    #[[name, description, limit, price]]
    Item = [["삐삐인형", "몬스터의 관심을 끄는 도구. 야생 몬스터와의 배틀에서 반드시 도망칠 수 있다.(특수몬스터, 보스 사용불가)",1, 5000],
            ["몬스터볼", "몬스터를 작은 구체 안에 우겨넣는다. 들어간 몬스터는 꺼낼 수 없다.(특수몬스터, 보스 사용불가)", 1,2000],
            ["투척용 동전", "동전을 던저 몬스터의 환심을 사 도망간다.", 1, 3000]]
    return Item

def getMoveItemList():
    #[[name, description, moveto, price]]
    Item = [["간이캠프", "다음층으로 내려가서 캠프를 설치한다. 설치된 캠프에는 상인이 찾아온다.", "Camp", 8000],
            ["몬스터 페로몬", "다음층에 몬스터 페로몬을 뿌린다. 몬스터가 찾아온다.", "Enemy", 2000]]
    return Item
    
def getIncenseItemList():
    #[[name, description, floor, effect, price]]
    Item = [["행운의 향로", "돈을 두배로 받을 수 있다.", 5, "money_incense", 6000],
            ["무사태평 향로", "", 2, "Enemy_incense", 3000]]
    return Item
