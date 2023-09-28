# Time complexity is O(N)

def find_most_repeated_number(array):
    numbers_with_count = {}
    max_count = 0
    most_repeated_number = None

    for number in array:
        if number not in numbers_with_count:
            numbers_with_count[number] = 0
        numbers_with_count[number] += 1


        if numbers_with_count[number] > max_count:
            most_repeated_number = [number]
            max_count = numbers_with_count[number]

        elif numbers_with_count[number] == max_count:
            most_repeated_number.append(number)

    return most_repeated_number


input_array = [1,2,3,6,4,3,2,11,15,99,83,3,2]
most_repeated = find_most_repeated_number(input_array)
print(most_repeated)