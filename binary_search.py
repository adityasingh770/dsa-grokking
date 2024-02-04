def binary_search(list, item):
    """
    Perform binary search on a sorted list to find the index of the specified item.

    Parameters:
    - lst (list): The sorted list to search within.
    - item: The item to search for in the list.

    Returns:
    - int or None: If the item is found, returns the index of the item in the list.
                  If the item is not present, returns None.

    Algorithm:
    - Initialize left and right pointers at the extremes of the list.
    - While left pointer is less than or equal to the right pointer:
        - Calculate the mid index.
        - Check the value at the mid index:
            - If it matches the target item, return the mid index.
            - If it's greater, update the right pointer to mid - 1.
            - If it's smaller, update the left pointer to mid + 1.

    Time Complexity: O(log n) - where n is the length of the input list.
    Space Complexity: O(1) - constant space is used.

    Note:
    - The input list must be sorted for the binary search to work correctly.
    """
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            right = mid - 1
        else:
            left = mid + 1
