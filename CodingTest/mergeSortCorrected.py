def merge_sort(lst):
    if len(lst) <= 1:
        return lst  # Base case: single element or empty list is already sorted
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])  # Sort left half
    right = merge_sort(lst[middle:])  # Sort right half
    return merge(left, right)
def merge(left, right):
    result = []
    i, j = 0, 0  # Pointers for left and right lists

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Test the function
print(merge_sort([9, 2, 4, 1, 9, 6, 3]))
