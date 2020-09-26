# 四则运算生成器(Beta)

## 实现的功能(Python 实现)

- 生成带括号的四则运算表达式
- 支持整数和真分数运算
- 有单元测试模块

## 文件模块

```
# 主函数
- main.py
    |__def makeFormula()
    |__def addBrackets()
    |__def solvingPostfixExpression()
    |__def getPostfixExpression()
    |__def doMath()

# 测试函数
- mainTest.py
    |__class MyTestCase()
        |__def test_solvingPostfixExpression_valid()
        |__def test_solvingPostfixExpression_invalid()
        |__def test_getPostfixExpression()

# 表达式文件
- formular.txt
```

[博客地址](https://www.cnblogs.com/justlikecode/p/13703205.html)