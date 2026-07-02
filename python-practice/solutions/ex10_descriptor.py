class TypeValidator:
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
            raise TypeError(
                f"{self.attr_name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(obj, f"_{self.attr_name}", value)


class RangeValidator:
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
                f"{self.attr_name} must be between {self.min_val} and {self.max_val}, "
                f"got {value}"
            )
        setattr(obj, f"_{self.attr_name}", value)
