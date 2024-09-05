import re

# Definir las expresiones regulares y sus tokens correspondientes
patterns = [
    (r'^\+$', 'SUMA'),
    (r'^\+\+$', 'INCREMENTO'),
    (r'^[0-9]+$', 'NÚMERO ENTERO'),
    (r'^[0-9]+\.[0-9]+$', 'NÚMERO DECIMAL')
]

def match_token(expression):
    for pattern, token in patterns:
        if re.match(pattern, expression):
            return token
    return "EXPRESIÓN NO VÁLIDA"

if __name__ == "__main__":
    # Recibir la expresión desde la consola
    expression = input("Introduce una expresión: ")
    
    # Obtener el token correspondiente
    token = match_token(expression)
    
    # Imprimir el token
    print(token)
