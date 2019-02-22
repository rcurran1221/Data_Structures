# python3

class HeapBuilder:
    
  def __init__(self, n, input_data):
    self._data = input_data
    self._size = n
    assert len(input_data) == n
    self._swaps = []
          
  def BuildMinHeap(self):
      for i in range(self._size // 2, -1, -1):
          self.SiftDown(i)
  
  def SiftDown(self, i):
      max_index = i
      
      left_child = LeftChild(i)
      if left_child < self._size and self._data[left_child] < self._data[max_index]:
          max_index = left_child
          
      right_child = RightChild(i)
      if right_child < self._size and self._data[right_child] < self._data[max_index]:
          max_index = right_child
          
      if i != max_index:
          self._swaps.append((i, max_index))
          self._data[max_index], self._data[i] = self._data[i], self._data[max_index]
          self.SiftDown(max_index)
      
  def IsMinHeap(self):
      if not self._data:
          print("Data not initialized")
          return
      
      for i in range(len(self._data)):
          if LeftChild(i) < self._size:
              if self._data[i] > self._data[LeftChild(i)]:
                  print("Is not Min Heap")
                  return
          if RightChild(i) < self._size:
              if self._data[i] > self._data[RightChild(i)]:
                  print("Is not Min Heap")
                  return
      print("Is Min Heap")
      return
    
def Parent(i):
    if i == 0:
        return None
      
    return int(i - 1 // 2)
  
def LeftChild(i):
    if i == 0:
        return 1
      
    return int(2*i + 1)
      
def RightChild(i):
    if i == 0:
        return 2
      
    return int(2*i + 2)

if __name__ == '__main__':
    input_data_one = [5, 4, 3, 2, 1]
    heap_builder_one = HeapBuilder(5, input_data_one)
    heap_builder_one.BuildMinHeap()
    heap_builder_one.IsMinHeap()
    
    input_data_two = [1, 2, 3, 4, 5]
    heap_builder_two = HeapBuilder(5, input_data_two)
    heap_builder_two.BuildMinHeap()
    heap_builder_two.IsMinHeap()
    
    input_data_three = [1, 4, 8, 11, 3]
    heap_builder_three = HeapBuilder(5, input_data_three)
    heap_builder_three.BuildMinHeap()
    heap_builder_three.IsMinHeap()
    
    input_data_four = [25, 20, 21, 22, 14, 23, 24, 26, 27, 28, 1, 2, 3, 30, 6]
    heap_builder_four = HeapBuilder(15, input_data_four)
    heap_builder_four.BuildMinHeap()
    heap_builder_four.IsMinHeap()
