"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""
    
    #make empty dictionary to keep count of each number
    num_count = {}

    #loop through numbers in given list of 'nums'
    for num in nums:
        #value at the number = number of times it appears 
        # (either 0 or add 1 if it exists)
        num_count[num] = num_count.get(num, 0) + 1

    #find highest count by using built in max function on values
    highest_count = max(num_count.values())

    #make set called 'mode'
    mode = set()

    #for key, value in dictionary.items():
    for num, count in num_count.items():
        if count == highest_count:
            mode.add(num)

    return mode



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
