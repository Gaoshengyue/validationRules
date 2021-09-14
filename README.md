## 基于pydantic的BaseModel下实现的validationRules
##  描述
目前标准结构化的python都开始使用pydantic做结构限制以及校验，每一次的validator都要调用validator装饰器后自己实现。本库是为了整合涵盖所有可能出现的需要校验方法进行封装的规则包。目的是开箱即用注解形式方便使用
## 前置
需要配合pydantic的validator使用

## 使用方式

例如：校验该字段是否是标准手机号
```python3
from pydantic import BaseModel, Field, validator

from validationRules.fieldRules import StringRules


class TestUserBase(BaseModel):
    userName: str = Field(description="用户名", alias="user_name")
    mobileNumber: str = Field(description="手机号", alias="mobile_number")
    password: str = Field(description="密码", alias="password")
    email: str = Field(description="邮箱", alias="email")
    IDCard: str = Field(description="身份证号", alias="id_card")

    @validator("userName")
    @StringRules.accountRule
    def check_account(cls, column):
        return column

    @validator("mobileNumber")
    @StringRules.mobileRule
    def check_mobile_number(cls, column):
        return column

    @validator("password")
    @StringRules.keywordCheckRule(password_level=1, min_length=8)
    def check_keyword(cls, column):
        return column

    @validator("email")
    @StringRules.emailRule(required=True)
    def check_email(cls, column):
        return column

    @validator("IDCard")
    @StringRules.IDCardRule(required=True)
    def check_id_card(cls, column):
        return column


# user_obj: TestUserBase = TestUserBase(
#
#     user_name="symoon",
#     mobile_number="13232633123"
# )
#
# print(user_obj)
# userName='symoon' mobileNumber='13232633123'

user_obj: TestUserBase = TestUserBase(

    user_name="symoon",
    mobile_number="13232633123",
    password="gsy121994",
    email="fsdfsfsf@qq.com",
    id_card="130303199412190919"
)
print(user_obj)
# [132326331231] mobile is not 11 length (type=value_error)
```
