# Given a list of numbers and a number k, return pair of two numbers from the list which add up to k

# Asked in google 

# Difficulty --> Easy

# There can be a lot of ways to solve this problem. Naive approach would
# be to check for all the combinations using nested loop which would take
# O(n^2) time. 

# An efficient approach would be to use a set DS and search for the difference
# of array elements and k in our list. This would take linear time and O(n) space


def checkSum(arr, n, k):
    # HashMap to store our difference
    hashmap = {}
    
    # Traversing the list
    for i in range(n):

        # Inserting the element in our HashMap
        hashmap[arr[i]] = i

        #  check if HashMap has the element needed
        if hashmap.get(k - arr[i]) and hashmap.get(k - arr[i]) != i:
        
            # Printing the pairs (not duplicates)
            print(f"({arr[i]},{k - arr[i]})", sep=',')


# test case 1
arr = [-40, -5, 1, 3, 6, 7, 8, 20]
n = len(arr)
k1 = 15
checkSum(arr, n, k1)

print()

# test case 2
arr1 = [2, 5, 3, 6, 7, 2]
n = len(arr1)
k2 = 5
checkSum(arr1, n, k2)

# Time complexity: O(n) -> Best and average
# Space complexity : O(n)
