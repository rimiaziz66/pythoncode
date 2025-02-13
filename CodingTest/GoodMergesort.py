# implement merge sort in python
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid= len(arr)//2
    left_arr= arr[:mid]
    right_arr= arr[mid:]
    #recursion
    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)
    #merge
    l=0
    r=0
    merge_arr =[]

    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l]<right_arr[r]:
            merge_arr.append(left_arr[l])
            l += 1
        else :
            merge_arr.append(right_arr[r])
            r += 1

    while l< len(left_arr):
        merge_arr.append(left_arr[l])
        l +=1

    while r< len(right_arr):
        merge_arr.append(right_arr[r])
        r +=1

    return merge_arr

print(merge_sort([3, 7, 1, 9, 23, 6, 2]))