# @Author: Shi Wei
# @Date:   2019-07-04
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-04

"""
计算指定的年月日是这一年的第几天
"""

# def which_day(year,month,date):
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         ]
#     # 判断年份是否为闰年
#     total = 0
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         for i in range(month-1):
#             total += days_of_month[1][i]
#         total += date
#     else:
#         for i in range(month-1):
#             total += days_of_month[0][i]
#         total += date
#
#     return total
#
# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2018, 1, 1))
#     print(which_day(2016, 3, 1))
#
# if __name__ == '__main__':
#     main()

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    print(days_of_month[1])
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()
