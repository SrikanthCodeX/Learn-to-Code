import sys


def find_duplicates(array):
    duplicates = []
    for item in array:
        if array.count(item) > 1:
            duplicates.append(item)
    return duplicates


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("arguments missing")
    else:
        input_array = sys.argv[1].strip("[]").split(",")
        duplicates = find_duplicates(input_array)
        print(duplicates)


# python FindDuplicates.py [1,2,3,4,3,2,1,5,7,6,7,9]
# python FindDuplicates.py [100,99,98,97,50,98,55,43,29,97]
