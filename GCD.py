# Find the maximum length subarray with GCD=1

# Difficulty -> Easy

# Asked in Zoho

# Approach:
# If a array has any two element GCD as 1 then the whole array has GCD=1
# using this logic, we will return the length of array as maximum subarray if it has
# any two elements with gcd 1


# Utility function to find gcd of two numbers
def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a


def gcd_1(arr1):
    # store the first element
    res = arr1[0]

    # loop through the array and calculate gcd with current res and current element
    for i in range(1, len(arr1)):
        res = gcd(res, arr1[i])

    # if gcd found to be 1 then return length of array else -1
    print(len(arr1) if (res == 1) else -1)


# Driver Code
arr1 = [2, 2, 4]
arr2 = [7, 2]

print(gcd_1(arr1))
print(gcd_1(arr2))

# Time Complexity : O(N)
# Space Complexity : O(1)
