from abc import ABC,abstractmethod


"""
    The Interpreter design pattern is used to define a grammar for a language and to provide an interpreter to evaluate sentences in that language. 
"""

#!AbstractExpression
class AbstractExpression:
    @staticmethod
    def interpret():
        pass


#!Number
class Number(AbstractExpression):
    def __init__(self, value):
        self.value = float(value)

    def interpret(self):
        return self.value


#!AlgebraExpression
class AlgebraExpression(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


#!Add
class Add(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


#!Subtract
class Subtract(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() - self.right.interpret()


#!Multiply
class Multiply(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


#!Divide
class Divide(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() / self.right.interpret()


#__name__ == __main__
if __name__ == '__main__':
    target = "3 + 5 - 2 * 7 / 5 + 11"

    tokens = target.split(' ')
    expression = []

    for i in range(len(tokens)):
        if i == 0:
            expression.append(Number(tokens[i]))
        elif tokens[i] == "+":
            expression.append(Add(expression.pop(), Number(tokens[i+1])))
        elif tokens[i] == "-":
            expression.append(Subtract(expression.pop(),Number(tokens[i+1])))
        elif tokens[i] == "*":
            expression.append(Multiply(expression.pop(),Number(tokens[i+1])))
        elif tokens[i] == "/":
            expression.append(Divide(expression.pop(),Number(tokens[i+1])))

    result = expression.pop().interpret()
    print('Result ', result)

