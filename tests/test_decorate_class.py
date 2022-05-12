import unittest
from typing import Any, Union, Optional
from dataclasses import dataclass
from enforce_typing import enforce_types


@enforce_types
@dataclass(frozen=True)
class Toto:
    what_was_that: Union[str, int]
    something: Any
    name: str = ""
    value: int = 1
    maybe_not: Optional[bool] = None


class TestDecorateClass(unittest.TestCase):
    def test_enforce_types_class_int(self):
        toto = Toto(what_was_that=1, something=2)
        assert isinstance(toto.what_was_that, int)
        assert isinstance(toto.something, int)
        assert isinstance(toto.name, str)
        assert isinstance(toto.value, int)
        assert toto.maybe_not is None

    def test_enforce_types_class_str(self):
        toto = Toto(what_was_that="titi", something=[], maybe_not=False)
        assert isinstance(toto.what_was_that, str)
        assert isinstance(toto.something, list)
        assert isinstance(toto.name, str)
        assert isinstance(toto.value, int)
        assert toto.maybe_not is False

    def test_list_instead_of_str_or_int(self):
        with self.assertRaises(TypeError):
            Toto(what_was_that=list(), something=2)

    def test_int0_instead_of_bool(self):
        with self.assertRaises(TypeError):
            Toto(what_was_that=1, something=2, maybe_not=0)

    def test_int_instead_of_str(self):
        with self.assertRaises(TypeError):
            Toto(what_was_that=1, something=2, name=3)

    def test_float_instead_of_int(self):
        with self.assertRaises(TypeError):
            Toto(what_was_that=1, something=2, value=3.0)
