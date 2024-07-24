class PriorityQueue:
    def __init__(self, mas):
        self.mas = mas
        self.length = len(mas)
        self.HeapSize = len(mas)

    @staticmethod
    def Parent(i):
        return i//2

    @staticmethod
    def Left(i):
        return 2*i

    @staticmethod
    def Right(i):
        return 2*i+1

    def MaxHeapify(self, i):
        l = self.Left(i)
        r = self.Right(i)
        if l < self.HeapSize and self.mas[l] > self.mas[i]:
            largest = l
        else: largest = i
        if r < self.HeapSize and self.mas[r] > self.mas[largest]:
            largest = r
        if largest !=i:
            self.mas[i], self.mas[largest] = self.mas[largest], self.mas[i]
            self.MaxHeapify(largest)

    def BuildMaxHeap(self):
        for i in range((self.length-1) // 2, -1, -1):
            self.MaxHeapify(i)

    def HeapSort(self):
        self.BuildMaxHeap()
        for i in range(self.length-1, 0,-1):
            self.mas[i], self.mas[0] = self.mas[0], self.mas[i]
            self.HeapSize -=1
            self.MaxHeapify(0)

    def HeapMaximum(self):
        return self.mas[0]

    def ExtractMax(self):
        if self.HeapSize < 1:
            print("Heap is empty")
        else:
            max = self.mas[0]
            self.mas[0] = self.mas[self.HeapSize-1]
            self.HeapSize -=1
            self.MaxHeapify(0)
            return max

    def MaxHeapIncrease(self,i, key):
        if key < self.mas[i]:
            print("key < curreny value")
        else:
            self.mas[i] = key
            while i > 0 and self.mas[self.Parent(i)] < self.mas[i]
                self.mas[self.Parent(i)], self.mas[i] = self.mas[i], self.mas[self.Parent(i)]
                i = self.Parent(i)

    def MaxHeapInsert(self, key):
        self.length+=1
        self.HeapSize+=1
        self.mas[self.HeapSize-1] = - 10**10
        self.MaxHeapIncrease(self.HeapSize-1, key)
