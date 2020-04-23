# Return True or false if the given string is an anagram

# Example eat, tea -> True

# Example Fire, roof -> False
def is_anagram(string1, string2):
# If the length of both string are not the same
    if len(string1) != len(string2):
        print('False')
        return False
# Sort list in alphabetical order
    one_sort = sorted(string1)
    two_sort = sorted(string2)
# Check if the sorted lists are the same
    if one_sort == two_sort:
        return True
    else:
        return False
    # return false if at any point letters don't match
# all letters match return true
one = 'woi'
three = [1,2,5,3]
two = 'iwo'
print(is_anagram(one, two)) 


# Given an integer array, find a maximum product of a triplet in array

# Example [5,3,7,1,9] -> 315

#   9*7*5

# Sort the list in descending order

# multiply the first 3 items in the array

# return the result
