def fibonacci_recursive(n):
    # base case
    if n < 2: return n
    # recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    

def fibonacci_iterative(n):
    if n == 0 : return 0
    if n == 1 : return 1

    result = 1
    prev_result = 0
    for m in range(2,n+1):
        tmp_result = result + prev_result
        prev_result = result
        result = tmp_result
    return tmp_result

if __name__ == '__main__':
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    result_r = fibonacci_recursive(43)
    print(result_r)
    result_i = fibonacci_iterative(43)
    print(result_i)
