# Failure inspection evidence

AI-assisted static code-reading worksheet. The author must review the labels.

The sample is purposive, not a random estimate of failure prevalence.

Cycle 1 cases are initial coding failures, not evidence of loop-induced drift.


## 1. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/71 / cycle 2

Category: type_handling. Confidence: high.

Observation: int(gap / 1.3) becomes gap // 1.3; the resulting float is passed to range().

Interpretation: The algorithm is retained, but numeric type information is lost during regeneration.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
```


Last passing code:
```python
def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst
```


Description fed into failure:
```text
"""
**FUNCTION** comb_sort(INPUTS)
  **INPUTS**
    lst (list)

  **OUTPUT**
    sorted list

  **STEPS**
    1. Initialize gap to the length of lst
    2. Initialize swapped to True
    3. While gap is not 1 or swapped is True
      3.1. Set gap to the maximum of 1 and the integer division of gap by 1.3
      3.2. Set swapped to False
      3.3. For each index i from 0 to the length of lst minus gap
        3.3.1. If the element at index i is greater than the element at index i plus gap
          3.3.1.1. Swap the elements at index i and index i plus gap
          3.3.1.2. Set swapped to True
    4. Return lst

  **END FUNCTION**
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
```


Failing code:
```python
def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap != 1 or swapped:
        gap = max(1, gap // 1.3)
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst
```


## 2. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/111 / cycle 2

Category: generation_error. Confidence: high.

Observation: The description requests intersection across nested lists; regenerated code intersects with set(flat_list[0]), where flat_list[0] is an integer.

Interpretation: The description retains the intent, but regenerated code uses an invalid operation on an element.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
```


Last passing code:
```python
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return set(flat_list).intersection(*nested_lists)
```


Description fed into failure:
```text
"""
FUNCTION common_in_nested_lists(INPUTS nested_lists)
    INPUTS: nested_lists (list of lists)

    OUTPUT: set of common elements in all nested lists

    STEPS
    1. Create a new list called flat_list by iterating over each sublist in nested_lists
    2. For each sublist, iterate over each item and add it to flat_list
    3. Convert flat_list to a set
    4. Use the intersection method to find the common elements in all nested lists
    5. Return the set of common elements

    END FUNCTION
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
```


Failing code:
```python
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return set(flat_list) & set(flat_list[0])
```


## 3. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/61 / cycle 4

Category: generation_error. Confidence: high.

Observation: The description says sum of digits; regenerated code compares int(substring) with its length.

Interpretation: The model fails to implement its own still-correct description.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
```


Last passing code:
```python
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring.isdigit():
                if sum(int(digit) for digit in substring) == len(substring):
                    count += 1
    return count
```


Description fed into failure:
```text
"""
FUNCTION count_Substrings(INPUTS s)
    INPUTS
        s: string

    OUTPUT
        count: integer

    STEPS
        count = 0
        FOR i FROM 0 TO length(s) - 1
            FOR j FROM i + 1 TO length(s)
                substring = characters of s from index i to j
                IF substring contains only digits
                    IF sum of digits in substring equals length of substring
                        count = count + 1
    END FUNCTION

    RETURN count
assert count_Substrings('112112') == 6
"""
```


Failing code:
```python
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring.isdigit() and int(substring) == len(substring):
                count += 1
    return count
```


## 4. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/94 / cycle 10

Category: representation_drift. Confidence: high.

Observation: The last description replaces the first tuple value with the index of the minimum-second-value tuple. Regenerated code returns an index.

Interpretation: The description changes the required output, and the next implementation follows that change.

Base passed: False; plus passed: False.


Original task:
```text
"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
```


Last passing code:
```python
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
```


Description fed into failure:
```text
"""
FUNCTION index_minimum

INPUTS: lst (a list of lists)

OUTPUT: the index of the sublist with the minimum second element

STEPS:
  1. Find the sublist with the minimum second element in lst
  2. Return the index of this sublist

FUNCTION index_minimum
END FUNCTION
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
```


Failing code:
```python
def index_minimum(lst):
    return min(enumerate(lst), key=lambda x: x[1][1])[0]
```


## 5. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/57 / cycle 3

Category: syntax_error. Confidence: high.

Observation: The regenerated return expression is missing a closing parenthesis.

Interpretation: Functional failure occurs despite a description that preserves the digit-concatenation task.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
```


Last passing code:
```python
def find_Max_Num(digits):
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))
```


Description fed into failure:
```text
"""
**FUNCTION** find_Max_Num
**INPUTS**
  - digits: a list of integers

**STEPS**
  1. Sort the list of digits in descending order
  2. Convert each digit in the sorted list to a string
  3. Join the strings together into a single string
  4. Convert the string back to an integer
  5. Return the resulting integer

**OUTPUT**
  - The largest possible integer that can be formed by concatenating the input digits

**END FUNCTION**
assert find_Max_Num([1,2,3]) == 321
"""
```


Failing code:
```python
def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True)))
```


## 6. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/139 / cycle 5

Category: representation_drift. Confidence: high.

Observation: The description turns scalar radius into INPUTS[0]; regenerated code indexes the scalar argument.

Interpretation: The representation changes the argument contract despite retaining an example assertion.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""
```


Last passing code:
```python
import math

def circle_circumference(radius):
  return 2 * math.pi * radius
```


Description fed into failure:
```text
"""
FUNCTION circle_circumference(INPUTS)
  radius = INPUTS[0]
  OUTPUT = 2 * math.pi * radius
END FUNCTION
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""
```


Failing code:
```python
import math

def circle_circumference(INPUTS):
  radius = INPUTS[0]
  return 2 * math.pi * radius

assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
```


## 7. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/277 / cycle 7

Category: representation_drift. Confidence: high.

Observation: The description invents a negative-threshold rule; regenerated code returns an empty dictionary for n < 0. Base tests pass and plus tests fail.

Interpretation: Added edge-case statements can introduce incorrect requirements. Extended tests expose the change.

Base passed: True; plus passed: False.


Original task:
```text
"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
```


Last passing code:
```python
def dict_filter(d, n):
    filtered_dict = {}
    for key, value in d.items():
        if value >= n:
            filtered_dict[key] = value
    return filtered_dict

assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
```


Description fed into failure:
```text
"""
FUNCTION dict_filter
    INPUTS
        d (dictionary): input dictionary
        n (number): threshold value

    OUTPUT
        filtered dictionary

    STEPS
    1. Create an empty dictionary called filtered_dict
    2. For each key-value pair in the input dictionary d
        2.1 If the value is greater than or equal to the threshold n
            2.1.1 Add the key-value pair to the filtered_dict
    3. Return the filtered_dict

    END FUNCTION

    EDGE CASES
    - If the input dictionary is empty, the function returns an empty dictionary
    - If the threshold value is negative, the function returns an empty dictionary
    - If the threshold value is not a number, the function raises a TypeError
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
```


Failing code:
```python
def dict_filter(d, n):
    if not isinstance(n, (int, float)) or n < 0:
        return {}
    filtered_dict = {}
    for k, v in d.items():
        if v >= n:
            filtered_dict[k] = v
    return filtered_dict
```


## 8. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/64 / cycle 8

Category: representation_drift. Confidence: high.

Observation: The passing code sorts ascending; the description says descending and the next code adds reverse=True.

Interpretation: Pseudocode can reverse a requirement even when the original assertion remains visible.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
```


Last passing code:
```python
def subject_marks(inputs):
    return sorted(inputs, key=lambda x: x[1])
```


Description fed into failure:
```text
"""
FUNCTION subject_marks(INPUTS)
  INPUTS: a list of tuples, where each tuple contains a subject and its marks

  OUTPUT: a sorted list of tuples, where each tuple contains a subject and its marks, sorted by marks in descending order

  STEPS
    1. Sort the input list of tuples in descending order based on the marks
    2. Return the sorted list of tuples

  END FUNCTION
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
```


Failing code:
```python
def subject_marks(INPUTS):
    return sorted(INPUTS, key=lambda x: x[1], reverse=True)
```


## 9. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/141 / cycle 9

Category: generation_error. Confidence: high.

Observation: The description retains ascending pancake sort; regenerated code searches suffixes while applying prefix flips.

Interpretation: The algorithm is regenerated incorrectly; the observed code fails tests.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
```


Last passing code:
```python
def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_idx = arr[:size].index(max(arr[:size])) + 1
        if max_idx != size:
            arr[:max_idx] = arr[:max_idx][::-1]
            arr[:size] = arr[:size][::-1]
    return arr
```


Description fed into failure:
```text
"""
FUNCTION pancake_sort(arr)

INPUTS
  arr: a list of elements to be sorted

OUTPUT
  the input list sorted in ascending order

STEPS
  1. Find the length of the input list
  2. Loop through the list from the last element to the first element
  3. In each iteration, find the index of the maximum element in the current slice of the list
  4. If the index of the maximum element is not equal to the current slice size, 
     4.1. Reverse the slice of the list from the start to the index of the maximum element
     4.2. Reverse the slice of the list from the start to the current slice size
  5. Repeat steps 3 and 4 until the slice size is 1
  6. Return the sorted list

END FUNCTION
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
```


Failing code:
```python
def pancake_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        max_idx = arr[i:].index(max(arr[i:])) + i
        if max_idx != i:
            arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            arr[:i + 1] = arr[:i + 1][::-1]
    return arr
```


## 10. meta-llama/llama-3.1-8b-instruct / pseudocode / Mbpp/422 / cycle 6

Category: generation_error. Confidence: high.

Observation: The description retains find_Average_Of_Cube; regenerated code defines find_average_of_cube and rewrites its example to use the new name.

Interpretation: The function interface drifts during generation. Keeping the original assertion in the prompt does not enforce compliance.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
```


Last passing code:
```python
def find_Average_Of_Cube(n):
    sum_of_cubes = 0
    for i in range(1, n + 1):
        sum_of_cubes += i ** 3
    average_of_cubes = sum_of_cubes / n
    return average_of_cubes
```


Description fed into failure:
```text
"""
FUNCTION find_Average_Of_Cube(n)
    INPUTS: n (number)
    OUTPUT: average_of_cubes (number)

    sum_of_cubes = 0

    FOR i FROM 1 TO n (inclusive)
        sum_of_cubes = sum_of_cubes + i ** 3
    END FOR

    average_of_cubes = sum_of_cubes / n

    RETURN average_of_cubes
END FUNCTION
assert find_Average_Of_Cube(2) == 4.5
"""
```


Failing code:
```python
def find_average_of_cube(n):
    sum_of_cubes = 0
    for i in range(1, n + 1):
        sum_of_cubes += i ** 3
    average_of_cubes = sum_of_cubes / n
    return average_of_cubes

assert find_average_of_cube(2) == 4.5
```


## 11. meta-llama/llama-3.1-8b-instruct / standard / Mbpp/71 / cycle 6

Category: representation_drift. Confidence: high.

Observation: The description introduces Quick Sort as a new request; regenerated code defines quick_sort instead of comb_sort.

Interpretation: A summary can become a new instruction and cause an interface failure.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
```


Last passing code:
```python
def comb_sort(arr):
    def get_next_gap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True

    return arr
```


Description fed into failure:
```text
"""
Here is a one-sentence summary of the code and the start of a new function:

`The provided code implements the Comb Sort algorithm, a comparison-based sorting algorithm that improves upon Bubble Sort by using a different gap size strategy to reduce the number of comparisons and swaps required to sort an array.`
 
`write a python function to implement the Quick Sort algorithm, which recursively partitions the input array around a pivot element and sorts the sub-arrays on either side of the pivot.`
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
```


Failing code:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```


## 12. meta-llama/llama-3.1-8b-instruct / standard / Mbpp/61 / cycle 4

Category: representation_drift. Confidence: high.

Observation: The description drops the comparison with substring length; the next code compares digit sum with int(substring).

Interpretation: The requirement changes before regeneration.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
```


Last passing code:
```python
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```


Description fed into failure:
```text
"""
write a python function to count the number of substrings in a given string that are equal to the sum of their digits.
assert count_Substrings('112112') == 6
"""
```


Failing code:
```python
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring.isdigit() and sum(int(digit) for digit in substring) == int(substring):
                count += 1
    return count
```


## 13. meta-llama/llama-3.1-8b-instruct / standard / Mbpp/111 / cycle 10

Category: generation_error. Confidence: high.

Observation: The description still asks for common elements; the next implementation intersects a union of all items with that same union.

Interpretation: The implementation returns all distinct items rather than their intersection across lists.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
```


Last passing code:
```python
def common_in_nested_lists(nested_lists):
    return set.intersection(*[set(sublist) for sublist in nested_lists])
```


Description fed into failure:
```text
"""
write a python function to find the common elements in a list of nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
```


Failing code:
```python
def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    return list(set([item for sublist in nested_lists for item in sublist]) & set(flat_list))
```


## 14. meta-llama/llama-3.1-8b-instruct / standard / Mbpp/141 / cycle 4

Category: representation_drift. Confidence: high.

Observation: The description changes ascending sorting into descending sorting; regenerated code also changes the flip logic.

Interpretation: Task meaning has already changed before the failing generation; code-level defects may also contribute.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
```


Last passing code:
```python
def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index == size - 1:
            continue
        if max_index != 0:
            arr[:max_index + 1] = arr[:max_index + 1][::-1]
        arr[:size] = arr[:size][::-1]
    return arr
```


Description fed into failure:
```text
"""
write a python function to sort an array of integers in descending order using the pancake sort algorithm.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
```


Failing code:
```python
def pancake_sort(arr):
    n = len(arr)
    while n > 1:
        max_idx = arr.index(max(arr[:n]))
        if max_idx == n - 1:
            n -= 1
            continue
        if max_idx != 0:
            arr = arr[:max_idx + 1][::-1] + arr[max_idx + 1:]
        arr = arr[:n - max_idx + 1][::-1] + arr[n - max_idx + 1:]
    return arr
```


## 15. meta-llama/llama-3.1-8b-instruct / standard / Mbpp/57 / cycle 4

Category: syntax_error. Confidence: high.

Observation: The regenerated return expression is missing a closing parenthesis.

Interpretation: The same syntax defect also occurs in the pseudocode configuration for this task.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
```


Last passing code:
```python
def find_Max_Num(nums):
    nums.sort(reverse=True)
    max_num = ''
    for num in nums:
        max_num += str(num)
    return int(max_num)
```


Description fed into failure:
```text
"""
Write a Python function to find the maximum number that can be formed by concatenating all numbers in a given list in descending order.
assert find_Max_Num([1,2,3]) == 321
"""
```


Failing code:
```python
def find_Max_Num(nums):
    return int(''.join(map(str, sorted(nums, reverse=True)))
```


## 16. qwen/qwen3.7-flash / standard / Mbpp/11 / cycle 7

Category: generation_error. Confidence: high.

Observation: The description retains removal of first and last occurrences; regenerated code removes twice even when only one occurrence exists. Base passes; plus fails.

Interpretation: The original requirement is retained, but the regenerated boundary-case handling is wrong.

Base passed: True; plus passed: False.


Original task:
```text
"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
```


Last passing code:
```python
def remove_Occ(s, char):
    first = s.find(char)
    last = s.rfind(char)
    
    if first == -1:
        return s
    
    result = s[:first] + s[first+1:last] + s[last+1:]
    return result
```


Description fed into failure:
```text
"""
write a python function to remove the first and last occurrences of a specified character from a given string.
assert remove_Occ("hello","l") == "heo"
"""
```


Failing code:
```python
def remove_Occ(s, char):
    first_index = s.find(char)
    last_index = s.rfind(char)
    
    if first_index == -1:
        return s
    
    # Remove the first occurrence
    s = s[:first_index] + s[first_index+1:]
    
    # Adjust last_index because we removed one character before it
    if last_index > first_index:
        last_index -= 1
    
    # Remove the last occurrence (which is now at adjusted last_index)
    s = s[:last_index] + s[last_index+1:]
    
    return s
```


## 17. qwen/qwen3.7-flash / standard / Mbpp/58 / cycle 2

Category: representation_drift. Confidence: high.

Observation: The description changes sign comparison into boolean negation; code uses not a and not b.

Interpretation: The description substitutes truthiness for sign and the next code follows the wrong operation.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
```


Last passing code:
```python
def opposite_Signs(a, b):
    return (a < 0) != (b < 0)
```


Description fed into failure:
```text
"""
write a python function to determine if two numbers have opposite signs by comparing their boolean negation results.
assert opposite_Signs(1,-2) == True
"""
```


Failing code:
```python
def opposite_Signs(a, b):
    return (not a) != (not b) and a * b < 0
```


## 18. qwen/qwen3.7-flash / standard / Mbpp/170 / cycle 4

Category: representation_drift. Confidence: high.

Observation: The description omits that the range is defined by indices; regenerated code filters values between start and end.

Interpretation: Removing the index interpretation changes the task from a slice sum into value filtering.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
```


Last passing code:
```python
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])
```


Description fed into failure:
```text
"""
write a python function to calculate the sum of elements in a list within a specified inclusive range.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""
```


Failing code:
```python
def sum_range_list(lst, start, end):
    return sum(x for x in lst if start <= x <= end)
```


## 19. qwen/qwen3.7-flash / standard / Mbpp/583 / cycle 6

Category: generation_error. Confidence: high.

Observation: The description retains nth Catalan number; regenerated code assigns catalan[1] even when n is zero. Base passes; plus fails.

Interpretation: A faithful task description can still produce a boundary-case implementation failure.

Base passed: True; plus passed: False.


Original task:
```text
"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
```


Last passing code:
```python
def catalan_number(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Create a table to store results of subproblems
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: C(0) = 1
    
    for i in range(1, n + 1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    
    return dp[n]
```


Description fed into failure:
```text
"""
write a python function to calculate the nth Catalan number using dynamic programming.
assert catalan_number(10)==16796
"""
```


Failing code:
```python
def catalan_number(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Create a table to store results of subproblems
    catalan = [0] * (n + 1)
    catalan[0] = 1
    catalan[1] = 1
    
    # Calculate values using dynamic programming
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    
    return catalan[n]
```


## 20. qwen/qwen3.7-flash / standard / Mbpp/763 / cycle 9

Category: representation_drift. Confidence: high.

Observation: Passing code sorts its input; the description instead refers to an already sorted array, and the next code omits sorting.

Interpretation: An implementation step is transformed into an assumed precondition.

Base passed: False; plus passed: False.


Original task:
```text
"""
Write a python function to find the minimum difference between any two elements in a given array. 
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
```


Last passing code:
```python
def find_min_diff(arr, n):
    # Sort the array first
    sorted_arr = sorted(arr)
    
    # Initialize minimum difference to infinity
    min_diff = float('inf')
    
    # Find the minimum difference between adjacent elements
    for i in range(n - 1):
        diff = sorted_arr[i + 1] - sorted_arr[i]
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
```


Description fed into failure:
```text
"""
write a python function to find the minimum difference between adjacent elements in a sorted array.
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
```


Failing code:
```python
def find_min_diff(arr, n):
    min_diff = float('inf')
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
```


## 21. qwen/qwen3.7-flash / pseudocode / Mbpp/7 / cycle 1

Category: initial_coverage_gap. Confidence: limited.

Observation: The initial code uses whitespace splitting and a length >= 4 filter. Base tests pass and plus tests fail.

Interpretation: This is not loop-induced drift. The saved records do not identify the failing extended input, so the exact cause remains unresolved.

Base passed: True; plus passed: False.


Original task:
```text
"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
```

No earlier cycle: this is an initial coding failure.


Failing code:
```python
def find_char_long(text):
    return [word for word in text.split() if len(word) >= 4]
```


## 22. qwen/qwen3.7-flash / pseudocode / Mbpp/99 / cycle 1

Category: initial_coverage_gap. Confidence: limited.

Observation: The initial code returns bin(n)[2:]. Base tests pass and plus tests fail.

Interpretation: This is not loop-induced drift. Negative-input handling is a candidate issue, but the exact failing input is not saved.

Base passed: True; plus passed: False.


Original task:
```text
"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
```

No earlier cycle: this is an initial coding failure.


Failing code:
```python
def decimal_to_binary(n):
    return bin(n)[2:]
```
