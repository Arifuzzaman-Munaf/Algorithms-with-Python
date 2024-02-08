"""the array has a size of N and we're given an integer K and we want to find maximum K consecutive elements"""


def max_sum(array, window_size):
    if len(array) < window_size:
        return -1

    window_sum = sum(array[:window_size])
    maxSum = window_sum

    for i in range(len(array) - window_size):
        window_sum = window_sum - array[i] + array[i + window_size]
        maxSum = max(window_sum, maxSum)

    return maxSum


if __name__ == '__main__':
    array_of_numbers = [10, 34, -10, 33, -89, 111, 43, -23]
    window_size = 3
    print(f"Maximum sum for three consecutive numbers = {max_sum(array_of_numbers, window_size)}")
