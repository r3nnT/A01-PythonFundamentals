# Name: Tyler Renn
# OSU Email: rennt@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A01
# Due Date: 04/24/23 @ 11:59 PM
# Description: 10 different Python functions that asses programming skills
#              and different procedures needed to succeed in the class.

import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Find the minimum and maximum value in an array
    """
    # Initialize min and max to first value in the array
    min = max = arr[0]

    # Compare values in array to determine min and max
    for i in range(1, arr.length()):
        if arr.get(i) < min:
            min = arr.get(i)
        elif arr.get(i) > max:
            max = arr.get(i)

    # Return the min and max values of the array
    return (min,max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray of int's and returns a new object with
    content modified by divisibility factors
    """

    # Form a new array object with the length of the original
    new_arr = StaticArray(arr.length())

    # Populate a new StaticArray object with contents of the original array
    for i in range(arr.length()):
        new_arr.set(i, arr.get(i))

    # Modify new_arr object with these divisibility factors
    for i in range(arr.length()):
        if abs(new_arr.get(i)) % 3 == 0 and abs(new_arr.get(i)) % 5 == 0:
            new_arr.set(i, "fizzbuzz")
        elif abs(new_arr.get(i)) % 5 == 0:
            new_arr.set(i, "buzz")
        elif abs(new_arr.get(i)) % 3 == 0:
            new_arr.set(i, "fizz")

    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverses the given array in place
    """

    # Split the array in half
    for i in range(arr.length()//2):

        # Swap elements of the first half of the array with the second half
        arr[i], arr[arr.length()-i-1] = arr[arr.length()-i-1], arr[i]

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotates an array based on the number steps
    if steps is positive, array rotates to the right
    if steps is negative, array rotates to the left
    """

    # Variables used to determine length, the new array and steps
    length = arr.length()
    new_arr = StaticArray(length)
    steps = steps % length

    # For loop to rotate the array
    for i in range(length):
        if steps >= 0:
            temp = (i + steps) % length
        else:
            temp = (i + steps + length) % length
        new_arr[temp] = arr[i]

    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Receives 2 integers and returns an array that contains all the
    consecutive integers (inclusive)
    """

    # Determine the length of the StaticArray and make one

    length = abs(end - start) + 1
    arr = StaticArray(length)

    # Populate the array with the consecutive integers
    for i in range(length):

        if end > start:
            arr[i] = start + i

        else:
            arr[i] = start - i

    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Returns an integer that describes whether the array
    is sorted
    """

    # Set variables for length and order
    length = arr.length()
    order = 0

    # Return 1 if the length of the array is 1
    if length <= 1:
        return 1

    # Check to see if the array is sorted in a certain order
    for i in range(1,length):
        if arr[i] > arr[i-1]:
            if order == -1:
                return 0
            order = 1
        elif arr[i] < arr[i-1]:
            if order == 1:
                return 0
            order = -1
        elif arr[i] == arr[i-1]:
            return 0

    return order


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    Recieves a StaticArray in sorted order. Returns the mode and how
    many times in occurd in the array
    """

    # Initialize variables
    mode = None
    max = 0
    length = arr.length()

    # Loop to determine how many times a certain index occurs
    for i in range(length):
        count = 0
        for j in range(length):
            if arr[j] == arr[i]:
                count += 1

        # Checks if the current count is bigger than the max
        if count > max:
            max = count
            mode = arr[i]

    return mode, max


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray that is already sorted. Returns a new StaticArray
    with all duplicate values removed
    """
    
    # Initialize the length and new StaticArray
    length = arr.length()
    new_arr = StaticArray(length)
    
    # Keep track of the last special value
    last_value = arr[0]

    # Add first element to the new array
    new_arr[0] = arr[0]

    # Loop through the remaining values in the array
    for i in range(length):

        # If the current element is different than the last_value
        # add it the new array and update the last_value
        if arr[i] != last_value:
            new_arr[i] = arr[i]
            last_value = arr[i]

    # Loop through to determine the amount of non-None elements
    none_count = 0
    for i in range(new_arr.length()):
        if new_arr[i] is not None:
            none_count += 1

    # New StaticArray that will hold all unique values
    final_array = StaticArray(none_count)
    j = 0

    # Add unique values to the final array
    for i in range(new_arr.length()):
        if new_arr[i] is not None:
            final_array[j] = new_arr[i]
            j += 1

    return final_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order, using the count sort algorithm
    """

    length = arr.length()
    max_val = arr[0]
    min_val = arr[0]
    for i in range(length):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    # Create the count array
    count_arr = [0] * (max_val - min_val + 1)
    for i in range(length):
        count_arr[max_val - arr[i]] += 1

    # Modify the count array to contain the ending positions of the values
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Create the sorted array
    sorted_arr = [0] * length
    for i in range(length - 1, -1, -1):
        sorted_arr[count_arr[max_val - arr[i]] - 1] = arr[i]
        count_arr[max_val - arr[i]] -= 1

    return sorted_arr


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Returns a modified string that is the same length as source.
    The ouput string must follow a certain set of rules
    """

    # Creates a dict that determines the route from s1 to s2
    directions = dict(
        zip(s1, s2))
    product = ""
    for value in source:
        if value in directions:
            product += directions[value]
        elif value.isupper():
            product += " "
        elif value.islower():
            product += "#"
        elif value.isdigit():
            product += "!"
        else:
            product += "="
    return product


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps} {abs(steps) % arr.length()}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
