## 基于pydantic的BaseModel下实现的validationRules
##  描述
目前标准结构化的python都开始使用pydantic做结构限制以及校验，每一次的validator都要调用validator装饰器后自己实现。本库是为了整合涵盖所有可能出现的需要校验方法进行封装的规则包。目的是开箱即用注解形式方便使用