# Integrante

Sara Lucia Villanueva Arcila

Una vez descargado el codigo e ingresado a la carpeta por medio de la terminal:

Para todos los programas, primero, ingresar por consola lo siguiente luego de estar en la carpeta correcta:

1. flex nombreArchivo.l
2. gcc lex.yy.c -o nombreArchivoEjecutable -lfl

Luego seguir los pasos dependiendo del programa a ejecutar

## Programa 1

* En el archivoTexto se encuentra todos los caracteres, lineas y palabras que va a analizar el programa

1. /.nombreArchivoEjecutable < archivoTexto

## Programa 2

Palabras usadas [comida, almuerzo, pelicula, carro, flor, celular, barco, llave,  casa, jugar, dado, uña, moto, pelota, número]

1. echo "palabras a traducir" | ./nombreArchivoEjecutable

## Programa 3

1. echo "caracteres simbolicos y numericos separados por un espacio" | ./nombreArchivoEjecutable

## Programa 4

1. echo "tokens separados por un espacio" | ./nombreArchivoEjecutable

## Programa 5

1. echo "numeros complejos separados por un espacio" | ./nombreArchivoEjecutable
