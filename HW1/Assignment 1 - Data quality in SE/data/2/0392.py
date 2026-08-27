# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from os import path, getcwd


def get_name_score(l, name):
    idx = l.index(name) + 1
    val = sum([(ord(c) - 64) for c in name])
    return idx * val


class Euler(BaseEuler):
    def solve(self):
        fp = path.join(getcwd(), 'euler/resources/names.txt')
        with open(fp, 'r') as f:
            names = sorted([name for name
                            in f.read().replace('"', '').split(',')])

        return sum([get_name_score(names, name) for name in names])

    @property
    def answer(self):
        return ('The total of all the name scores in the file is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 22:

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?
'''
