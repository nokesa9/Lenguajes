#ifndef AFD_H
#define AFD_H

// Transiciones
typedef struct {
    char estado_actual[10];
    char simbolo;
    char estado_siguiente[10];
} Transicion;

// Estructura automata
typedef struct {
    char estados[10][10];
    int num_estados;
    char alfabeto[10];
    int num_simbolos;
    char estado_inicial[10];
    char estados_aceptacion[10][10];
    int num_estados_aceptacion;
    Transicion transiciones[100];
    int num_transiciones;
} DFA;

// Funcion para leer el archivo de configuracion
void leer_configuracion(char *nombre_archivo, DFA *dfa);

// Funcion para verificar si un estado es de aceptacion
int es_estado_aceptacion(DFA *dfa, char *estado);

// Funcion para procesar la cadena de entrada
int procesar_cadena(DFA *dfa, char *cadena);


#endif
