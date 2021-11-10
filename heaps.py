### Priority Queues ###
'''
class PriorityQueue:
    
    def __init__(self):
        self.A = []

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        else:
            return self.A.pop()                                         # NOT correct on its own!

    @classmethod
    def sort(Queue, A):
        pq = Queue()                                                    # make empty priority queue
        for x in A:                                                     # n x T_insert
            pq.insert(x)
        out = [pq.delete_max() for _ in A]                              # n x T_delete_max
        out.reverse()
        return out
'''

### Binary Heaps ###
class PQ_Heap(PriorityQueue):
    def insert(self, *args):                        # O(log n)
        super().insert(*args)                        # append to end of array
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    def delete_max(self):                           # O(log n)
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max()                 # pop from end of array


# A = [7, 3, 5, 6, 2, 0, 3, 1, 9, 4]
