def get_sets(problem):
    first_choice = int(problem[0]) - 1
    second_choice = int(problem[5]) - 1

    f_line = problem[1:5][first_choice]
    s_line = problem[6:11][second_choice]

    first_set = {x for x in f_line.strip().split(' ')}
    second_set = {x for x in s_line.strip().split(' ')}
    return first_set, second_set


def chunks(l, n):
    if n<1:
        n=1
    return [l[i:i+n] for i in range(0, len(l), n)]

def solve(set_one, set_two):
    inters = set_one.intersection(set_two)
    leng = len(inters)
    if leng == 1:
        return inters.pop()
    elif leng == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main():
    content = None
    with open("input.txt", "r") as f:
        content = f.read().strip()

    lines = [x.strip() for x in content.split('\n')]
    test_cases = int(lines[0])
    probs = chunks(lines[1:], 10)
    with open("output.txt", "w") as f:
        for i, el in enumerate([solve(*get_sets(l)) for l in probs]):
            f.write("Case #{}: {}\n".format(i+1, el))

if __name__ == '__main__':
    main()
