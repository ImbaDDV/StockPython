"""
# @Author: Shi Wei <Minsk>
# @Date:   2019-06-21
# @Email:  250110242@qq.com
# @Project: Craps赌博游戏
#           玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
#           如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
#           玩家再次要色子 如果摇出7点 庄家胜
#           如果摇出第一次摇的点数 玩家胜
#           否则游戏继续 玩家继续摇色子
#           玩家进入游戏时有1000元的赌注 全部输光游戏结束
# @Last modified by:   Minsk
# @Last modified time: 2019-06-22
"""
from random import randint

#赌资
money = 1000

#摇色子
def shake_dice():
    num = randint(1,6) + randint(1,6)
    print('抛出结果为%d' % num)
    return num

while money > 0:
    print('现在你的赌注为：%d元' % money)
    needs_go_on = False

    while True:
        bet = int(input('请下注：'))
        if bet > 0 and bet <= money:
            break
    first_result = shake_dice()
    #玩家赢(第一次)
    if first_result == 7 or first_result == 11:
        print('玩家胜')
        money += bet
    #庄家赢(第一次)
    elif first_result == 2 or first_result == 3 or first_result == 12:
        print('庄家胜')
        money -= bet
    else:
        needs_go_on = True

    while needs_go_on:
        current_result = shake_dice()
        if current_result == 7:
            print('庄家胜')
            money -= bet
            needs_go_on = False
        elif current_result == first_result:
            print('玩家胜')
            money += bet
            needs_go_on = False
            
print('全部输光游戏结束')
