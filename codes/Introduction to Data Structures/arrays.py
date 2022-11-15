numbers = [1, 2, 3, 4, 5, 6, 7]

# accessing arrays in two ways
if 5 in numbers: print(True)

for n in numbers:
  if(n == 7):
    print(True)

    break

# inserting element at first position
# Linear Time Complexity - O(n)
numbers.insert(0, 0)
print(numbers)

# appending element at last position
# Ammortized Constant Space Complexity - O(1) or O(k), where k is the growth of memory
numbers.append(8)
print(numbers)

# extend array with another array
# O(k), where k is number of element in the list that we are adding into the extended list
numbers.extend([11, 12, 13, 14, 15])
print(numbers)

# deleting element from the array
# Linear Time Complexity - O(n)
numbers.remove(3)
print(numbers)