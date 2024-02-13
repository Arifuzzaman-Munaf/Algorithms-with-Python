"""the array has a size of N and we're given an integer K and we want to find maximum K consecutive elements"""


# This function will return maximum sum of k consecutive elements
def max_sum(array, window_size):
    # Length of the array can not be less than window size
    if len(array) < window_size:
        return -1

    # Calculating the sum of first K elements
    window_sum = sum(array[:window_size])
    maxSum = window_sum

    """ Compute sums of remaining windows by removing first element of previous window
        Adding last element of current window."""
    for i in range(len(array) - window_size):
        window_sum = window_sum - array[i] + array[i + window_size]
        maxSum = max(window_sum, maxSum)

    return maxSum


if __name__ == '__main__':
    # maximum sum of this array should be 131
    array_of_numbers = [10, 34, -10, 33, -89, 111, 43, -23]
    window_size = 3
    print(f"Maximum sum for three consecutive numbers = {max_sum(array_of_numbers, window_size)}")
