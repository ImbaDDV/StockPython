#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-8-1
# @Author: Minsk
# @Desc  : 
# @File  : SetOnceMappingMixin.py
# @Software : PyCharm

class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict= SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    print(my_dict.KeyError())
print(my_dict)