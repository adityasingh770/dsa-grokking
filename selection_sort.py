def find_smallest(arr):
    """
    Finds the index of the smallest element in the given array.

    Parameters:
    - arr (List): The input list containing comparable elements.

    Returns:
    - int: The index of the smallest element in the array.

    This function iterates through the elements of the array to identify the smallest one.
    It returns the index of that smallest element, allowing for easy retrieval or further manipulation.
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    Performs selection sort on the given array, sorting it in ascending order.

    Parameters:
    - arr (List): The input list to be sorted.

    Returns:
    - List: A new list containing the elements of the input list in ascending order.

    This function applies the selection sort algorithm to sort the elements of the input array.
    It creates a new array with sorted elements and returns it, leaving the original array unchanged.

    Notes:
    - The function iteratively finds the smallest element using find_smallest function
      and appends it to a new array until the original array is empty.
    - Time complexity: O(n^2) as it needs to find the smallest element for each iteration.
    - Space complexity: O(n) due to the creation of a new array.
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
