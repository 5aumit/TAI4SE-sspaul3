# coding=utf-8
"""Advent of Code 2018, Day 7"""

import networkx
import re

G = networkx.DiGraph()
with open("puzzle_input") as f:
    for line in f.read().split("\n"):
        match = re.search("Step (?P<pre>[A-Z]).*step (?P<post>[A-Z])", line)
        G.add_edge(match.group("pre"), match.group("post"))


def part_one():
    """Solution to Part 1"""
    return "".join(networkx.lexicographical_topological_sort(G))


def part_two():
    """Solution to Part 2"""
    tasks = {}
    current_time = 0
    while G.nodes():
        # noinspection PyCallingNonCallable
        candidate_next_tasks = [task for task in G.nodes()
                                if task not in tasks.keys() and G.in_degree(task) == 0]
        if candidate_next_tasks and len(tasks) < 5:
            next_task = sorted(candidate_next_tasks)[0]
            tasks[next_task] = ord(next_task) - 4
        else:
            min_task_time = min(tasks.values())
            current_time += min_task_time
            completed_task = dict(zip(tasks.values(), tasks.keys()))[min_task_time]
            tasks = {k: v - min_task_time for k, v in tasks.items() if k != completed_task}
            G.remove_node(completed_task)
    return current_time
