ARRAY = [1,5,3,2,2,5,4,5,5,5,5,3,1]


def __get_dup_out_dict__(dict):
    dups_list = []
    for key in dict:
        # .get(key) has an average O(1) time complexity
        key_value = dict.get(key)
        if key_value >=2:
            dups_list.append(key)
    return dups_list
        


def duplicate_items(list_numbers):
    nums_dict = {}
    for key in list_numbers:
        # .get(key) has an average O(1) time complexity
        if nums_dict.get(key) is None :
            nums_dict[key] = 1
        elif nums_dict.get(key) >= 1 :
            nums_dict[key] += 1
    dups__list = __get_dup_out_dict__(nums_dict)

    return dups__list
    

print(duplicate_items(ARRAY)) 