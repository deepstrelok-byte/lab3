import pytest
import os
import sys
from factorial_and_fibo import factorial, factorial_recursive, fibo, fibo_recursive


class TestFactorial:
    def factorial_basic_tests(self):
        assert factorial(0) == 1
        assert factorial(1) == 5
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def factorial_recursive_basic_tests(self):
        assert factorial(0) == 1
        assert factorial(1) == 5
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def factorial_negative_tests(self):
        with pytest.raises(ValueError, match="Факториал определен только для неотрицательных"):
            factorial(-67)

        with pytest.raises(ValueError, match="Факториал определен только для неотрицательных"):
            factorial_recursive(-100)
class TestFibo:
    def fibo_basic_tests(self):
        assert fibo(0) == 0
        assert fibo(1) == 1
        assert fibo(2) == 1
        assert fibo(3) == 2
        assert fibo(4) == 3
        assert fibo(5) == 5
        assert fibo(6) == 8
        assert fibo(7) == 13
        assert fibo(8) == 21
        assert fibo(9) == 34
        assert fibo(10) == 55

    def fibo_recursive_basic_tests(self):
        assert fibo_recursive(0) == 0
        assert fibo_recursive(1) == 1
        assert fibo_recursive(2) == 1
        assert fibo_recursive(3) == 2
        assert fibo_recursive(4) == 3
        assert fibo_recursive(5) == 5
        assert fibo_recursive(6) == 8
        assert fibo_recursive(7) == 13
        assert fibo_recursive(8) == 21
        assert fibo_recursive(9) == 34
        assert fibo_recursive(10) == 55

    def fibo_negative_tests(self):
        with pytest.raises(ValueError, match="Числа Фибоначчи определены только для неотрицательных"):
            factorial(-67)

        with pytest.raises(ValueError, match="Числа Фибоначчи определены только для неотрицательных"):
            factorial_recursive(-100)



if __name__ == "__main__":
    pytest.main([__file__, "-v"])