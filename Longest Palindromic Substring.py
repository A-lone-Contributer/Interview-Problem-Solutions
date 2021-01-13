# Find the longest Palindromic Substring

# Asked in Amazon ,MakeMyTrip, Microsoft, Qualcomm, Visa

# Difficulty -> Medium

# Algorithm:
# We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and
# there are only 2n - 1 such centers. You might be asking why there are 2n - 1 but not nn centers? The reason is the
# center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba")
# and its center are between the two 'b's.

# function to find longest palindrome
def longestPalindrome(s: str) -> str:
    # if the length is 0 or 1 then simply return the string
    if len(s) < 2:
        return s
    start, end = 0, 0

    # iterate till the length of string 
    for i in range(len(s)):

        # expand around center for odd length strings
        len1 = expandFromCenter(s, i, i)

        # expand around center for even length strings
        len2 = expandFromCenter(s, i, i + 1)

        # find the max of both
        l = max(len1, len2)
        
        # compute the start and end after checking if 
        # it is bigger than the length we already have
        if l > end - start:
            start = i - (l - 1) // 2
            end = i + l // 2

    return s[start:end + 1]


# utility function to expand from center
def expandFromCenter(s, idx1, idx2):
    
    # this loop simply check for palindromic property
    while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
        idx1 -= 1
        idx2 += 1
    return idx2 - idx1 - 1


# driver code
string = "abcddcb"
print(longestPalindrome(string))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
