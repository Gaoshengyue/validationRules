#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: validationRules
@File: reRuleMatch.py
@Author: Symoon
@Date: 2021/9/13 下午1:51
"""

from functools import wraps
from typing import List

from pydantic import BaseModel

from publicLib.structureFunc import doubleWrap
from rulePackage.ruleHandler import RuleHandler


class StringRules(BaseModel):

    @staticmethod
    @doubleWrap
    def mobileRule(func):
        """
        标准手机号校验
        func:被装饰check函数
        comment:支持数字类型手机号。但一般不推荐用数字存储手机号
        """

        @wraps(func)
        def checkMobile(*args, **kwargs):
            mobile_list: List[str] = []
            [mobile_list.append(str(mobile)) for mobile in args if type(mobile) == str or type(mobile) == int]
            for mobile in mobile_list:
                RuleHandler.checkMobile(mobile)
            return func(*args, **kwargs)

        return checkMobile

    @staticmethod
    @doubleWrap
    def keywordCheckRule(func, keyword_list: List[str] = None, startswith: str = None, endswith: str = None,
                         min_length: int = None, max_length: int = None, level: int = 3):
        """
        输入字符验证
        :param func: 被装饰check函数
        :param keyword_list: 关键字列表
        :param startswith: 以***为开头
        :param endswith: 以***为结尾
        :param min_length: 最小长度
        :param max_length: 最大长度
        :param level: 验证登记 默认为3   {3:"必须大小写字母数字以及特殊符号",2:"必须包含大小写字母及数字",3:"必须包含字母及数字",0:"不做验证"}
        :return:
        """

        @wraps(func)
        def checkKeyword(*args, **kwargs):
            verified_str_list = [str(verified_str) for verified_str in args if type(verified_str) == str]

            for verified_str in verified_str_list:
                RuleHandler.checkPassword(verified_str, keyword_list=keyword_list, startswith=startswith,
                                          endswith=endswith, min_length=min_length,
                                          max_length=max_length,
                                          level=level)
            return func(*args, *kwargs)

        return checkKeyword
