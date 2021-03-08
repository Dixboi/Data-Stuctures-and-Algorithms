def bubble_sort(list_to_be_sorted):
	for number_1 in range(len(list_to_be_sorted)):
		for number_2 in range(len(list_to_be_sorted)):
			if list_to_be_sorted[number_1] < list_to_be_sorted[number_2]:
				list_to_be_sorted[number_1], list_to_be_sorted[number_2] = list_to_be_sorted[number_2], list_to_be_sorted[number_1]
				
	return list_to_be_sorted
