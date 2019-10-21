# Given a pattern containing only I’s and D’s. I for increasing and D for decreasing.
# Devise an algorithm to print the minimum number following that pattern.
# Digits from 1-9 and digits can’t repeat.

# Asked in Amazon,goldmann sacs and google
#  Difficulty -> medium


# Approach:
# We have to take numbers from 1-9 so we always push (i+1) to our stack.
# Then we check what is the resulting character at the specified index.
# So,there will be two cases which are as follows:-
# Case 1: If we have encountered I or we are at the last character of input string,then pop from the stack
# and add it to the end of the output string until the stack gets empty.
# Case 2: If we have encountered D, then we want the numbers in decreasing order.
# so we just push (i+1) to our stack.

def decode(seq):
    # A list implemented as stack
    l = []
    
    # Stores the size of given sequence
    n=len(seq)

    # resultant string
    decoded_string = ""
    
    # loop running one more than the sequence length as the decoded string is
    # one more in lenght of sequence
    for i in range(0, n + 1):
    
        # pushing number i+1 into the stack
        l.append(i + 1)

        # if all characters of the input sequence are
        # processed or current character is 'I'
        # (increasing)
        if i == len(seq) or seq[i] == "I":
        
            # while the stack is empty
            while l:
            
                # add the elements in stack to the result 
                decoded_string += str(l.pop())

    # printing the result
    print(decoded_string)


# Test cases

decode("IDID")
decode("I")
decode("DD")
decode("II")
decode("DIDI")
decode("IIDDD")
decode("DDIDDIID")

# Time Complexity : O(n)
# Space Complexity : O(n)
