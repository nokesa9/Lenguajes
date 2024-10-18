import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

# Funciones de ejemplo que vamos a usar en MAP y FILTER
def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

# Clase visitor para evaluar los comandos MAP y FILTER
class MapFilterEvalVisitor(ParseTreeVisitor):
    def visitMapCommand(self, ctx):
        func_name = ctx.function().getText()
        iterable = self.visit(ctx.iterable())
        # Usamos map para aplicar la función a cada elemento
        result = list(map(self.get_function(func_name), iterable))
        return result  # ¡Retornamos el resultado correctamente!

    def visitFilterCommand(self, ctx):
        func_name = ctx.function().getText()
        iterable = self.visit(ctx.iterable())
        # Usamos filter para aplicar la condición a cada elemento
        result = list(filter(self.get_function(func_name), iterable))
        return result  # ¡Retornamos el resultado correctamente!

    def visitList(self, ctx):
        return [int(element.getText()) for element in ctx.elements().element()]

    def visitTuple(self, ctx):
        return tuple([int(element.getText()) for element in ctx.elements().element()])

    # Método auxiliar para obtener la función por su nombre
    def get_function(self, func_name):
        if func_name == 'square':
            return square
        elif func_name == 'is_even':
            return is_even
        else:
            raise Exception(f"Function '{func_name}' no está definida")

# Función principal para procesar la entrada
def main(expression):
    input_stream = InputStream(expression)
    
    # Procesar la expresión con ANTLR
    lexer = MapFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.command()

    # Evaluar la expresión usando el visitor
    visitor = MapFilterEvalVisitor()
    result = visitor.visit(tree)  # ¡Evaluamos la expresión y obtenemos el resultado!
    print(f"Resultado: {result}")

if __name__ == '__main__':
    # Expresión que vamos a analizar
    expression = "FILTER(is_even, [1, 3, 4, 6, 8, 11, 14])"

    main(expression)
