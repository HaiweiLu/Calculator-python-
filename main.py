from random import randint, random
from fractions import Fraction
from time import time
from typing import List

OP = ['+', '-', '*', '÷']


def makeFormula(upperLimit=100,
                fraction=False) -> List[str]:
    if fraction:
        upperLimit = 20

    # 运算数的个数
    count = randint(3, 5)
    build = []
    number = randint(1, upperLimit)
    build.append(str(number))

    for _ in range(count):
        # 把乘法除法的比重降低
        if random() > 0.618:
            operation = randint(2, 3)
        else:
            operation = randint(0, 1)
        # 设置有一定概率生成含有分数与整数的表达式
        if fraction and random() > 0.5:
            numerator = randint(1, upperLimit - 1)
            denominator = randint(numerator + 1, upperLimit)
            number = Fraction(numerator, denominator)
        else:
            number = randint(1, upperLimit)
        build.append(OP[operation])
        build.append(str(number))

    return build


def addBrackets(formula: List[str]) -> List[str]:
    # op1: 是否包含 +-, op2: 是否包含*÷
    op1, op2 = False, False
    for item in formula:
        if item in "+-":
            op1 = True
        elif item in "*÷":
            op2 = True

    # 表达式如果含有的运算符优先级是相等的, 就无需添加括号
    if not (op1 and op2):
        return formula

    # 随机插入括号
    station = [i for i in range(0, int(len(formula) / 2) + 2, 2)]
    index = station[randint(0, len(station) - 1)]
    _formula = formula[:index] + ['('] + formula[index:]
    _formula = _formula[:index + 4] + [')'] + _formula[index + 4:]

    return _formula


def solvingPostfixExpression(postfixList: List[str]):
    operandStack = []

    # 计算后缀表达式
    for token in postfixList:
        if token in "+-*÷":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            try:
                result = doMath(token, operand1, operand2)
                operandStack.append(result)
            except:
                return 'NAN'
        else:
            try:
                token = int(token)
            except:
                token = Fraction(token)
            operandStack.append(token)

    return operandStack.pop()


def getPostfixExpression(infixExpr: List[str]) -> List[str]:
    # 记录操作符优先级
    prec = {'*': 3, '÷': 3, '+': 2, '-': 2, '(': 1}
    postfixList = []
    operatorStack = []

    # 中缀表达式转换为后缀表达式
    for token in infixExpr:
        if token in "+-*÷":
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


def main() -> (str, float):
    formula = makeFormula(upperLimit=16, fraction=True)
    _formula = addBrackets(formula)
    postfixExprList = getPostfixExpression(_formula)
    result = solvingPostfixExpression(postfixExprList)
    _formula = ' '.join(_formula)
    expression = _formula + ' = ' + str(result)
    return expression, result


if __name__ == '__main__':
    start = time()
    with open('furmula.txt', 'w', encoding='utf-8') as file:
        for i in range(1000):
            expression, result = main()
            try:
                if result >= 0:
                    print(expression, file=file)
            except TypeError:
                pass

    print('total time: ', time() - start)
