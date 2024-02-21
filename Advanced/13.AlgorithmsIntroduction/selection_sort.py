def selection_sort(nums):
    for idx in range(len(nums)):
        min_index = idx

        for next_idx in range(idx + 1, len(nums)):
            if nums[next_idx] < nums[min_index]:
                min_index = next_idx

        nums[idx], nums[min_index] = nums[min_index], nums[idx]

nums = [int(x) for x in input().split()]
selection_sort(nums)

print(*nums)
