import sys
import json


with open(__file__.replace('.py', '.txt')) as f:
    problem = f.read()


data = {
    'problem': problem,
    'example': """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""  # should give 42
}


def solve_problem(input):
    parents = {}
    for i, line in enumerate(input.split('\n')):
        about, object = line.split(')')
        parents[object] = about

    orbit_counts = {'COM': 0}

    for object in tuple(parents.keys()):
        stack = [object]
        while stack[-1] not in orbit_counts:
            stack.append(parents[stack[-1]])
        known = orbit_counts[stack.pop()]
        stack.reverse()
        for thing in stack:
            orbit_counts[thing] = orbit_counts[parents[thing]] + 1

    return sum(orbit_counts.values())


# part 1
if sys.argv[-1] in data.keys():
    scenarios = (sys.argv[-1],)
else:
    scenarios = tuple(data.keys())


for scenario in scenarios:
    input = data[scenario]
    r = solve_problem(input)
    print(f'FINAL ANSWER: {r}')


# 932, too low

print('')
print('**** PART 2 ******')


def get_parents(key, parents):
    """Get parents for a particular key through parents dict"""
    r = [key]
    while True:
        this_one = r[-1]
        if this_one == 'COM':
            return r
        r.append(parents[this_one])


def part2(input):
    parents = {}
    for i, line in enumerate(input.split('\n')):
        about, object = line.split(')')
        parents[object] = about

    santa = get_parents('SAN', parents)
    me = get_parents('YOU', parents)

    for i, planet in enumerate(me):
        if planet in santa:
            print(f'met at {planet}')
            print('')
            print(santa[:santa.index(planet) + 1])
            print(len(santa[:santa.index(planet) + 1]))
            # minus one because we want traversials between elements in list
            print(santa.index(planet))
            print('')
            print(me[:i + 1])
            print(len(me[:i + 1]))
            # minus one because we want traversials between elements in list
            print(i)
            # minus another one because transfering to the planet is already counted
            # ...or something like that
            # minus one because problem said so
            return i + santa.index(planet) - 1

data['example'] = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

for scenario in scenarios:
    input = data[scenario]
    r = part2(input)
    print(f'Part 2 answer {r}')

# 432, too high
# 433, too high
# 431, too high
# 430, correct
