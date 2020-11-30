# Count the number of 2s as digit in all numbers from 0 to n.

# Asked in Amazon
# Difficulty -> Easy

def occurrenceof2(n):

    # count variable to count the occurrence of 2's
    count = 0
    
    # traverse till the target
    for i in range(1, n + 1):
    
        # Cast the number to string and count the number of 2's and add it to count
        count += str(i).count('2')
        
    return count


# Test cases
print(occurrenceof2(22))
print(occurrenceof2(100))

# Time complexity : O(n)
# Space complexity : O(1)
