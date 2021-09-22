#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: rulesHandler
@File: ruleHandler.py
@Author: Symoon
@Date: 2021/9/13 下午2:36
"""

import re
from typing import List

from pydantic import BaseModel

from ValidationRules.reRuleMatch import ReRuleMatch


class RuleHandler(BaseModel):
    """
    验证方法类
    """

    @staticmethod
    def checkAccount(account_str: str):
        """
        校验账号通用方法
        :param account_str: 账号字符串
        :return:
        """
        res = re.match(ReRuleMatch.accountRule.getRuleStr, account_str)
        if res:
            pass
        else:
            raise ValueError("[{}] string is not an standard account".format(account_str))

    @staticmethod
    def checkMobile(mobile: str):
        """
        校验手机号通用方法
        :param mobile: 手机号str
        :return:
        """
        if not mobile.isdigit():
            raise ValueError("[{}] mobile is not digit".format(mobile))
        if len(mobile) != 11:
            raise ValueError("[{}] mobile is not 11 length".format(mobile))
        reg = re.compile(ReRuleMatch.mobileRule.getRuleStr)
        if not reg.match(mobile):
            raise ValueError("[{}] Incorrect mobile phone number".format(mobile))

    @staticmethod
    def checkKeyWords(verified_str: str, keyword_list: List[str]):
        """
        检查是否包含关键字符
        :param verified_str: 待验证字符串
        :param keyword_list: 关键字符列表
        :return:
        """
        not_found_keyword_list = [keyword for keyword in keyword_list if not verified_str.find(keyword) >= 0]
        if not_found_keyword_list:
            raise ValueError("【{}】not found in {}".format("、".join(not_found_keyword_list), verified_str))

    @staticmethod
    def checkStartSwitch(verified_str: str, startswith: str = None):
        """
        检查是否以**开头
        :param verified_str: 待验证字符串
        :param startswith: 开头关键字
        :return:
        """
        if not verified_str.startswith(startswith):
            raise ValueError("{} not startswith {}".format(verified_str, startswith))

    @staticmethod
    def checkEndSwitch(verified_str: str, endswith: str = None):
        """
        检查是否以**结尾
        :param verified_str: 待验证字符串
        :param endswith: 结尾关键字
        :return:
        """
        if not verified_str.endswith(endswith):
            raise ValueError("{} not endswith {}".format(verified_str, endswith))

    @staticmethod
    def checkMinLength(verified_str: str, min_length: int = None):
        """
        检查最小长度限制
        :param verified_str: 待验证字符串
        :param min_length: 最小长度参数
        :return:
        """
        if not len(verified_str) >= min_length:
            raise ValueError("{} length less than minimum limit {}".format(verified_str, min_length))

    @staticmethod
    def checkMaxLength(verified_str: str, max_length: int = None):
        """
        检查最大长度限制
        :param verified_str: 待验证字符串
        :param max_length: 最大长度参数
        :return:
        """
        if not len(verified_str) <= max_length:
            raise ValueError("{} length greater than maximum limit {}".format(verified_str, max_length))

    @staticmethod
    def checkPasswordLevel(verified_str: str, password_level: int = 0):
        """
        验证密码安全等级
        :param verified_str: 待验证字符串
        :param password_level: 安全等级
        :return:
        """
        level_match = {
            3: ReRuleMatch.highPasswordRule.getRuleStr,
            2: ReRuleMatch.middlePasswordRule.getRuleStr,
            1: ReRuleMatch.lowPasswordRule.getRuleStr
        }
        res = re.search(level_match[password_level], verified_str)
        if res:
            pass
        else:
            raise ValueError("[{}] string is not standard".format(verified_str))

    @classmethod
    def checkPassword(cls, verified_str: str, keyword_list: List[str] = None, startswith: str = None,
                      endswith: str = None,
                      min_length: int = None, max_length: int = None, password_level: int = 0):

        """
        验证密码通用方法
        :param verified_str: 待验证字符串
        :param keyword_list: 需要验证的关键字列表
        :param startswith: 以***开头
        :param endswith: 以***结尾
        :param min_length: 最小长度
        :param max_length: 最大长度
        :param password_level: 验证等级，默认为0 {3:"三种必须条件",2:"两种必须条件",3:"必须包含字母及数字",0:"不做验证"}
        :return:
        """
        # 判断是否校验关键字
        if keyword_list:
            cls.checkKeyWords(verified_str, keyword_list)
        # 判断是否校验开头
        if startswith:
            cls.checkStartSwitch(verified_str, keyword_list)
        # 判断是否校验结尾
        if endswith:
            cls.checkEndSwitch(verified_str, keyword_list)
        # 最小长度
        if min_length:
            cls.checkMinLength(verified_str, min_length)
        # 最大长度
        if max_length:
            cls.checkMaxLength(verified_str, max_length)
        # 判断鉴定等级
        if password_level != 0:
            cls.checkPasswordLevel(verified_str, password_level)

    @staticmethod
    def checkEmail(email_str: str):
        """
        检查是否标准邮箱
        :param email_str: 邮箱字符串
        :return:
        """
        res = re.match(ReRuleMatch.emailRule.getRuleStr, email_str)
        if res:
            pass
        else:
            raise ValueError("[{}] string is not an standard email".format(email_str))

    @staticmethod
    def checkIDCard(id_str: str):
        """
        检查是否标准身份证号
        :param id_str: 身份证号字符串
        :return:
        """
        res = re.match(ReRuleMatch.idRule.getRuleStr, id_str)
        if res:
            pass
        else:
            raise ValueError("[{}] string is not an standard idCard".format(id_str))
