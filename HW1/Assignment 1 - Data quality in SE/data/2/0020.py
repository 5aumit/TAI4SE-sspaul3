# coding=utf-8
from cw_performance.speed_contest import SpeedContest

__author__ = 'Cezary Wagner'
__copyright__ = 'Copyright 2015-2018, Cezary K. Wagner.'
__license__ = 'Apache License 2.0'
__version__ = '1.0'


def init():
    global x
    x = 0


def simple_add():
    global x
    x = x + 1


def increment_add():
    global x
    x += 1


if __name__ == '__main__':
    sc = SpeedContest()
    sc.add_function(simple_add, init)
    sc.add_function(increment_add, init)
    sc.timeit_functions(verbose=True)
    sc.repeat_functions(verbose=True)
