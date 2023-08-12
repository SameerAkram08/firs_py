def find_largest_zero_sum_subarray(arr):
    sum_indices = {}
    current_sum = 0
    max_length = 0
    end_index = -1
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if arr[i] == 0 and max_length == 0:
            max_length = 1
            end_index = i
        
        if current_sum == 0:
            max_length = i + 1
            end_index = i
        
        if current_sum in sum_indices:
            if max_length < i - sum_indices[current_sum]:
                max_length = i - sum_indices[current_sum]
                end_index = i
        else:
            sum_indices[current_sum] = i
    
    start_index = end_index - max_length + 1
    return start_index, end_index

arr = [15, -2, 2, -8, 1, 7, 10, 23]
subarray_indices = find_largest_zero_sum_subarray(arr)
print(f"Largest subarray with zero sum starts at index: {subarray_indices[0]} and ends at index: {subarray_indices[1]}")
