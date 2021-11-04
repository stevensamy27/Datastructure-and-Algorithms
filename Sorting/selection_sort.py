def selection_sort(A):                       # Selection sort array A
    for i in range(len(A) - 1):              # O(n) loop over array
        m = i                                # O(1) initial index of max
        for j in range(i+1, len(A)-1):       # O(i) search for max in A[:i]
            if A[j] < A[m]:                  # O(1) check for larger value
                m = j                        # O(1) new max found
        A[m], A[i] = A[i], A[m]              # O(1) swap

#E.X
A = [3,2,1,4]
print(A)
selection_sort(A)
print(A)

# OUTPUT
'''
[3, 2, 1, 4]
[1, 2, 3, 4]

'''