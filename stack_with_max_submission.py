#python3
import sys

class StackWithMax():
    
    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        
        if self.max_stack:
            current_max = self.max_stack[-1]
            if a >= current_max:
                self.max_stack.append(a)
        else:
            self.max_stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        
        current_max = self.max_stack[-1]
        b = self.__stack[-1]
        
        if current_max == b:
            self.max_stack.pop()
        self.__stack.pop()
            
    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1]
    
def run_stack_with_max(num_queries, queries):
    stack = StackWithMax()
    
    for i in range(num_queries):
        query = queries[i].split()
        
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
            
if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
