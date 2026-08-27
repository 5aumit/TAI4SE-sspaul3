#!/usr/bin/python3
"""100-my-int"""


class MyInt(int):
    """MyInt"""
    def __new__(cls, value):
        """new"""
        return  super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        """equal"""
        return  super(MyInt, self).__ne__(other)
    def __ne__(self, other): 
        """ne"""
        return super(MyInt, self).__eq__(other)