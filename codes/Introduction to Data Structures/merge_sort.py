def merge_sort(list):
  """
  Sorts a list in ascending order.
  Returns a new sorted list.

  Divide: Find the midpoint of the list and divide into sublists.
  Conquer: Recursively sort the sublists created in previous step.
  Combine: Merge the sorted sublists created in previous step.

  Takes, overall O(k * n * Log n) time.

  Takes, overall O(n) space.
  """

  if(len(list) <= 1):
    return list

  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(list):
  """
  Divide the unsorted list at midpoint into sublists.
  Returns two sublists - left and right.

  Takes, overall O(Log n) time.

  If you take a look at python documentation, 
  you will see that slicing is not constant time operation, 
  but takes O(k) time where k is the slice size.  

  That means split takes, O(k * Log n) time.
  """

  mid = (len(list)) // 2
  left = list[:mid]
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Merges two lists (arrays), sorting them in the process.
  Returns a new merged list. 

  Takes, overall O(n) time.
  """

  list = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if(left[i] < right[j]):
      list.append(left[i])
      i += 1
    else:
      list.append(right[j])
      j += 1

  while i < len(left):
    list.append(left[i])
    i += 1
  
  while j < len(right):
    list.append(right[j])
    j += 1

  return list

def verify_sorted(list):
  """
  It is recursive verification of sorted list.
  It can be done with Iterative appraoch or for loop.
  """
  n = len(list)

  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])

alist = [99, 55, 77, 22, 10, 8, 33, 27, 87, 11]
sorted_list = merge_sort(alist)

print("Unsorted List: ")
print(alist)
print("Sorted List: ")
print(sorted_list)

print(verify_sorted(alist))
print(verify_sorted(sorted_list))