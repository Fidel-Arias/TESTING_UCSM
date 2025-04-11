import pytest
from ..Stats import stats

def test():
    ###Your code here.
    # Change l to something that manages full coverage. You may
    # need to call stats twice with different input in order
    # to achieve full coverage.
    
    # Caso 1: Lista vacía (cubre None en min/max y manejo de lista vacía)
    stats([])
    
    # Caso 2: Lista con un solo elemento (cubre median para longitud impar y freq=1)
    stats([5])
    
    # Caso 3: Lista con elementos repetidos (cubre incremento en freq y cálculo de moda)
    stats([2, 2, 3, 4])
    
    # Caso 4: Lista con número par de elementos (cubre median para longitud par)
    stats([1, 2, 3, 4, 5, 6])
    
    # Caso 5: Lista con múltiples modas (cubre mode con varios valores)
    stats([1, 1, 2, 2, 3])
    
    # Caso 6: Lista con todos elementos iguales (cubre caso especial de moda)
    stats([7, 7, 7])

# def test_stats_output(capsys):
#     # Test output for specific cases
#     test_cases = [
#         ([], "min = None\nmax = None\nmedian = None\nmode(s) = []"),
#         ([5], "min = 5\nmax = 5\nmedian = 5\nmode(s) = [5]"),
#         ([1, 2, 2, 3], "min = 1\nmax = 3\nmedian = 2.0\nmode(s) = [2]"),
#         ([1, 1, 2, 2], "min = 1\nmax = 2\nmedian = 1.5\nmode(s) = [1, 2]")
#     ]
    
#     for input_list, expected_output in test_cases:
#         stats(input_list)
#         captured = capsys.readouterr()
#         assert expected_output in captured.out

# NUEVO TEST QUE DETECTA EL ERROR
def test_negative_numbers(capsys):
    stats([-5, -3, -7])
    captured = capsys.readouterr()
    # Este test fallará porque esperamos max = -3 pero el código devuelve max = "N/A"
    assert "max = -3" in captured.out