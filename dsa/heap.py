"""
    WE ARE DEALING WITH INSERTION AND DELETION WRT MAX HEAP IN THIS PROGRAM

    WHAT YOU CAN TRY ON YOUR OWN
    1. HEAPIFY FUNCTION IMPLEMENTATION (MAXHEAPIFY / MINHEAPIFY)
    2. BUILD MAX/MINHEAP FUNCTION
    3. HEAPSORT

"""


def insertInPQ(arr, value):
    arr.append(value)                   # Inserting at the end
    curr = len(arr) - 1                 # Getting the index position of the currently inserted element
    if(curr == 0):
        print(arr)
        return
    parentIdx = (curr-1)//2 # Finding the index position of the parent node
    while(arr[curr] > arr[parentIdx]):
        arr[curr], arr[parentIdx] = arr[parentIdx], arr[curr] # Swap operation between the child and the parent
        curr = parentIdx                # assing parentIdx to curr for next iteration (which may take place or may not)
        if curr == 0:                   # If curr==0 then we are pointing to the laregst element, so simply break from the loop
            break
        parentIdx = (curr-1)//2         # update parentIdx
        
    print(arr)

def delete(arr):
    if len(arr) == 0:                   # Obvious base case
        return arr
    if len(arr) == 1:                   # If only one element is present, after deleting it we have empty list, thus returning it
        return []
    
    arr[0] = arr[-1]                    # Copying the last element of the list to the first
    arr.pop()                           # Removing the last element
    curr = 0                            # Setting curr to 0 to point the first element of the array / root of the heap
    while True:
        left = 2 * curr + 1             # Finding index position of the left child
        right = 2 * curr + 2            # Finding index position of the right child
        largest = curr                  # Assuming current element is largest (larger among itself, left and right child)
        if left < len(arr) and arr[left] > arr[largest]:
            largest = left               # Updating the largest to point to the left child if it is larger than curr which we assumed to be largest   
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right              # Updating the largest to point to the right child, if it is either greater than the parent or the left child
        if largest == curr:              # if largest is never updated, it remains equal to curr, means parent is greater than child hence no swap reqd.
            break

        arr[curr], arr[largest] = arr[largest], arr[curr] # Swap between the parent and the largest element (either the left or the right child)

        curr = largest                  # Update curr with largest for further iteration 

    print(arr)


    
arr = []
insertInPQ(arr, 1)
insertInPQ(arr, 2)
insertInPQ(arr, 3)
insertInPQ(arr, 4)
insertInPQ(arr, 0)
insertInPQ(arr, 5)
insertInPQ(arr, 6)
insertInPQ(arr, 7)
delete(arr)
delete(arr)
insertInPQ(arr, 9)
insertInPQ(arr, 10)
delete(arr)
delete(arr)

        
    