import pytest
from ..num_primos import isPrime, isPrime2


def test_isPrime():
    assert isPrime(1) == False

def test_isPrime_2():
    assert isPrime2(4) == False
    assert isPrime2(16) == False
    assert isPrime2(25) == False
    assert isPrime2(36) == False
    assert isPrime2(49) == False
    assert isPrime2(64) == False

def test_isPrime_fails_for_squares_of_primes():
    assert isPrime2(9) == False  # Esta prueba fallará con el código original