import pytest
from ..num_primos import isPrime

@pytest.mark.parametrize("n", {
    (1),
})
def test_isPrime(n):
    assert isPrime(n) == True