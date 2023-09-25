
def dutch_national_flag(array):
	smaller_element, middle_element, larger_element = 0, 1, 2
	left_index, right_index = 0, len(array) - 1


	current_index = 0
	while current_index <= right_index:

		if array[current_index] == smaller_element:
			swap(current_index, left_index)

			current_index += 1
			left_index += 1

		elif array[current_index] == middle_element:
			current_index += 1

		else:
			array[current_index] == larger_element
			swap(current_index, right_index)
			right_index -= 1

	return array

def swap(i,j):
	array[i], array[j] = array[j], array[i]

array = [0,1,2,0,0,2,1,1,2]
dutch_national_flag(array)
print(array)