def bubble_sort(n):
    stop_condition = False
    len_list = len(n)
    while not stop_condition:
        was_a_change = False
        for index, number in enumerate(n):
            if index+1 > len(n)-1: continue
            if n[index] > n[index+1]: # swap numbers
                n[index], n[index+1] = n[index+1], n[index]
                was_a_change = True
            
        if not was_a_change:
            stop_condition = True

    return n

if __name__ == '__main__':
    n = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    n_sorted = bubble_sort(n)
    print(f' n_sorted {n_sorted} ')