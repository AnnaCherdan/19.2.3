import pytest
from app.calculater import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_correctly_division(self):
        assert self.calc.division(self, 2, 15)

    def test_correctly_subtraction(self):
        assert self.calc.subtraction(self, 3, 10)

    def test_correctly_adding(self):
        assert self.calc.adding(self, 7, 8)
