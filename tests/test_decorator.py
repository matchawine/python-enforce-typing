import pytest
from typing import Any, Union, Optional
from dataclasses import dataclass
from static_typing import enforce_types


def test_enforce_types_class():
    @enforce_types
    @dataclass(frozen=True)
    class Toto(object):
        what_was_that: Union[str, int]
        something: Any
        name: str = ""
        value: int = 1
        maybe_not: Optional[bool] = None

    toto = Toto(what_was_that=1, something=2)
    assert isinstance(toto.what_was_that, int)
    assert isinstance(toto.something, int)
    assert isinstance(toto.name, str)
    assert isinstance(toto.value, int)
    assert toto.maybe_not is None

    toto = Toto(what_was_that="titi", something=list(), maybe_not=False)
    assert isinstance(toto.what_was_that, str)
    assert isinstance(toto.something, list)
    assert isinstance(toto.name, str)
    assert isinstance(toto.value, int)
    assert toto.maybe_not is False

    with pytest.raises(TypeError):
        Toto(what_was_that=list(), something=2)
    with pytest.raises(TypeError):
        Toto(what_was_that=1, something=2, maybe_not=0)
    with pytest.raises(TypeError):
        Toto(what_was_that=1, something=2, name=3)
    with pytest.raises(TypeError):
        Toto(what_was_that=1, something=2, value=3.0)


def test_enforce_types_function():
    @enforce_types
    def function(
        what_was_that: Union[str, int],
        something: Any,
        name: str = "",
        value: int = 1,
        maybe_not: Optional[bool] = None,
        no_hint=None,
    ):
        assert isinstance(what_was_that, (int, str))
        assert something or not something
        assert isinstance(name, str)
        assert isinstance(value, int)
        assert maybe_not is None or isinstance(maybe_not, bool)
        assert no_hint or not no_hint

    function(what_was_that=1, something=2)
    function(what_was_that="toto", something=list(), maybe_not=False, no_hint=1.0)
    with pytest.raises(TypeError):
        function(what_was_that=list(), something=2)
    with pytest.raises(TypeError):
        function(what_was_that=1, something=2, maybe_not=1)
    with pytest.raises(TypeError):
        function(what_was_that=1, something=2, name=3)
    with pytest.raises(TypeError):
        function(what_was_that=1, something=2, value=3.0)
