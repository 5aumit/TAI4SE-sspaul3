import sys
num = int(input())
odd_sum = 0
even_sum = 0
odd_smallest = sys.maxsize
even_smallest = sys.maxsize
odd_biggest = -sys.maxsize
even_biggest = -sys.maxsize
for i in range(0, num):
    element = float(input())
    if i % 2 != 0:
        even_sum += element
        if element <= even_smallest:
            even_smallest = element
        if element > even_biggest:
            even_biggest = element
    else:
        odd_sum += element
        if element <= odd_smallest:
            odd_smallest = element
        if element > odd_biggest:
            odd_biggest = element
if num == 0:
    print(f'OddSum=0.00,')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif odd_sum == 0:
    print(f'OddSum=0.00,')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_smallest:.2f},')
    print(f'EvenMax={even_biggest:.2f}')
elif even_sum == 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_smallest:.2f},')
    print(f'OddMax={odd_biggest:.2f},')
    print(f'EvenSum=0.00,')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')

else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_smallest:.2f},')
    print(f'OddMax={odd_biggest:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_smallest:.2f},')
    print(f'EvenMax={even_biggest:.2f}')