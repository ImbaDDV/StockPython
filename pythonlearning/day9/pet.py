#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-5 21:35
# @Author : Minsk
# @Site : 
# @File : pet.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod


# 抽象类，无法被实例化
class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


# 子类
class Dog(Pet):

    def make_voice(self):
        print("%s:汪汪汪" % self._nickname)


# 子类
class Cat(Pet):

    def make_voice(self):
        print("%s:喵喵喵" % self._nickname)


def main():
    pets = [Dog("柯基"), Cat("猫"), Dog("金毛")]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
