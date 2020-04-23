TEST = 'hello'

TEST2 = "Apple"

TEST3 = 'madam'


def is_palindrome(str):
    if str == '':
        return True
    i = 0
    j = len(str) -1
    while i < j:
        # print(str[i], str[j])
        if str[i] != str[j]:
            print(str[i], str[j])
            return False
        else:
            i+=1 
            j-=1
    return True



if __name__ == "__main__":
    print(is_palindrome(''))