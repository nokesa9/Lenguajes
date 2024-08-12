#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "afd.h"

void leer_configuracion(char *nombre_archivo, DFA *dfa) {
    FILE *archivo = fopen(nombre_archivo, "r");
    if (archivo == NULL) {
        printf("No se puede abrir el archivo de configuración.\n");
        exit(1);
    }

    // Leer el conjunto de estados
    fscanf(archivo, "%s", dfa->estados[0]);
    dfa->num_estados = 0;
    char *token = strtok(dfa->estados[0], ",");
    while (token != NULL) {
        strcpy(dfa->estados[dfa->num_estados++], token);
        token = strtok(NULL, ",");
    }

    // Leer el alfabeto
    fscanf(archivo, "%s", dfa->alfabeto);
    dfa->num_simbolos = strlen(dfa->alfabeto);

    // Leer el estado inicial
    fscanf(archivo, "%s", dfa->estado_inicial);

    // Leer los estados de aceptación
    fscanf(archivo, "%s", dfa->estados_aceptacion[0]);
    dfa->num_estados_aceptacion = 0;
    token = strtok(dfa->estados_aceptacion[0], ",");
    while (token != NULL) {
        strcpy(dfa->estados_aceptacion[dfa->num_estados_aceptacion++], token);
        token = strtok(NULL, ",");
    }

    // Leer las transiciones
    dfa->num_transiciones = 0;
    char linea[100];
    while (fscanf(archivo, "%s", linea) != EOF) {
        token = strtok(linea, ",");
        strcpy(dfa->transiciones[dfa->num_transiciones].estado_actual, token);
        token = strtok(NULL, ",");
        dfa->transiciones[dfa->num_transiciones].simbolo = token[0];
        token = strtok(NULL, ",");
        strcpy(dfa->transiciones[dfa->num_transiciones].estado_siguiente, token);

        dfa->num_transiciones++;
    }

    fclose(archivo);
}

int es_estado_aceptacion(DFA *dfa, char *estado) {
    for (int i = 0; i < dfa->num_estados_aceptacion; i++) {
        if (strcmp(estado, dfa->estados_aceptacion[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

int procesar_cadena(DFA *dfa, char *cadena) {
    char estado_actual[10];
    strcpy(estado_actual, dfa->estado_inicial);

    for (int i = 0; i < strlen(cadena); i++) {
        char simbolo = cadena[i];
        int transicion_encontrada = 0;

        // Verificar si el símbolo pertenece al alfabeto
        int simbolo_valido = 0;
        for (int j = 0; j < dfa->num_simbolos; j++) {
            if (simbolo == dfa->alfabeto[j]) {
                simbolo_valido = 1;
                break;
            }
        }
        if (!simbolo_valido) {
            printf("Resultado: la cadena fue rechazada (símbolo '%c' no pertenece al alfabeto).\n", simbolo);
            return 0;
        }

        // Buscar la transición correspondiente
        for (int j = 0; j < dfa->num_transiciones; j++) {
            if (strcmp(estado_actual, dfa->transiciones[j].estado_actual) == 0 && simbolo == dfa->transiciones[j].simbolo) {
                strcpy(estado_actual, dfa->transiciones[j].estado_siguiente);
                transicion_encontrada = 1;
                break;
            }
        }

        if (!transicion_encontrada) {
            printf("Resultado: la cadena fue rechazada (no hay transición desde el estado '%s' con el símbolo '%c').\n", estado_actual, simbolo);
            return 0;
        }
    }

    if (es_estado_aceptacion(dfa, estado_actual)) {
        printf("Resultado: la cadena fue aceptada.\n");
        return 1;
    } else {
        printf("Resultado: la cadena fue rechazada (terminó en el estado '%s', que no es de aceptación).\n", estado_actual);
        return 0;
    }
}

