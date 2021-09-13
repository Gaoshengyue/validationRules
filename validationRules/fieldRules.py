from pydantic import BaseModel
from typing import List
import re
from functools import wraps
from publicLib.structureFunc import doubleWrap


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
                if not mobile.isdigit():
                    raise ValueError("[{}] mobile is not digit".format(mobile))
                if len(mobile) != 11:
                    raise ValueError("[{}] mobile is not 11 length".format(mobile))
                reg = re.compile(r"(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}")
                if not reg.match(mobile):
                    raise ValueError("[{}] Incorrect mobile phone number".format(mobile))
            return func(*args, **kwargs)

        return checkMobile
