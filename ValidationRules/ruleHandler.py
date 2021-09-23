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
    def checkAccount(account_str: str, label: str = "", error_msg: str = ""):
        """
        校验账号通用方法
        :param error_msg: 错误信息
        :param label: 标签主题
        :param account_str: 账号字符串
        :return:
        """
        res = re.match(ReRuleMatch.accountRule.getRuleStr, account_str)
        if res:
            pass
        else:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 非标准账号，需要包含英文+数字或纯英文".format(label, account_str))

    @staticmethod
    def checkMobile(mobile: str, label: str = "", error_msg: str = ""):
        """
        校验手机号通用方法
        :param error_msg: 错误信息
        :param label: 标签主题
        :param mobile: 手机号str
        :return:
        """
        if not mobile.isdigit():
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 手机号非纯数字输入".format(label,mobile))
        if len(mobile) != 11:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 手机号长度不足11位".format(label,mobile))
        reg = re.compile(ReRuleMatch.mobileRule.getRuleStr)
        if not reg.match(mobile):
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 {}".format(label,mobile, ReRuleMatch.mobileRule.getRuleErrorMsg))

    @staticmethod
    def checkKeyWords(verified_str: str, keyword_list: List[str], label: str = "", error_msg: str = ""):
        """
        检查是否包含关键字符
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param keyword_list: 关键字符列表
        :return:
        """
        not_found_keyword_list = [keyword for keyword in keyword_list if not verified_str.find(keyword) >= 0]
        if not_found_keyword_list:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】中找不到关键词 {}".format(label,"、".join(not_found_keyword_list), verified_str))

    @staticmethod
    def checkStartSwitch(verified_str: str, startswith: str = None, label: str = "", error_msg: str = ""):
        """
        检查是否以**开头
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param startswith: 开头关键字
        :return:
        """
        if not verified_str.startswith(startswith):
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】 不是以 {} 为开头".format(label,verified_str, startswith))

    @staticmethod
    def checkEndSwitch(verified_str: str, endswith: str = None, label: str = "", error_msg: str = ""):
        """
        检查是否以**结尾
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param endswith: 结尾关键字
        :return:
        """
        if not verified_str.endswith(endswith):
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】 不是以 {} 为结尾".format(label,verified_str, endswith))

    @staticmethod
    def checkMinLength(verified_str: str, min_length: int = None, label: str = "", error_msg: str = ""):
        """
        检查最小长度限制
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param min_length: 最小长度参数
        :return:
        """
        if not len(verified_str) >= min_length:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】 长度小于 {} 位最小长度限制".format(label,verified_str, min_length))

    @staticmethod
    def checkMaxLength(verified_str: str, max_length: int = None, label: str = "", error_msg: str = ""):
        """
        检查最大长度限制
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param max_length: 最大长度参数
        :return:
        """
        if not len(verified_str) <= max_length:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】 长度大于 {} 位最大长度限制".format(label,verified_str, max_length))

    @staticmethod
    def checkPasswordLevel(verified_str: str, password_level: int = 0, label: str = "", error_msg: str = ""):
        """
        验证密码安全等级
        :param error_msg: 错误信息
        :param label: 标签主题
        :param verified_str: 待验证字符串
        :param password_level: 安全等级
        :return:
        """
        level_match = {
            3: ReRuleMatch.highPasswordRule,
            2: ReRuleMatch.middlePasswordRule,
            1: ReRuleMatch.lowPasswordRule
        }
        res = re.search(level_match[password_level].getRuleStr, verified_str)
        if res:
            pass
        else:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 {}".format(label,verified_str, level_match[password_level].getRuleErrorMsg))

    @classmethod
    def checkPassword(cls, verified_str: str, keyword_list: List[str] = None, startswith: str = None,
                      endswith: str = None,
                      min_length: int = None, max_length: int = None, password_level: int = 0, label: str = "",
                      error_msg: str = ""):

        """
        验证密码通用方法
        :param error_msg: 错误信息
        :param label: 标签主题
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
            cls.checkKeyWords(verified_str, keyword_list,label,error_msg)
        # 判断是否校验开头
        if startswith:
            cls.checkStartSwitch(verified_str, keyword_list,label,error_msg)
        # 判断是否校验结尾
        if endswith:
            cls.checkEndSwitch(verified_str, keyword_list,label,error_msg)
        # 最小长度
        if min_length:
            cls.checkMinLength(verified_str, min_length,label,error_msg)
        # 最大长度
        if max_length:
            cls.checkMaxLength(verified_str, max_length,label,error_msg)
        # 判断鉴定等级
        if password_level != 0:
            cls.checkPasswordLevel(verified_str, password_level,label,error_msg)

    @staticmethod
    def checkEmail(email_str: str, label: str = "", error_msg: str = ""):
        """
        检查是否标准邮箱
        :param error_msg: 错误信息
        :param label: 标签主题
        :param email_str: 邮箱字符串
        :return:
        """
        res = re.match(ReRuleMatch.emailRule.getRuleStr, email_str)
        if res:
            pass
        else:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值 【{}】 {}".format(label,email_str, ReRuleMatch.emailRule))

    @staticmethod
    def checkIDCard(id_str: str, label: str = "", error_msg: str = ""):
        """
        检查是否标准身份证号
        :param error_msg: 错误信息
        :param label: 标签主题
        :param id_str: 身份证号字符串
        :return:
        """
        res = re.match(ReRuleMatch.idRule.getRuleStr, id_str)
        if res:
            pass
        else:
            if error_msg:
                raise ValueError(error_msg)
            raise ValueError("【{}】 输入值【{}】 {}".format(label,id_str, ReRuleMatch.idRule.getRuleErrorMsg))
