def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # makes a frequency counter
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) +1
    
    # finds the highest value from the counts values
    max_val = max(counts.values())
    
    # find the index of the highest value
    for (num, freq) in counts.items():
        if freq == max.value:
            return num