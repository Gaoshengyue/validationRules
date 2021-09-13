from functools import wraps


def doubleWrap(func):
    """
    解决装饰器可忽略括号的方案
    """
    @wraps(func)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return func(args[0])
        else:
            return lambda real_func: func(real_func, *args, **kwargs)

    return new_dec
