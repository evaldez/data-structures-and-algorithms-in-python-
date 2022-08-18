def reverse(string):
    inversed_string=[]
    len_string = len(string) 
    str_last_index = len_string - 1
    for index, letter in enumerate(string):
        inversed_string.append(string[ str_last_index - index ])
        
    joined_string =  ''.join(str(x) for x in  inversed_string)
    return joined_string

if __name__ == '__main__':
    string = 'Hello World!'
    result = reverse(string)
    print(result)