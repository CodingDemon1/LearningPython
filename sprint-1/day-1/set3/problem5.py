def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))