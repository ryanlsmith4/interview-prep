# Speed O(n) Space O(n)

example_list = [1,2,3,4,5,6]
def reverse_list(old_list):
    new_list = []

    for index in range(len(old_list)):
        new_index = len(old_list) - 1 - index
        new_list.append(old_list[new_index])
    return new_list


print(reverse_list(example_list))
