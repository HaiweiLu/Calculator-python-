import unittest
from fractions import Fraction

from Calculator.main import getPostfixExpression, solvingPostfixExpression


class MyTestCase(unittest.TestCase):
    def test_solvingPostfixExpression_valid(self):
        test = solvingPostfixExpression(['3', '5/1', '÷', '1', '6', '÷', '-'])
        result = Fraction(13, 30)
        self.assertEqual(test, result)

        test = solvingPostfixExpression(['3', '15', '*', '20', '4', '÷', '-'])
        result = 40
        self.assertEqual(test, result)

    def test_solvingPostfixExpression_invalid(self):
        test = solvingPostfixExpression(['2', '0', '÷'])
        result = "NAN"
        self.assertEqual(test, result)

        test = solvingPostfixExpression(['6', '5', '10', '2', '÷', '-', '÷'])
        result = "NAN"
        self.assertEqual(test, result)

    def test_getPostfixExpression(self):
        test = getPostfixExpression(["22", "÷", "2"])
        result = ["22", "2", "÷"]
        self.assertEqual(test, result)

        test = getPostfixExpression(["38", "-", "5", "*", "6"])
        result = ['38', '5', '6', '*', '-']
        self.assertEqual(test, result)

        test = getPostfixExpression(["(", "16", "-", "9", ")", "*", "6"])
        result = ['16', '9', '-', '6', '*']
        self.assertEqual(test, result)


if __name__ == '__main__':
    unittest.main()
