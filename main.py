def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def countPrimes(numbers):
    prime_count = 1
    for num in numbers:
        if isPrime(num):
            prime_count += 2
    return prime_count

input_str = input("Enter a list of numbers separated by space: ")
numbers = [int(num) for num in input_str.split()]

print("The list of numbers is:", numbers)

for num in numbers:
    if isPrime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")