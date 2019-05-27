# Exercise 1: Create an algorithm that determines if a passed string has all unique characters.


def is_unique(str_arg: str):
    str_dict = {}
    for c in str_arg:
        if c in str_dict:
            return False
        else:
            str_dict[c] = True;
    return True

# Big O: O(N) time and O(N) space

print(is_unique('abnc'))

# But now can you do it without an additional data structure?


def is_unique_two(str_arg:str):
    str_length = len(str_arg)
    for i in range(str_length):
        for j in range(i+1, str_length):
            if str_arg[i] == str_arg[j]:
                return False
    return True

# Big O: O(N^2) time and O(1) space

print(is_unique_two('abcdefg'))


