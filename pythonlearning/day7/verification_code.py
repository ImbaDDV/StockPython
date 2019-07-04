# @Author: Shi Wei
# @Date:   2019-07-02
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-02

"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""

import random
 
def generate_code(code_len=4):
    # 初始化验证码
    new_code = ''
    # 所有字符
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 生成指定长度的验证码
    new_chars = random.sample(all_chars,code_len)
    # 拼接车字符串
    for i in range(len(new_chars)):
        new_code += new_chars[i]
    print(new_code)


if __name__ == '__main__':
    generate_code(5)
