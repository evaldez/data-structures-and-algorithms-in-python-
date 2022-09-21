def selection_sort(n):
    stop_condition = False
    len_list = len(n)
    smallest_index = None
    smallest_number = None
    
    for out_index, out_number in enumerate(n):
        first_iter=True
        for in_index, number in enumerate(n):
            if in_index < out_index : continue 
            if first_iter:
                smallest_index = in_index
                smallest_number = number
                first_iter=False
                continue
            if smallest_number > number: 
                smallest_index = in_index
                smallest_number = number
        n[out_index], n[smallest_index]  = n[smallest_index], n[out_index]

    return n

if __name__ == '__main__':
    n = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    n_sorted = selection_sort(n)
    print(f' n_sorted {n_sorted} ')