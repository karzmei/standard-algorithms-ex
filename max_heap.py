class MaxHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def __propagate_up(self, idx):
        cur_idx = idx
        done = False
        while not done and cur_idx > 0:
            parent_idx = (cur_idx - 1) // 2
            if self.heap[cur_idx] > self.heap[parent_idx]:
                self.heap[cur_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[cur_idx]
                cur_idx = parent_idx
            else:
                done = True

    def __propagate_down(self, idx):
        cur_idx = idx
        done = False
        while not done and cur_idx < self.length:
            l_child_idx = 2 * cur_idx + 1
            r_child_idx = 2 * (cur_idx + 1)
            
            if l_child_idx >= self.length:
                done=True
            else:
                if r_child_idx < self.length and self.heap[r_child_idx] > self.heap[l_child_idx]:
                    larger_child_idx = r_child_idx
                else:
                    larger_child_idx = l_child_idx

                if self.heap[cur_idx] < self.heap[larger_child_idx]:
                    self.heap[cur_idx], self.heap[larger_child_idx] = self.heap[larger_child_idx], self.heap[cur_idx]
                    cur_idx = larger_child_idx
                else:
                    done = True

    def insert(self, value: float):
        if self.length < len(self.heap):
            self.heap[self.length] = value
        else:
            self.heap.append(value)
        self.length += 1

        self.__propagate_up(self.length - 1)

    def pop_max(self) -> float:
        max_val = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.length -= 1
        self.__propagate_down(0)
        
        return max_val

    def get_heap(self) -> list:
        return self.heap


if __name__=="__main__":
    strim = [1, 2, 3, 3, 3, 5, 6]
    k = 3

    max_heap = MaxHeap()
    for i in range(len(strim)):
        print(f"Inserting {strim[i]}")
        max_heap.insert(strim[i])
        print(f"Heap after insertion: {max_heap.get_heap()}")

    for i in range(k):
        print(f"Popping max: {max_heap.pop_max()}")
        print(f"Heap after popping: {max_heap.get_heap()}")
