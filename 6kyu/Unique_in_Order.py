def unique_in_order(iterable): 
    unique_list = []
    prev = None
    for i in iterable:
        if i != prev:
            unique_list.append(i)
        prev = i
    return unique_list
