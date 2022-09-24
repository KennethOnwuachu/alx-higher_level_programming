#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    length = len(my_list)
    new_list = my_list[:]

    if idx > length:
        return (my_list)
    else:
        new_list[idx] = element
        return(new_list)
    
