# @Author: Shi Wei
# @Date:   2019-07-04
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-05

"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

#创造30个人
def mymain():
    people = [x for x in range(1,31)]
    #print(people)
    #9次一轮回的计数器
    counter, index, number = 0, 0, 0
    while counter < 15:
        for index in range(30):
            if people[index] != 'X':
                number += 1
                if number == 9:
                    people[index] = 'X'
                    counter += 1
                    number = 0
            else:
                continue
    for person in people:
        print('基' if person !='X' else '非', end='')

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()
    print()
    mymain()
