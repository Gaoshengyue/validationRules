from pydantic import BaseModel, Field, validator
from validationRules.fieldRules import StringRules


class TestUserBase(BaseModel):
    userName: str = Field(description="用户名", alias="user_name")
    mobileNumber: str = Field(description="手机号", alias="mobile_number")
    password: str = Field(description="密码", alias="password")

    @validator("mobileNumber")
    @StringRules.mobileRule
    def check_mobile_number(cls, column):
        return column

    @validator("password")
    @StringRules.keywordCheckRule(level=3)
    def check_password(cls, column):
        return column


user_obj: TestUserBase = TestUserBase(

    user_name="symoon",
    mobile_number="13232633123",
    password="Gsy121994*"
)

print(user_obj)
