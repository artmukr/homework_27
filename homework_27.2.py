def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]
        merge_sort(left)
        merge_sort(right)
        current_left = 0
        current_right = 0
        current_index = 0

        while current_left < len(left) and current_right < len(right):
            if left[current_left] < right[current_right]:
                input_list[current_index] = left[current_left]
                current_left += 1
            else:
                input_list[current_index] = right[current_right]
                current_right += 1
            current_index += 1

        while current_left < len(left):
            input_list[current_index] = left[current_left]
            current_left += 1
            current_index += 1

        while current_right < len(right):
            input_list[current_index] = right[current_right]
            current_right += 1
            current_index += 1
    return input_list


nums = [44, 68, 2, 4, 98, 67, 35, 5]
print(merge_sort(nums))
