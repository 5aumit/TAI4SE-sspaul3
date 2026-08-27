def show_characters_v1(name):
    for index in range(len(name)):
        print(name[index], end=' ')
    else:
        print()


def show_characters_v2(name):
    end_count = -1 * (len(name) + 1)
    for index in range(-1, end_count, -1):
        print(name[index], end=' ')
    else:
        print()


def show_reverse_string(data):
    print(data[::-1])


def show_swapcase(data):
    print(data.swapcase())
