from random import randint
from fractions import Fraction
from time import time
from typing import List

OP = ['+', '-', '*', '/']


def makeFormula(upperLimit=100, fraction=False) -> str:
    if fraction:
        upperLimit = 20
        count = randint(4, 8)
    else:
        count = randint(1, 3)
    build = ""
    number1 = randint(1, upperLimit)
    build += str(number1)

    for i in range(count):
        if fraction and (i+1) % 2:
            operation = 3
        elif fraction:
            operation = randint(1, 2)
        else:
            operation = randint(1, 3)
        number2 = randint(1, upperLimit)
        op = ' ' + OP[operation] + ' '
        build += op + str(number2)

    return build


def solvingPostfixExpression(postfixList: List[str]):
    operandStack = []

    # 计算后缀表达式
    for token in postfixList:
        if token in "+-*/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            try:
                result = doMath(token, operand1, operand2)
                operandStack.append(result)
            except:
                return "ERROR: Dividend cannot be 0"
        else:
            operandStack.append(int(token))

    return operandStack.pop()


def getPostfixExpression(infixExpr: str) -> List[str]:
    # 记录操作符优先级
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    postfixList = []
    operatorStack = []
    # 以空格分割表达式, 并转为字符数组
    tokenList = infixExpr.split()

    # 中缀表达式转换为后缀表达式
    for token in tokenList:
        if token in "+-*/":
            while operatorStack and \
                    prec[operatorStack[-1]] >= prec[token]:
                postfixList.append(operatorStack.pop())
            operatorStack.append(token)
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            topToken = operatorStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operatorStack.pop()
        else:
            postfixList.append(token)
    while operatorStack:
        postfixList.append(operatorStack.pop())

    return postfixList


def doMath(op: str, number1, number2):
    if op == '+':
        return number1 + number2
    elif op == '-':
        return number1 - number2
    elif op == '*':
        return number1 * number2
    else:
        return Fraction(number1, number2)


if __name__ == '__main__':
    start = time()
    with open('furmula.txt', 'w', encoding='utf-8') as file:
        for i in range(10000):
            formula = makeFormula()
            postfixExprList = getPostfixExpression(formula)
            result = solvingPostfixExpression(postfixExprList)
            expression = formula + ' = ' + str(result)
            if result >= 0:
                print(expression, file=file)

    print('total time: ', time() - start)
