from ..suma_bits import add8
import pytest

def test_add8_full_coverage():
    # Caso 1: 0 + 0 + 0 = 0
    assert add8(*[False]*16, False) == (False,)*8 + (False,)
    
    # Caso 2: 0 + 0 + 1 = 1
    assert add8(*[False]*16, True) == (True,) + (False,)*7 + (False,)
    
    # Caso 3: 1 + 1 + 0 = 0 con carry 1
    assert add8(True, *[False]*7, True, *[False]*7, False) == (False, True) + (False,)*6 + (False,)
    
    # Caso 4: 255 + 1 + 0 = 0 con carry 1 (11111111 + 00000001)
    assert add8(
        True, True, True, True, True, True, True, True,      # a = 255
        True, False, False, False, False, False, False, False,  # b = 1
        False
    ) == (False,)*8 + (True,)
    
    # Caso 5: 255 + 1 + 1 = 1 con carry 1
    assert add8(
        True, True, True, True, True, True, True, True,       # a = 255
        True, False, False, False, False, False, False, False,  # b = 1
        True
    ) == (True,) + (False,)*7 + (True,)
    
    # Caso 6: 15 + 1 + 0 = 16 (00001111 + 00000001)
    assert add8(
        False, False, False, False, True, True, True, True,   # a = 00001111
        True, False, False, False, False, False, False, False,  # b = 00000001
        False
    ) == (True,) + (False,)*3 + (True,)*4 + (False,)
