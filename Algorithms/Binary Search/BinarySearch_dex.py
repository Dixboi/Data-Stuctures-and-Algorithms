def binary_search(lst, toFind):
    start = 0
    last = len(lst) - 1
    
    while start <= last:
        middle = (start + last) // 2
        if lst[middle] == toFind:
            return middle
        elif toFind < lst[middle]:
            last = middle - 1
        elif toFind > lst[middle]:
            start = middle + 1
			
    #if the element is not in the list
    return -1
