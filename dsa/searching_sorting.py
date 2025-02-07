class SearchingSorting:

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "\r\n\033[38;5;208m  TRY CODING ALL THE ALGORITHMS BY YOURSELF AFTER UNDERSTANDING THEM ON PEN AND PAPER. STRICTLY CODE THEM IN C !!  \033[0m\n\n"


    def merge(self,left, right):
        i = j = 0                               # i and j point to the first elements of the left and right sorted sub arrays
        arr = []                                # Auxuliary space


        while i < len(left) and j < len(right): # We run this for loop until either the left or the right or both sorted sub arrays are exhausted
            if left[i] <= right[j]:             # if the current smallest element of left is smaller than the current smallest element of the right sorted sub array
                arr.append(left[i])             # we simply take the ith element of left (current smallest element of the left sorted array) and append it to arr
                i += 1                          # Followed by this we increment i to point to the next smallest element of left sorted subarray
            else:
                arr.append(right[j])            # Similar as above condition
                j += 1                          # Similar as above condition

        """
            At this point of time, we have exited the above while loop meaning that either the left or the right or both the sorted sub arrays are exhausted
        """

        if i < len(left):                       # This means if the left sorted sub array is still not exhausted, meaning right one would have been exhausted (since we exited the while loop)
            arr.extend(left[i:])                # We simply append the remaining left sub array to the arr[]
        elif j < len(right):                    # Similar to above condition
            arr.extend(right[j:])               # Similar to the above condition

        return arr                              # Finally we return arr which is the merger of the left and the right sorted sub arrays, this arr is also sorted

    def MergeSort(self, arr):


        """
        Best Case : O(nlogn)
        Avg Case : O(nlogn)
        Worst Case : O(nlogn)
        """
        
        if len(arr) <= 1:                       # This condition becomes true when there is only 1 element in the array, we arrive at the condition at the last level of recursion for an array
            return arr                          # An array consisting of a single element is always sorted, so we simply return that array
        mid = len(arr) // 2                     # Here we are calculating the mid index of the array, which is used to split the array into 2 halves

        _left = self.MergeSort(arr[:mid])       # We recursively apply Merge Sort on the left sub array, store the sorted left part for the particular recursion step in _left
        _right = self.MergeSort(arr[mid:])      # We recursively apply Merge Sort on the right sub array, store the sorted left part for the particular recursion step in _right
        m_arr = self.merge(_left, _right)       # After the left and the right subarrays are sorted we merge them and store the merged sorted array in m_arr


        return m_arr                            # return the merged sorted array, -> here we go from the bottom to the top of the recusion tree

    def insertionSort(self, arr):

        """
        Best Case : O(n)
        Avg Case  : O(n^2)
        Worst Case: O(n^2)
        """

        # Not adding comments to this one,  try understanding, running and coding this by yourself (strictly in C !)

        for i  in range(1, len(arr)):
            key = arr[i]
            j = i 
            while j > 0 and arr[j-1] > key:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = key
        print("Sorted using insertion sort:  ", end = '')
        print(arr)



    def partititonQS(self, arr, low, high):
        pivot = arr[low]                            # Here we are taking the pivot element as the first element, we are free to take any element as pivot
        i = low                                     # Starting the i pointer from the pivot position
        j = high                                    # Starting the j pointer from the end position

        while i < j:
            while arr[i] <= pivot  and i < high:    # Here we are incrementing i pointer until we are finding an element which is greater than pivot, observe why we are setting upper bound for i as high-1, as it would prevent us from index out of bound conditon (try taking original array as [2,1] to understand this)
                i+=1
            while arr[j] > pivot and j > low:       # Here we are decrementing j till we find an element which is less than or equal to the pivot element, similar explaination for lower bound of j
                j-=1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]     # Once we come out of the above for loop (we found ith element > pivot and jth element <= pivot), we check if i < j, if yes then we just swap the ith and the jth element of the array, if i > j, we get out of this while loop

        arr[low] , arr[j] = arr[j], arr[low]        # At this point of time, we still have ith element > pivot and jth element <= pivot but i > j, so here we swap the jth element(the smaller than or equal to element of the pivot) with the pivot --- HERE arr[low] IS THE PIVOT ELEMENT

        return j                                    # At this point, the pivot is at this correct position (the position at which it should have been in the sorted array), hence we return the new index position of pivot i.e j (as we had swapped the pivot with the jth element)
        
    def QuickSort(self, arr, low, high):

        """
        Best Case : O(nlogn)
        Avg Case : O(nlogn)
        Worst Case : O(n^2)
        """

        if low < high:                                  # This is the base case for the recursion, we only divide the array when its size > 1
            pivot = self.partititonQS(arr, low, high)   # Partition operation returns index position of pivot (the element which went to its right place in the partititonQS() function)
            self.QuickSort(arr, low, pivot-1)           # Apply this function recursively on the left subarray wrt pivot
            self.QuickSort(arr, pivot+1, high)          # Apply this function recursively on the right subarray wrt pivot

        return arr                                      # return the sorted array / subarray


         

    def BubbleSort(self, arr):

        """
        Best Case : O(n)
        Avg Case  : O(n^2)
        Worst Case: O(n^2)
        """

        for i in range(len(arr)):                           # Take i from the start of the array to the end
            swapped = False                                 # Set swapped flag to false to later check if there is any swap amongst the eleements of the array
            for j in range(len(arr)-i-1):                   # We only take this j till the mentioned index, because to the right of it, we have already bubbled up greater elements, the greatest element of the array is placed at the last position after the complete first iteration and so on ...
                if arr[j] > arr[j+1] :                      # Check if the element at jth index is greater than element at j+1 th index
                    arr[j], arr[j+1] = arr[j+1] , arr[j]    # If yes, then swap those two elements
                    swapped = True                          # Mark the swapped flag to True 
                
            if not swapped:                                 # If any element is not swapped in the above iteration then it means array is sorted and therefore swapped remains false
                break                                       # Therefore we break from the outer for loop, marking the end of the sorting process
        
        print("Sorted using Bubble Sort :    ", end='')
        print(arr)



    def SelectionSort(self, array):

        """
        Best Case : O(n^2)
        Avg Case  : O(n^2)
        Worst Case: O(n^2)
        """

        for i in range(len(array)-1):                           # We take i from 0 the 2nd last index, because after the final operation, we only have one element left and all other elements are at right position, so we need not process for final element, take array [2,1] to understand this 
            min = array[i]                                      # Assume the ith element of the array to be minimum (subarray towards the left is sorted)
            minIdx = i                                          # Initialise index position of minimum element with i
            for j in range(i, len(array)):                      # Traverse the entire array from i to the end to find the minimum element
                if array[j] < min:                              # check if current element is less than minimum element
                    min = array[j]                              # If yes, then update the minumum element
                    minIdx = j                                  # Also update the index position of the minumum element
                
            
            array[minIdx], array[i] = array[i], array[minIdx]   # Now swap the ith element (from where we started traversing the array) with the minimum element of the traversed array
 
        print("Sorted using Selection Sort : ", end='')
        print(array)




    def BinarySearch(self, arr, low, high, target):
        """
            Prerequisites : Araay is already sorted
            high and low are the start and end indices of the array for which we are calling BinarySearch
        """


        if low > high:                                          # Low > High means we have traversed the entire array and got noting in hand
            print("element not found")                          # So we simply exit with this print statement
            # return -1
        if high >= low:                                         # Just to check if high >= low
            mid = (high + low) // 2                             # Find the middle index
            if arr[mid] == target:                              # If middle element is equal to the target, print its position and exit from the function call    
                print(f"element found at posiiton :   {mid}")
                # return mid
            elif arr[mid] > target:                             # If target element is less than the middle element
                self.BinarySearch(arr, low, mid - 1, target)    # Search for the left of the array wrt mid, for the left array, low remains the same and high becomes mid-1
            else:
                self.BinarySearch(arr, mid + 1, high, target)   # else do the opposite, now the high remains the same,  and low changes to mid + 1

        """
            If the target element actually exists in the array, then it would boil down to the condition of target == arr[mid]
        """
        
        



        

mylist = [3,2,34,56,27,23,30]

arr = SearchingSorting() ; print(arr)

arr.BubbleSort(mylist.copy())

arr.SelectionSort(mylist.copy())

qs_sorted = arr.QuickSort(mylist.copy(), 0, len(mylist)-1)
print("Sorted using QuickSort Sort : ", end='')
print(qs_sorted)

ms_sorted = arr.MergeSort(mylist.copy())
print("Sorted using Merge Sort :     ", end='')
print(ms_sorted)

arr.insertionSort(mylist.copy())

arr.BinarySearch(ms_sorted, 0, len(ms_sorted)-1, 1)

