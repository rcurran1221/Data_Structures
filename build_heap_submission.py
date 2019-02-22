# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self._size = -1

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)
    self._size = n

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwapsNaive(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
  
  def GenerateSwaps(self):
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

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()
    
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
    heap_builder = HeapBuilder()
    heap_builder.Solve()
