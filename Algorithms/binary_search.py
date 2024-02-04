def binary_search(arr, target):
    left = 0  # start index of array
    right = len(arr) - 1  # End index of the array

    # the loop will run until left and right index are same when element is not found
    while left <= right:

        # check if target is in the mid-index
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        # if target element is larger than mid-element, simply ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # In this case, target will be smaller than mid-element, simply ignore the right half
        else:
            right = mid - 1

    # if we reach here then target in not in the array
    return -1


if __name__ == '__main__':

    # test array, you can change according to your preferences.
    array = [1, 2, 4, 5, 7, 8, 9, 33, 55, 66, 77, 88, 99, 123, 345, 677, 888]
    target_element = 55

    target_index = binary_search(array, target_element)

    if target_index == -1:
        print("Element is not in the array")
    else:
        print(f"The index of the target element = {target_index}")
