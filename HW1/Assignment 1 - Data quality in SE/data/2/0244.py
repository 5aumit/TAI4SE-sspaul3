import common
year_common = common.import_year_common(2019)

tape = common.extract_numbers(common.read_file('2019/25/data.txt'))

moves = [
    'south',
    'take monolith',
    'east',
    'take asterisk',
    'west',
    'north',
    # 'west',
    # 'take coin',
    # 'north',
    # 'east',
    # 'take astronaut ice cream',
    # 'west',
    # 'south',
    # 'east',
    'north',
    'north',
    # 'take mutex',
    'west',
    'take astrolabe',
    'west',
    # 'take dehydrated water',
    'west',
    'take wreath',
    'east',
    'south',
    'east',
    'north',
    'north'
]

def gen_input():
    for move in moves:
        for c in move:
            yield ord(c)
        yield 10
    # manual controls
    # while True:
    #     inp = input()
    #     for c in inp:
    #         yield ord(c)
    #     yield 10

mem = year_common.tape_to_mem(tape)
it = year_common.run_intcode(mem, gen_input())

for c in it:
    print(chr(c), end='')
