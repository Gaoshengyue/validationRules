from pydantic import BaseModel
from typing import List
import re
from functools import wraps


def doubleWrap(f):
    @wraps(f)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return f(args[0])
        else:
            return lambda real_func: f(real_func, *args, **kwargs)

    return new_dec


class StringRules(BaseModel):

    @staticmethod
    @doubleWrap
    def mobileRule(func):
        """
        标准手机号校验
        func:被装饰check函数
        """

        @wraps(func)
        def checkMobile(*args, **kwargs):
            mobile_list: List[str] = []
            [mobile_list.append(str(mobile)) for mobile in args]
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

