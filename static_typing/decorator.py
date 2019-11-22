import typing
import inspect
from contextlib import suppress
from functools import wraps


def enforce_types(wrapped):
    spec = inspect.getfullargspec(wrapped)

    def check_types(*args, **kwargs):
        params = dict(zip(spec.args, args))
        params.update(kwargs)
        for name, value in params.items():
            with suppress(KeyError):
                type_hint = spec.annotations[name]
                if isinstance(type_hint, typing._SpecialForm):
                    continue
                actual_type = getattr(type_hint, "__origin__", type_hint)
                actual_type = type_hint.__args__ if isinstance(actual_type, typing._SpecialForm) else actual_type
                if not isinstance(value, actual_type):
                    raise TypeError(
                        f"Expected type '{type_hint}' for attribute '{name}' but received type '{type(value)}')"
                    )

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
