
def partition(input_list, low, high):
    smaller_index = (low - 1)
    pivot = input_list[high]
    for current_index in range(low, high):
        if input_list[current_index] < pivot:
            smaller_index += 1
            input_list[smaller_index], input_list[current_index] = \
                input_list[current_index], input_list[smaller_index]
    input_list[smaller_index + 1], input_list[high] = \
        input_list[high], input_list[smaller_index + 1]
    return smaller_index + 1


def quick_sort(input_list, low, high):
    if low < high:
        pivot = partition(input_list, low, high)
        quick_sort(input_list, low, pivot - 1)
        quick_sort(input_list, pivot + 1, high)
    return input_list


nums = [27, 4, 45, 15, 8, 99, 458, 2]
n = len(nums)
print(quick_sort(nums, 0, n - 1))
