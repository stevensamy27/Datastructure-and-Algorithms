def insertion_sort(A):                                        # Insertion sort array A
    for i in range(1, len(A)):                                # O(n) loop over array
        j = i                                                 # O(1) initialize pointer
        while j > 0 and A[j] < A[j - 1]:                      # O(i) loop over prefix
            A[j - 1], A[j] = A[j], A[j - 1]                   # O(1) swap
            j = j - 1                                         # O(1) decrement j


# E.X
A = [3,4,2,1,5]
insertion_sort(A)
print("sorted array: " + str(A))

# OUTPUT
'''
sorted array: [1, 2, 3, 4, 5]

'''