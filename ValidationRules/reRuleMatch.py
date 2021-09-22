#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: rulesHandler
@File: reRuleMatch.py
@Author: Symoon
@Date: 2021/9/13 下午1:51
"""

from enum import Enum, unique


@unique
class ReRuleMatch(Enum):
    # 标准手机号校验规则
    mobileRule = {"非标准手机号": r"(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}"}
    # 满足三种条件  大小写字母数字或者符号
    highPasswordRule = {
        "需要包含大小写字母数字或者符号，满足其中三种条件": r"^(?![a-zA-Z]+$)(?![A-Z0-9]+$)(?![A-Z\\W_!@#$%^&*`~()-+=]+$)(?![a-z0-9]+$)(?![a-z\\W_"
                                    r"!@#$%^&*`~()-+=]+$)(?![0-9\\W_!@#$%^&*`~()-+=]+$)[a-zA-Z0-9\\W_!@#$%^&*`~()-+=]*$"}
    # 满足两种条件字母数字或者符号
    middlePasswordRule = {
        "需要包含字母数字或者符号，满足其中两种条件": r"^(?![a-zA-Z]+$)(?![A-Z\\W_!@#$%^&*`~()-+=]+$)(?![a-z0-9]+$)(?![a-z\\W_"
                                 r"!@#$%^&*`~()-+=]+$)(?![0-9\\W_!@#$%^&*`~()-+=]+$)[a-zA-Z0-9\\W_!@#$%^&*`~()-+=]*$"}
    # 满足数字加字母
    lowPasswordRule = {
        "需要包含字母以及数字": r"^(?=.*\d)(?=.*[a-z]).*$"}

    # 标准邮箱校验规则
    emailRule = {"非标准邮箱": r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"}

    # 标准身份证号校验规则
    idRule = {"非标准身份证号": r"(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)"}

    # 校验账号规则
    accountRule = {"非标准账号": r"^[a-zA-Z][a-zA-Z0-9_]{4,15}$"}

    @property
    def getRuleErrorMsg(self):
        """
        根据枚举名称获取规则序号
        :return:
        """
        return list(self.value.keys())[0]

    @property
    def getRuleStr(self):
        """
        根据枚举名称获取规则语句
        :return: 状态说明message
        """
        return list(self.value.values())[0]


if __name__ == "__main__":
    print(ReRuleMatch.mobileRule.mobileRule.getRuleStr)
