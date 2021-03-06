#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nrel_5mw_controller.skeleton import fib

__author__ = "Rick Lupton"
__copyright__ = "Rick Lupton"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
