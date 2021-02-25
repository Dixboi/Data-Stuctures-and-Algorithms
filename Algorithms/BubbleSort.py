
def bubble_sort(list_to_be_sorted):
	for number_1 in range(len(list_to_be_sorted)):
		for number_2 in range(len(list_to_be_sorted)):
			if list_to_be_sorted[number_1] < list_to_be_sorted[number_2]:
				list_to_be_sorted[number_1], list_to_be_sorted[number_2] = list_to_be_sorted[number_2], list_to_be_sorted[number_1]
				
	return list_to_be_sorted

if __name__ == "__main__":
    list_to_be_sorted = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    print("Not sorted list: ")
    print(list_to_be_sorted)
    print()
    sorted_list = bubble_sort(list_to_be_sorted)
    print("Sorted list: ")
    print(sorted_list)
