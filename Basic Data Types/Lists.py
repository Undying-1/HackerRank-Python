class List():
    def __init__(self) -> None:
        self.arr = []
    
    def operation(self, type, index=0, number=0):
        getattr(self, type)(index, number)

    def insert(self,index, number):
        self.arr.insert(index, number)
    
    def append(self, index=0, number=0):
        self.arr.append(number)
        
    def pop(self,index=0, number=0):
        self.arr.pop()
        
    def sort(self, index=0, number=0):
        self.arr.sort()
        
    def reverse(self, index=0, number=0):
        self.arr.reverse()
        
    def remove(self, index=0, number=0):
        self.arr.remove(number)
        
    def print(self, index=0, number=0):
        print(self.arr)


if __name__ == '__main__':
    N = int(input())
    list_class = List()
    results = []
    for i in range(N):
        data = input().split()
        if len(data) == 3:
            list_class.operation(data[0], int(data[1]), int(data[2]))
        elif len(data) == 2:
            list_class.operation(data[0], 0, int(data[1]))
        else:
            results.append(list_class.operation(data[0]))
