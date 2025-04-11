import pytest
from ..num_primos import isPrime


def test_isPrime():
    assert isPrime(1) == False

def test_isPrime_fails_for_squares_of_primes():
    assert isPrime(9) == False  # Esta prueba fallará con el código original