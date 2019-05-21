import math
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""
"""
F = float(input('华氏温度为:'))
#摄氏温度为
C = (F-32)/1.8
print('华氏温度为:%.1f,摄氏温度为:%.1f' % (F,C))
"""
"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
"""
radius = float(input('圆的半径为:'))
#圆的周长
perimeter = 2 * math.pi * radius
#圆的面积
area = math.pi * radius**2
print('圆的周长:%.2f,圆的面积:%.2f' % (perimeter,area))
"""
"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = int(input('输入年份:'))
#判断年份是否为闰年
def check_the_year_is_leapyear(year):
	#判断闰年
	if(year % 4 == 0 and year % 100 !=0):
		return True
	else:
		if(year % 400 == 0):
			return True
		else:
			return False
		return False
		
#is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)		
print(check_the_year_is_leapyear(year))
