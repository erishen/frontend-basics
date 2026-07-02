# 描述符（Descriptor）
# 实现类型验证描述符


class TypeValidator:
    """
    描述符：验证属性类型。
    用法：
        class Person:
            name = TypeValidator("name", str)
            age = TypeValidator("age", int)
    赋值时类型不匹配应抛出 TypeError。
    """
    # TODO: 在这里实现 __init__, __get__, __set__
    def __init__(self, name, expected_type):
        self.attr_name = name
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.attr_name = name 

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.attr_name}", None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.attr_name} must be {self.expected_type.__name__}")
        setattr(obj, f"_{self.attr_name}", value)


class RangeValidator:
    """
    描述符：验证数值范围。
    用法：
        class Config:
            port = RangeValidator("port", 1, 65535)
    赋值时超出范围应抛出 ValueError。
    """
    # TODO: 在这里实现 __init__, __get__, __set__
    def __init__(self, name, min_val, max_val):
        self.attr_name = name 
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.attr_name = name 

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.attr_name}", None)

    def __set__(self, obj, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(
                f"{self.attr_name} must be between {self.min_val} and {self.max_val}"
            )
        setattr(obj, f"_{self.attr_name}", value)


