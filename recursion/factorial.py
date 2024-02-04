def factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which the factorial is calculated.

    Returns:
    - int: The factorial of the input integer.

    This recursive function computes the factorial of a non-negative integer 'n'.
    The factorial of 'n' is the product of all positive integers less than or equal to 'n'.
    If 'n' is 0 or 1, the function returns 1 as the base case; otherwise, it recursively
    multiplies 'n' with the factorial of (n-1) until the base case is reached.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
