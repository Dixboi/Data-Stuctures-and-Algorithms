
def bubble_sort(to_sort):
    for loop_count in range(len(to_sort) - 1):
        for element in range(len(to_sort) - loop_count - 1):
            if to_sort[element] > to_sort[element + 1]:
                to_sort[element], to_sort[element + 1] = to_sort[element + 1], to_sort[element]
                
    return to_sort
