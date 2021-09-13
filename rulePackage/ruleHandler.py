#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: validationRules
@File: ruleHandler.py
@Author: Symoon
@Date: 2021/9/13 下午2:36
"""

import re
from typing import List

from pydantic import BaseModel

from rulePackage.reRuleMatch import ReRuleMatch


class RuleHandler(BaseModel):
    """
    验证方法类
    """

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
    def checkPassword(verified_str: str, keyword_list: List[str] = None, startswith: str = None, endswith: str = None,
                      min_length: int = None, max_length: int = None, level: int = 3):

        """
        验证密码通用方法
        :param verified_str: 待验证字符串
        :param keyword_list: 需要验证的关键字列表
        :param startswith: 以***开头
        :param endswith: 以***结尾
        :param min_length: 最小长度
        :param max_length: 最大长度
        :param level: 验证等级，默认为3 {3:"必须大小写字母数字以及特殊符号",2:"必须包含大小写字母及数字",3:"必须包含字母及数字",0:"不做验证"}
        :return:
        """
        if level != 0:
            level_match = {
                3: ReRuleMatch.highPasswordRule.getRuleStr,
            }
            res = re.search(level_match[level], verified_str)
            if res:
                pass
            else:
                raise ValueError("[{}] string is not standard".format(verified_str))
