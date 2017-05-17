# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the deco')
        func()
        print('After deco')
    return function_that_runs_func


@my_decorator
def my_function():
    print('im the function')

my_function()

# trial
