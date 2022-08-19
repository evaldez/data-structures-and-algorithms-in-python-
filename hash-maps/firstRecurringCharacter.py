#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined


def firstRecurringCharacter(input):
    rec_char=None
    hashmap={}
    for char in input:
        if char in hashmap.keys(): return char
        hashmap[char] = True
    return None

if __name__ == '__main__':
    array1 = [2,5,1,2,3,5,1,2,4]
    rec_char = firstRecurringCharacter(array1)
    print(f' Recurring char: {rec_char} ')
    array2 = [2,5,5,2,3,5,1,2,4]
    rec_char = firstRecurringCharacter(array2)
    print(f' Recurring char: {rec_char} ')
    array3 = [2,3,4,5]
    rec_char = firstRecurringCharacter(array3)
    print(f' Recurring char: {rec_char} ')