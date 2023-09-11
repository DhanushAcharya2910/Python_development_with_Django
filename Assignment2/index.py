def find_first_index(arr, target):
    left, right = 0, len(arr) - 1
    first_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            first_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_index

def find_last_index(arr, target):
    left, right = 0, len(arr) - 1
    last_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            last_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_index


sorted_array = [1, 2, 2, 2, 3, 4, 4, 5, 6]
target_value = 2

first_index = find_first_index(sorted_array, target_value)
last_index = find_last_index(sorted_array, target_value)

if first_index != -1 and last_index != -1:
    print(f"The first index of {target_value} is {first_index}")
    print(f"The last index of {target_value} is {last_index}")
else:
    print(f"{target_value} not found in the array.")
