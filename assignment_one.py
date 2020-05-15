# Assignment 1
# Code out 2 solutions for each of the 3 problems. Use your pseudocode to guide your comments. 
# Problem 1
# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
def sum_of_t(list, t):
    if len(list) == 0:
        return 'empty list'
    for num in list:
        for num2 in list:
            if num + num2 == t:
                return [num, num2]
    return 'No Candidates'

def sum_of_t_better(list, t):
    if len(list) == 0:
        return 'empty list'
    pairs = {}
    for num in list:
        val = t - num
        if num in pairs:
            return [num, val]
        pairs[val] = num
    return 'No Candidates'
# Problem 2
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]
def slice_sol(list, k):
    if len(list) == 0:
        return 'empty list'
    list.sort(reverse=True)
    return list[:k]

def max_list(list, k):
    if len(list) == 0:
        return 'empty list'
    solution = []
    for i in range(k):
        maxI = max(list)
        ind = list.index(maxI)
        list.pop(ind)
        solution.append(maxI)
    return solution

# Problem 3
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]
if __name__ == "__main__":
    b=[5, 1, 3, 6, 8, 2, 4, 7]
    k=3
    a=[5, 3, 6, 8, 2, 4, 7]
    t=10
    # print(sum_of_t(a, t))
    # print(sum_of_t_better(a, t))
    # print(slice_sol(b, k))
    print(max_list(b, k))