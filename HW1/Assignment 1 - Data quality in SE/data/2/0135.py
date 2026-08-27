# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

def read_data(filename):
  goals = {}
  with open(filename,'rb') as f:
    reader = csv.reader(f)
    headers = reader.next()

    for row in reader:
      name, for_, against_, = row[0], row[5], row[6]

      goals[name] = {}
      goals[name]['for'] = int(for_)
      goals[name]['against'] = int(against_)

  return goals

def get_team_with_min_score_difference(goals):
  min_diff = 9999
  min_name = ''

  for name in goals:
    diff = abs(goals[name]['for'] - goals[name]['against'])

    if diff < min_diff:
      min_diff, min_name = diff, name

  return min_name, min_diff



goals = read_data('football.csv')
min_name, min_diff = get_team_with_min_score_difference(goals)

print("The team with the smallest 'for' vs. 'against' difference is {0}: with a difference of {1}".format(min_name, min_diff))

# Aston_Villa
# 1
