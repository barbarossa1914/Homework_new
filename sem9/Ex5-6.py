class Heap(list):
    def heapify(self, n):
        try:
            while self[2*n + 1] < self[n] or self[2*n + 2] < self[n]:
                if self[2*n + 1] == min(self[2*n + 1], self[2*n + 2]):
                    self[n], self[2*n + 1] = self[2*n + 1], self[n]
                    return self.heapify(2*n + 1)
                else:
                    self[n], self[2 * n + 2] = self[2 * n + 2], self[n]
                    return self.heapify(2 * n + 2)
        except:
            try:
                if self[2*n + 1] < self[n]:
                    self[n], self[2 * n + 1] = self[2 * n + 1], self[n]
                    return self.heapify(2 * n + 1)
            except:
                return
            return


    def emerge(self, n):
        while self[(n - 1)//2] > self[n] and n > 0:
            self[(n - 1)//2], self[n] = self[n], self[(n - 1)//2]
            print(self)
            return self.emerge((n - 1)//2)
        return


    def get_min(self):
        m = self[0]
        self[0] = self[-1]
        self.pop()
        self.heapify(0)
        return m


    def norm(self):
        for i in range(0, len(self)//2 + 1):
            self.heapify(len(self)//2 - i)
        return


    def heapify1(self, n):
        try:
            while self[2*n + 1] > self[n] or self[2*n + 2] > self[n]:
                if self[2*n + 1] == max(self[2*n + 1], self[2*n + 2]):
                    self[n], self[2*n + 1] = self[2*n + 1], self[n]
                    return self.heapify1(2*n + 1)
                else:
                    self[n], self[2 * n + 2] = self[2 * n + 2], self[n]
                    return self.heapify1(2 * n + 2)
        except:
            try:
                if self[2*n + 1] > self[n]:
                    self[n], self[2 * n + 1] = self[2 * n + 1], self[n]
                    return self.heapify1(2 * n + 1)
            except:
                return
            return


    def norm1(self):
        for i in range(0, len(self)//2 + 1):
            self.heapify1(len(self)//2 - i)
        return


def heapsort(arr):
    heap = Heap(arr)
    heap.norm()
    sorted_arr = []
    while len(heap) > 0:
        sorted_arr.append(heap.get_min())
    return sorted_arr


print(heapsort([10, 9, 8, 7, 6, -4, 3, -1, 20, 1, 2, 5, 13, -5, -6]))


heap1 = Heap([10, 9, 8, 7, 6, -4, 3, -1, 20, 1, 2, 5, 13, -5, -6])
heap1.norm()
# минимальная куча #
print(heap1)
heap1.norm1()
# максимальная куча #
print(heap1)