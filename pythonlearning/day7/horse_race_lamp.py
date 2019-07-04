# @Author: Shi Wei
# @Date:   2019-07-02
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-02

"""
练习1：在屏幕上显示跑马灯文字
"""

import os
import time

def main():
    content = "马鞍山欢迎你，祝你玩得愉快......."
    while True:
        # 清除屏幕上的输出
        os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
