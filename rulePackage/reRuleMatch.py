#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: validationRules
@File: reRuleMatch.py
@Author: Symoon
@Date: 2021/9/13 下午1:51
"""

from enum import Enum, unique


@unique
class ReRuleMatch(Enum):
    mobileRule = {"0001": r"(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}"}
    highPasswordRule={"0002":r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$"}

    @property
    def getRuleNumber(self):
        """
        根据美剧名称获取规则序号
        :return:
        """
        return list(self.value.keys())[0]

    @property
    def getRuleStr(self):
        """
        根据美剧名称获取规则语句
        :return: 状态说明message
        """
        return list(self.value.values())[0]


if __name__ == "__main__":
    print(ReRuleMatch.mobileRule.mobileRule.getRuleStr)
