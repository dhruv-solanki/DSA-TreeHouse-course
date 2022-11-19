from linked_list import LinkedList

def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  - Recursively divide the linked list into sublists containing a single Node.
  - Repeatedly merge the sublists to produce sorted sublists until one remains.

  Returns a sorted linked list.

  Takes, O(n * k * Log n) time
  """

  if(linked_list.size() == 1 or linked_list.head is None):
    return linked_list

  left_half, right_half = split(linked_list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(linked_list):
  """
  Divide the unsorted linked list at midpoint into sublists.

  Takes, O(k * Log n) time
  """

  if(linked_list == None or linked_list.head == None):
    left_half = linked_list
    right_half = None

    return left_half, right_half
  else:
    size = linked_list.size()
    mid = size // 2

    mid_node = linked_list.node_at_index(mid-1)

    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None

    return left_half, right_half

def merge(left, right):
  """
  Merges two linked lists, sorting by data in Nodes.
  Returns a new, merged list.

  Takes, O(n) time
  """

  # Create a new linked list that contains Nodes from
  # merging left and right
  merged = LinkedList()

  # Add a fake head that will be discarded later
  merged.add(0)

  # Set current to the head of the linked list
  current = merged.head

  # Obtain head nodes of left and right  linked lists
  left_head = left.head
  right_head = right.head

  # Iterate over left and right until we reach tail Node of either
  while left_head or right_head:
    # If the head Node of left is None, we're past the tail Node of left
    # Add the Node from right to merged linked list
    if(left_head is None):
      current.next_node = right_head
      # Call next on right to set loop condition to False
      right_head = right_head.next_node

    # If the head Node if right is None, we're past the tail Node if right
    # Add the Node from left to merged linked list
    elif(right_head is None):
      current.next_node = left_head
      # Call next on left to set loop condition to False
      left_head = left_head.next_node
    else:
      # Not at either tail Node
      # Obtain Node data to perform the comparison operations
      left_data = left_head.data
      right_data = right_head.data
      # If data on left is less than right, set current to left Node
      if(left_data < right_data):
        current.next_node = left_head
        # Move left head to the next Node
        left_head = left_head.next_node
      # If data on left is greater than right, set current to right Node
      else:
        current.next_node = right_head
        # Move right head to the next Node
        right_head = right_head.next_node
    
    # Move current to next Node
    current = current.next_node
  
  # Discard fake head and set first merged Node as head
  head = merged.head.next_node
  merged.head = head

  return merged

linked_list = LinkedList()
linked_list.add(11)
linked_list.add(99)
linked_list.add(23)
linked_list.add(8)
linked_list.add(65)

print(linked_list)

sorted_linked_list = merge_sort(linked_list)
print(sorted_linked_list)