# Find all the permutations of a string

# Asked in Zoho,Amazon

# Difficulty -> Medium

# Approach:
# Make a dictionary of characters of string and their count as key-value pair and separate out both
# and append to respective lists in sorted format so that the result is in lexicographical order.
# Now check for the count and if it is non-zero then recurse and put them in result list and decrease the count for
# that character when the last recursion lvl i.e string is exhauted then backtrack and find the non-zero count and
# do the same till all permutations are found

def string_permutation(s):
    mapping = {}

    # creating a dictionary with character,count as key,value pair
    for char in s:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1

    characters = []
    count = []

    # create a list of sorted string character and their counts
    for i, j in sorted(mapping.items()):
        characters.append(i)
        count.append(j)

    # array to store the result
    result = [0] * len(s)

    string_permutation_helper(characters, count, result, 0)


def string_permutation_helper(s, count, result, level):
    # if the recursion level is equal to length of string

    if level == len(result):
        # print the result and return
        print("".join(result))
        return

    # Traverse through the whole string
    for i in range(len(s)):

        # if count is zero, do nothing
        if count[i] == 0:
            continue

        # if count is non-zero then insert the element in result and decrement its count
        result[level] = s[i]
        count[i] -= 1

        # call the function recursively for the next level
        string_permutation_helper(s, count, result, level + 1)

        # incrementing the count which was decremented before going into recursion
        count[i] += 1


# Driver code
string = input("Enter your string: ")

if string:
    print("Permutations of given string are: ")
    string_permutation(string)
else:
    print("String length should be atleast 1.")

# Time Complexity : O(n!)
# Space Complexity : O(n)
