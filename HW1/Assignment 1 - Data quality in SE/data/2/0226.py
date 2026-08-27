#!/usr/bin/env python3

import sys

all_neighbors_coord = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            if i != 0 or j != 0 or k != 0:
                all_neighbors_coord.append((i, j, k))

def add_coord(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])

class life:
    def __init__(self, world):
        self.world = world

    def get_world_size(self):
        xs = [c[0] for c in self.world]
        ys = [c[1] for c in self.world]
        zs = [c[2] for c in self.world]
        return ((min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs)))

    def is_active(self, coord):
        return coord in self.world

    def count_active_neighbors(self, coord):
        return len(list(filter(lambda c: self.is_active(add_coord(coord, c)), all_neighbors_coord)))

    def get_next_square_state(self, coord, next_world):
        if self.is_active(coord):
            if self.count_active_neighbors(coord) in [2, 3]:
                next_world[coord] = '#'
        else:
            if self.count_active_neighbors(coord) == 3:
                next_world[coord] = '#'

    def step(self):
        next_world = {}
        ws = self.get_world_size()
        for i in range(ws[0][0]-1,ws[1][0]+2):
            for j in range(ws[0][1]-1,ws[1][1]+2):
                for k in range(ws[0][2]-1,ws[1][2]+2):
                    self.get_next_square_state((i,j,k), next_world)
        self.world = next_world

    def run(self, steps):
        for _i in range(0, steps):
            self.step()
            self.print()

    def count_active(self):
        return len(self.world)

    def print(self):
        ws = self.get_world_size()
        for k in range(ws[0][2], ws[1][2]+1):
            print('z={}'.format(k))
            print()
            for j in range(ws[0][1], ws[1][1]+1):
                s = ''
                for i in range(ws[0][0], ws[1][0]+1):
                    if self.is_active((i,j,k)):
                        s += '#'
                    else:
                        s += '.'
                print(s)
        print()

def parse_world(rows):
    world = {}
    k = 0
    for j, r in enumerate(rows):
        for i, c in enumerate(r):
            if c == '#':
                world[(i,j,k)] = '#'
    return world

inp = 'test.txt'
if len(sys.argv) == 2:
    inp = sys.argv[1]

world = parse_world([r.strip() for r in open(inp, 'r').readlines()])

l = life(world)
l.print()
l.run(6)
print(l.count_active())
