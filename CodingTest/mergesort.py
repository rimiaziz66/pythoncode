
# bad one because of pop(0) operation
def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  middle = len(lst) // 2
  left = lst[:middle]
  right = lst[middle:]
  sleft = merge_sort(left)
  sright = merge_sort(right)
  return merge(sleft, sright)

def merge(left, right):

  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

print(merge_sort([9,2,4,1,9,6,3]))