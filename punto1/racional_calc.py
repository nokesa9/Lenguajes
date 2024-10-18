import sys
from antlr4 import *
from RacionalLexer import RacionalLexer
from RacionalParser import RacionalParser
from RacionalVisitor import RacionalVisitor  # Usar el visitor generado por ANTLR
from fractions import Fraction

# Clase visitor que evalúa la expresión de fracciones
class RacionalEvalVisitor(RacionalVisitor):
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitFractionExpr(self, ctx):
        numerator = int(ctx.fraction().INT(0).getText())
        denominator = int(ctx.fraction().INT(1).getText())
        return Fraction(numerator, denominator)

# Función principal para procesar la entrada
def main(expression):
    input_stream = InputStream(expression)
    
    # Procesar la expresión con ANTLR
    lexer = RacionalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RacionalParser(stream)
    tree = parser.expr()

    # Evaluar la expresión usando el visitor
    visitor = RacionalEvalVisitor()
    result = visitor.visit(tree)
    print(f"Resultado: {result}")

if __name__ == '__main__':
    # Expresión que vamos a analizar
    expression = "(5/6 - 1/3) * 4/7"

    main(expression)
