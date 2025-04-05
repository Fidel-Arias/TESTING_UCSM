import math

def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if number % check == 0:
            return False
    return True

def check(n):
    print("isPrime(" + str(n) + ") = {}".format(isPrime(n)))


check(1)
check(2)
check(3)
check(4)
check(5)
check(20)
check(21)
check(22)
check(23)
check(24)