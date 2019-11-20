def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        key = input_list[index]
        prev_index = index-1
        while prev_index >= 0 and key < input_list[prev_index]:
            input_list[prev_index + 1] = input_list[prev_index]
            prev_index -= 1
        input_list[prev_index + 1] = key
    return input_list


nums = [44, 19, 78, 656, 2, 45, 67]
print(insertion_sort(nums))
