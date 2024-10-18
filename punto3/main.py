import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser

# Función para calcular la transformada de Laplace de una expresión de forma dinámica
def laplace_transform(expression):
    # Eliminar espacios en blanco para facilitar la manipulación
    expression = expression.replace(" ", "")
    
    # Si la expresión es una suma, calculamos cada parte por separado
    if "+" in expression:
        parts = expression.split("+")
        return " + ".join([laplace_transform(part) for part in parts])
    
    # Regla general para cos(at)
    if "cos" in expression:
        a = extract_coefficient(expression, "cos")
        return f"s/(s^2 + {a}^2)"
    
    # Regla general para sin(at)
    elif "sin" in expression:
        a = extract_coefficient(expression, "sin")
        return f"{a}/(s^2 + {a}^2)"
    
    # Regla general para exp(-at)
    elif "exp" in expression:
        a = extract_coefficient(expression, "exp")
        return f"1/(s+{a})"
    
    # Regla general para t^n
    elif "t^" in expression:
        n = expression.split("^")[1]  # Extraer el exponente
        return f"{int(n)}!/s^{int(n)+1}"
    
    # Regla general para t
    elif "t" in expression and "^" not in expression:
        return "1/s^2"
    
    # Caso para constantes (1, 2, 3, etc.)
    elif expression.isdigit():
        return f"{expression}/s"
    
    # Si no se reconoce, devolver mensaje de error
    else:
        return "Transformada no disponible para esta expresión"

# Función auxiliar para extraer coeficientes de sin, cos, exp
def extract_coefficient(expression, func):
    # Ejemplo de expresión: sin(2t), exp(-3t), etc.
    if func in expression:
        inside_parentheses = expression.split(f"{func}(")[1].rstrip(")")
        coefficient = inside_parentheses.replace("t", "")
        # Si no hay coeficiente, se asume 1
        if coefficient == "" or coefficient == "-":
            return 1 if coefficient == "" else -1
        return coefficient
    return 1

# Función principal para procesar la entrada
def main(expression):
    # Generar un input stream a partir de la expresión fija
    input_stream = InputStream(expression)
    
    # Procesar la expresión con ANTLR
    lexer = LaplaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceParser(stream)
    tree = parser.transform()

    # Obtener la expresión del árbol parseado
    expr = tree.getText()
    print(f"Calculando transformada de Laplace para: {expr}")
    
    # Llamar a la función para calcular la transformada
    result = laplace_transform(expr)
    print(f"Resultado: {result}")

if __name__ == '__main__':
    # Expresión fija que vamos a analizar (puedes cambiarla)
    expression = "L(t^2 + exp(-t))"
    main(expression)
