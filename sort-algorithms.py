def insertion_sort(arr):
  sorted_arr = []
  for el in arr:
    added = False
    for i in range(len(sorted_arr)):
      if sorted_arr[i] > el and not added:
        added = True
        sorted_arr.insert(i, el)

    if not added:
      sorted_arr.append(el)

  return sorted_arr

def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for i2 in range(len(arr) - i - 1):
      if arr[i2] > arr[i2 + 1]:
        arr[i2], arr[i2 + 1] = arr[i2 + 1], arr[i2]

  return arr

def selection_sort(arr):
  for i in range(len(arr)):
    min_value = float('inf')
    min_idx = -1
    for i2 in range(i, len(arr)):
      if arr[i2] < min_value:
        min_value = arr[i2]
        min_idx = i2
    arr[i], arr[min_idx] = arr[min_idx], arr[i]  

  return arr

###################
#   Merge Sort    #
###################

def merge(left, right):
  res = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      res.append(left[0])
      left = left[1:]
    else:
      res.append(right[0])
      right = right[1:]
  if len(left) > 0:
    res = res + left
  if len(right) > 0:
    res = res + right
  
  return res

def merge_sort(arr):
  if len(arr) <= 1:
    return arr 

  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  if left[-1] <= right[0]:
    return left + right
  else:
    return merge(left, right)

###################
#   Quick Sort    #
###################

def partition (arr, low, high):
  pivot = arr[high]
  min_idx = low - 1

  for i in range(low, high):
    if (arr[i] < pivot):
      min_idx += 1
      arr[i], arr[min_idx] = arr[min_idx], arr[i]

  arr[min_idx+1], arr[high] = arr[high], arr[min_idx+1]
  return min_idx + 1


def quick_sort_rec(arr, low, high):
  if low < high:
    partition_point = partition(arr, low, high)

    quick_sort_rec(arr, low, partition_point - 1)
    quick_sort_rec(arr, partition_point + 1, high)

def quick_sort(arr):
  quick_sort_rec(arr, 0, len(arr) - 1)
  return arr

###################
#   Heap Sort    #
###################

class MinHeap:
  def __init__(self):
    # We'll start the root at index 1
    self.list = [0]
    self.size = 0

  def move_up(self, i):
    # Notice that i // 2 is the parent of the element
    while i // 2:
      if self.list[i] < self.list[i // 2]:
        self.list[i], self.list[i // 2] = self.list[i // 2], self.list[i]
      i = i // 2

  def move_down(self, i):
    # notice that i * 2 is the left child
    while (i * 2) < len(self.list):
      min_idx = i * 2
      if (i * 2 + 1 < len(self.list) and self.list[i * 2 + 1] < self.list[min_idx]):
        min_idx = i * 2 + 1

      if (self.list[i] > self.list[min_idx]):
        self.list[i], self.list[min_idx] = self.list[min_idx], self.list[i]

      i = min_idx

  def insert(self, val):
    self.list.append(val)
    self.move_up(len(self.list) - 1)
    self.size += 1

  def pop(self):
    if self.size == 0:
      return None

    top = self.list[1]
    self.list[1] = self.list[-1]
    self.list.pop()
    self.size -= 1
    if self.size > 1:
      self.move_down(1)

    return top
  
def heap_sort(arr):
  heap = MinHeap()
  for el in arr:
    heap.insert(el)

  res = []
  val = heap.pop()
  while val is not None:
    res.append(val)
    val = heap.pop()
  return res


import random 

my_arr = [random.randint(0,100) for x in range(40)]

print("Before sort:    ", my_arr)
print("Insertion sort: ", insertion_sort(my_arr[:]))
print("Bubble sort:    ", bubble_sort(my_arr[:]))
print("Selection sort: ", selection_sort(my_arr[:]))
print("Merge sort:     ", merge_sort(my_arr[:]))
print("Quick sort:     ", quick_sort(my_arr[:]))
print("Heap sort:      ", heap_sort(my_arr[:]))
