def quick_sort(arr):
    """
    Sorts a list of comparable elements using the quicksort algorithm.

    Parameters:
    - arr (list): The list of elements to be sorted.

    Returns:
    list: A new list containing the sorted elements.

    Notes:
    - The function uses the middle element as the pivot for partitioning.
    - Elements equal to the pivot are placed in the middle to handle duplicates.
    - Recursively sorts the left and right partitions until the entire list is sorted.
    - Time complexity: O(n log n) on average, O(n^2) in the worst case.
    - Space complexity: O(log n) due to the recursive nature of the algorithm.
    """
    if len(arr) < 2:
        return arr

    # Choose the middle element as the pivot
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left_side = [x for x in arr if x <= pivot]
    right_side = [x for x in arr if x > pivot]
    return quick_sort(left_side) + pivot + quick_sort(right_side)
