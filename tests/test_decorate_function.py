import unittest
from typing import Any, Union, Optional
from enforce_typing import enforce_types


@enforce_types
def function(
    what_was_that: Union[str, int],
    something: Any,
    name: str = "",
    value: int = 1,
    maybe_not: Optional[bool] = None,
    no_hint=None,
):
    pass


class TestDecorateFunction(unittest.TestCase):
    def test_all_good_use_defaults(self):
        function(what_was_that=1, something=2)

    def test_all_good_provide_all(self):
        function(what_was_that="toto", something=list(), maybe_not=False, no_hint=1.0)

    def test_no_hint_can_be_str(self):
        function(what_was_that=1, something=2, no_hint="yes")

    def test_no_hint_can_be_int(self):
        function(what_was_that=1, something=2, no_hint=1)

    def test_list_instead_of_str_or_int(self):
        with self.assertRaises(TypeError):
            function(what_was_that=list(), something=2)

    def test_int1_instead_of_bool(self):
        with self.assertRaises(TypeError):
            function(what_was_that=1, something=2, maybe_not=1)

    def test_int_instead_of_str(self):
        with self.assertRaises(TypeError):
            function(what_was_that=1, something=2, name=3)

    def test_float_instead_of_int(self):
        with self.assertRaises(TypeError):
            function(what_was_that=1, something=2, value=3.0)
