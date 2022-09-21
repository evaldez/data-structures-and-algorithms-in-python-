def find_factorial_recursive(n):
    # base case
    if n == 1: return 1
    # recursive case
    m = n-1
    result = find_factorial_recursive(m)*n
    # return result
    return result

def find_factorial_iterative(n):
    result = 1
    m = n
    for m in range(1,n+1):
        result = result * m
    return result

if __name__ == '__main__':
    result_r = find_factorial_recursive(5)
    print(result_r)
    result_i = find_factorial_iterative(5)
    print(result_i)
