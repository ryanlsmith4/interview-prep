LIST1 = [1, 2, 4, 5, 6, 7, 8, 9, 10]

LIST2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

LIST3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

LIST4 = [2, 3, 4, 5, 6, 7, 8, 9]

def find_missing_number(list_numbers):
    numbers_needed = [1,2,3,4,5,6,7,8,9,10] 
    for i, j in zip(list_numbers, numbers_needed):
        print(i,j)
        if i != j:
            print(i,j)
            return j
        else:
            return list_numbers[-1] + 1

print(find_missing_number(LIST4))