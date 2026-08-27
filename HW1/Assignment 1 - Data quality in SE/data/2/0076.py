__doc__


def fizz_buzz(num1, num2, end_range):
    if not (
        isinstance(num1, int) and isinstance(num2, int) and isinstance(end_range, int)
    ) or (num1 < 0 or num2 < 0 or end_range < 0):
        return "Input should be a positive integer"

    # I'm storing the result to test the returned value aka a list of outputs
    result = []

    for i in range(1, end_range):
        output = i
        if i % num1 == 0 and i % num2 == 0:
            output = "FizzBuzz"
        elif i % num1 == 0:
            output = "Fizz"
        elif i % num2 == 0:
            output = "Buzz"
        result.append(output)
        print(output)

    return result


def test_answer():
    import sys

    answer1 = None
    answer2 = None
    answer3 = None
    try:
        answer1 = fizz_buzz(3, 5, 16)
        answer2 = fizz_buzz(2, 7, 20)
        answer3 = fizz_buzz(100)
    except:
        print("An error occurred:", sys.exc_info()[1])

    assert answer1 == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
    ]
    assert answer2 == [
        1,
        "Fizz",
        3,
        "Fizz",
        5,
        "Fizz",
        "Buzz",
        "Fizz",
        9,
        "Fizz",
        11,
        "Fizz",
        13,
        "FizzBuzz",
        15,
        "Fizz",
        17,
        "Fizz",
        19,
    ]
    assert answer3 == None
