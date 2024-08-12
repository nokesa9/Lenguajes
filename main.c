#include <stdio.h>
#include "afd.h"

int main() {
    DFA dfa;
    char nombre_archivo[100];
    char cadena[100];

    printf("Ingrese el nombre del archivo de configuración: ");
    scanf("%s", nombre_archivo);

    leer_configuracion(nombre_archivo, &dfa);

    printf("Ingrese la cadena de entrada: ");
    scanf("%s", cadena);

    procesar_cadena(&dfa, cadena);

    return 0;
}
