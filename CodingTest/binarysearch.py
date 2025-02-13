#Search for an element in a sorted array.
#Implement a binary search algorithm in Python.
def binarysearch(arr,e):
    low =0
    hight = len(arr)-1

    while low<=hight:
        mid = (low + hight) // 2
        if arr[mid]== e:
            return mid
        elif arr[mid]<e:
            low = mid+1
        else:
            high= mid-1
    return -1

print(binarysearch([4,5,6,7,8,9],8))