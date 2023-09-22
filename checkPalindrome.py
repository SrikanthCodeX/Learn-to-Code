
def check_palindrome(word):
    length_of_word = len(word)
    length_to_check= len(word)//2
    index = 0

    while index <= length_to_check:
        if word[index] != word[length_of_word-1]:
            print(f'{word} is not a palindrome')
            return
        index += 1
        length_of_word -= 1
    print(f'{word} is a palindrome')

check_palindrome("antarcita")
check_palindrome("rotator")

