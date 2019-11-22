Adds a simple decorator ``enforce_types`` that enables enforcing strict typing on a function or dataclass using annotations.

Works with collection types and subtypes for example ``Dict[str, Tuple[int, int]]``, and with special types as ``Optional`` and ``Any``.

Seeing as this uses type annotations from `PEP 484`_, >=Python 3.5 is required.

PyPi project page: [TBU]

.. _PEP 484: https://www.python.org/dev/peps/pep-0484/

__ PEP484_

Installation
------------

Other than downloading from PyPi with `pip`, you may also clone the repository and run the usual setuptools process::

  $> git clone https://github.com/matchawine/python-static-typing.git && cd python-static-typing
  $> python setup.py {build,install}


Usage
-----

.. code:: python

  from typing import Any, Union, Optional
  from dataclasses import dataclass
  from static_typing import enforce_types

  @enforce_types
  @dataclass(frozen=True)
  class Toto(object):
      what_was_that: Union[str, int]
      something: Any
      name: str = ""
      value: int = 1
      maybe_not: Optional[bool] = None

  >>> Toto(what_was_that=list(), something=2)
  TypeError: Expected type 'typing.Union[str, int]' for attribute 'what_was_that' but received type '<class 'list'>')

  >>> Toto(what_was_that=1, something=2, maybe_not=0)
  TypeError: Expected type 'typing.Union[bool, NoneType]' for attribute 'maybe_not' but received type '<class 'int'>')

  >>> Toto(what_was_that=1, something=2, name=3)
  TypeError: Expected type '<class 'str'>' for attribute 'name' but received type '<class 'int'>')

  >>> Toto(what_was_that=1, something=2, value=3.0)
  TypeError: Expected type '<class 'int'>' for attribute 'value' but received type '<class 'float'>')

  >>> Toto(what_was_that=1, something=2)
  Toto(what_was_that=1, something=2, name='', value=1, maybe_not=None)

  >>> Toto(what_was_that="titi", something=list(), maybe_not=False)
  Toto(what_was_that='titi', something=[], name='', value=1, maybe_not=False)

