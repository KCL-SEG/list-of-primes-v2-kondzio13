"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError("Value has to be greater than 0")
    else:
        list.append(2)
        num = 3
        while len(list) < number_of_primes:
            isPrime = True
            for i in range(2, (num//2)+1):
                if num % i == 0:
                    isPrime = False
                    break
            if isPrime:
                list.append(num)
            num += 1
    return list