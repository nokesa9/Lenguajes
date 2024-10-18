# Para correr los programas
1. Instalar ANTLR si no esta instalado
    - brew install antlr # Para macOS
    - sudo apt install antlr4 # Para Linux (Debian-based)
      
2. Asegurarse de tener Python 3 instalado
    - python3 --version
      
3. Generar los archivos Python a partir de las gramáticas usando ANTLR
    - antlr4 -Dlanguage=Python3 -visitor NombreDelArchivo.g4
      
4. Instalar la librería antlr4-python3-runtime en Python si no está instalada
    - pip install antlr4-python3-runtime

5. Activar entorno virtual

## Punto 1
1. Generar los archivos de Python desde la gramática Racional.g4
    - antlr4 -Dlanguage=Python3 -visitor Racional.g4
      
2. Ejecutar el script racional_calc.py con la expresión deseada
    - python3 racional_calc.py
      
3. Ejemplo de expresión para probar. Se puede modificar si se desea
    - expression = "(1/3 + 2/3)"

## Punto 2
1. Generar los archivos de Python desde la gramática MapFilter.g4
    - antlr4 -Dlanguage=Python3 -visitor MapFilter.g4
   
3. Ejecutar el script map_filter.py con la expresión deseada
    -  python3 map_filter.py

5. Ejemplo de expresión para MAP. Se puede modificar
    - expression = "MAP(square, [1, 2, 3, 4])"

7. Ejemplo de expresión para FILTER. Se puede modificar
    - expression = "FILTER(is_even, [1, 3, 4, 6, 8, 11, 14])"

## Punto3
1. Generar los archivos de Python desde la gramática Laplace.g4
    - antlr4 -Dlanguage=Python3 -visitor Laplace.g4
      
2. Ejecutar el script laplace_transform.py con la expresión deseada
    - python3 laplace_transform.py

3. Ejemplo de expresión. Se puede modificar
    - expression = "L(sin(t))"





