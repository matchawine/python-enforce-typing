import typing
import inspect
from functools import wraps


def enforce_types(wrapped):
    spec = inspect.getfullargspec(wrapped)

    def check_types(*args, **kwargs):
        passed_args = get_passed_arguments(args, kwargs)
        for name, value in passed_args.items():
            type_hint = spec.annotations.get(name, typing.Any)
            if isinstance(type_hint, typing._SpecialForm):
                continue
            actual_type = get_origin_if_special_form(type_hint)
            if not isinstance(value, actual_type):
                raise TypeError(
                    f"Expected type '{type_hint}' for attribute '{name}'"
                    f" but received type '{type(value)}')"
                )

    def get_origin_if_special_form(type_hint):
        """e.g. returns Union for type_hint=Union[int, str]
        """
        actual_type = getattr(type_hint, "__origin__", type_hint)
        if isinstance(actual_type, typing._SpecialForm):
            actual_type = type_hint.__args__
        return actual_type

    def get_passed_arguments(args, kwargs) -> dict:
        params = dict(zip(spec.args, args))
        params.update(kwargs)
        return params

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            check_types(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    if inspect.isclass(wrapped):
        wrapped.__init__ = decorate(wrapped.__init__)
        return wrapped

    return decorate(wrapped)
