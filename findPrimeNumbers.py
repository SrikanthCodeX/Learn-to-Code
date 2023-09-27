# find prime numbers upto N
# Time Complexity is O(N^2)

prime_numbers = [2]
def find_prime_numbers(N):

    for number in range(3, N+1):
        if not has_factors(number):
            prime_numbers.append(number)
    return prime_numbers

def has_factors(number):
    check_factors_upto = (number // 2) + 1
    for i in range(2,check_factors_upto):
        if number % i == 0:
            return True
    return False


find_prime_numbers(100)
print(prime_numbers)









