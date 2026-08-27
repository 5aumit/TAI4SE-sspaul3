#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Problem definition:

Write three functions that compute the sum of the numbers in a given list using
a for-loop, a while-loop, and recursion.

"""

import sys


def calculate_sum_using_for_loop(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


def calculate_sum_using_while_loop(numbers):
    result = 0
    index = 0
    while index < len(numbers):
        result += numbers[index]
        index += 1

    return result


def calculate_sum_using_recursion(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + calculate_sum_using_recursion(numbers[1:])


def main():
    numbers = [1, 5, 6, 31, 55, 0, -5, 6]
    result_using_for_loop = calculate_sum_using_for_loop(numbers)
    result_using_while_loop = calculate_sum_using_while_loop(numbers)
    result_using_recursion = calculate_sum_using_recursion(numbers)
    assert result_using_for_loop == result_using_while_loop == result_using_recursion, \
        "Results form sum operations do not match!!: " \
        "For loop: {}, While loop {}, Recursion {}".format(result_using_for_loop,
                                                           result_using_while_loop,
                                                           result_using_recursion)


if __name__ == '__main__':
    sys.exit(main())
