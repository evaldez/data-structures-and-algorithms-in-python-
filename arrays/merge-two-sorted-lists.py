def mergeSortedArrays(array1, array2):
    joined_array = []
    while(array1 or array2):

        # if array1 is empty add array2 and finish
        if not array1: 
            joined_array += array2
            break

        # if array2 is empty add array1 and finish
        if not array2: 
            joined_array += array1
            break

        if array1[0] <= array2[0]:
            joined_array.append(array1[0])
            del array1[0]
        else:
            joined_array.append(array2[0])
            del array2[0]

    return joined_array

def mergeSortedArraysV2(array1, array2):
    
    if not array1  or not array2:
        print("un array está vacio")
        return array1 + array2

    joined_array = []
    array1index = 0
    array2index = 0

    while( array1index < len(array1) and array2index < len(array2)  ):
        if array1[array1index] < array2[array2index]:
            joined_array.append(array1[array1index])
            if array1index<len(array1):
                array1index+=1
        else:
            joined_array.append(array2[array2index])
            if array2index<len(array2):
                array2index+=1

    return joined_array + array1[array1index:] + array2[array2index:]


if __name__ == '__main__': 
    array1 = [0,3,4,31]
    array2 = [3,4,6,30]

    result = mergeSortedArraysV2(array1, array2)
    #result = mergesortedarr(array1, array2)
    print(result)