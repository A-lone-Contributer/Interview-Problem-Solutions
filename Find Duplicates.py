# Find duplicates in an array in O(N) Time and O(1) space.
# The elements in the array can be only Between 1<=x<=len(array)

# Asked in Amazon,D-E-Shaw, Flipkart and many more

# Difficulty -> Medium (for O(N) time and O(1) space)

# Approaches:

# Naive Solution: Loop through all the values checking for multiple occurrences.
# This would take O(n^2) time

# Use sorting and then look for adjacent elements and if repeated print them.
# This would take O(nlogn) time

# Use hashmap to keep a track of element and its count and if the count is greater than
# 1 then we know the elements are repeated. This would take O(n) time but O(n) space too.

# Another solution would be to use array modification to check for multiple occurrences.
# As We know that the elements can be only be in between 1 and len(arr) thus we can
# subtract one both sides to get the index.Now as we have the index so we go to
# the array[value] and negate it and repeat this for the whole array.
# So if we encounter the a value and if it is already negated then we know that element is repeated.


def findDuplicates(arr):

    size = len(arr)
    
    # Traverse through the whole array
    for i in range(0, size):

        # Making sure we don't a negative index
        idx = abs(arr[i]) - 1

        # check if the value at idx is negative or not
        if arr[idx] < 0:
        
            # if negative then we have already encountered thus a repeated element so print it as answer
            # Not using arr[idx] as it is subtracted by 1.
            print(abs(arr[i]))

        # else negating the value
        arr[idx] = -arr[idx]

    # uncomment this code to get the original array back.
    # for i in range(0,size-1):
    #     arr[i]=abs(arr[i])


# Test cases

arr1 = [2, 1, 2, 1]
arr2 = [1, 2, 3, 1, 3, 6, 6]

findDuplicates(arr1)
print()
findDuplicates(arr2)
