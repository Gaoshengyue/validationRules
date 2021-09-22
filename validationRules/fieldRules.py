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

from ..publicLib.structureFunc import doubleWrap
from ..rulePackage.ruleHandler import RuleHandler


class StringRules(BaseModel):

    @staticmethod
    @doubleWrap
    def accountRule(func, required: bool = False):
        """
        账号合法校验
        :param func:
        :param required: 是否必填
        :return:
        """

        @wraps(func)
        def checkAccount(*args, **kwargs):
            """
            校验账号合法
            :param args:
            :param kwargs:
            :return:
            """
            account_list: List[str] = [str(account) for account in args if type(account) == str]
            if required and not account_list:
                raise ValueError("{} is not allowed value,check input".format(account_list))
            for account_str in account_list:
                RuleHandler.checkAccount(account_str)
            return func(*args, **kwargs)

        return checkAccount

    @staticmethod
    @doubleWrap
    def mobileRule(func, required: bool = False):
        """
        标准手机号校验
        :param func:被装饰check函数
        comment:支持数字类型手机号。但一般不推荐用数字存储手机号
        :param required: 是否必填
        """

        @wraps(func)
        def checkMobile(*args, **kwargs):
            """
            校验手机号
            :param args:
            :param kwargs:
            :return:
            """
            mobile_str_list: List[str] = [str(mobile) for mobile in args if type(mobile) == str or type(mobile) == int]
            if required and not mobile_str_list:
                raise ValueError("{} is not allowed value,check input".format(mobile_str_list))

            for mobile_str in mobile_str_list:
                RuleHandler.checkMobile(mobile_str)
            return func(*args, **kwargs)

        return checkMobile

    @staticmethod
    @doubleWrap
    def keywordCheckRule(func, keyword_list: List[str] = None, startswith: str = None, endswith: str = None,
                         min_length: int = None, max_length: int = None, password_level: int = 0,
                         required: bool = False):
        """
        输入字符验证
        :param func: 被装饰check函数
        :param keyword_list: 关键字列表
        :param startswith: 以***为开头
        :param endswith: 以***为结尾
        :param min_length: 最小长度
        :param max_length: 最大长度
        :param password_level: 验证等级，默认为0 {3:"三种必须条件",2:"两种必须条件",3:"必须包含字母及数字",0:"不做验证"}
        :param required: 是否必填
        :return:
        """

        @wraps(func)
        def checkKeyword(*args, **kwargs):
            verified_str_list: List[str] = [str(verified_str) for verified_str in args if type(verified_str) == str]
            if required and not verified_str_list:
                raise ValueError("{} is not allowed value,check input".format(verified_str_list))
            for verified_str in verified_str_list:
                RuleHandler.checkPassword(verified_str, keyword_list=keyword_list, startswith=startswith,
                                          endswith=endswith, min_length=min_length,
                                          max_length=max_length,
                                          password_level=password_level)
            return func(*args, *kwargs)

        return checkKeyword

    @staticmethod
    @doubleWrap
    def emailRule(func, required: bool = False):
        """
        标准邮箱校验

        :param func:
        :param required: 是否必填
        :return:
        """

        @wraps(func)
        def checkEmail(*args, **kwargs):
            email_str_list = [str(email_str) for email_str in args if type(email_str) == str]
            if required and not email_str_list:
                raise ValueError("{} is not allowed value,check input".format(email_str_list))
            for email_str in email_str_list:
                RuleHandler.checkEmail(email_str)
            return func(*args, **kwargs)

        return checkEmail

    @staticmethod
    @doubleWrap
    def IDCardRule(func, required: bool = False):
        """
        身份证号校验
        :param func:
        :param required: 是否必填
        :return:
        """

        @wraps(func)
        def checkIDCard(*args, **kwargs):
            """
            校验身份证号
            :param args:
            :param kwargs:
            :return:
            """
            id_str_list = [str(id_str) for id_str in args if type(id_str) == str]
            if required and not id_str_list:
                raise ValueError("{} is not allowed value,check input".format(id_str_list))
            for id_str in id_str_list:
                RuleHandler.checkIDCard(id_str)
            return func(*args, **kwargs)

        return checkIDCard
