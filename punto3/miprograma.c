#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1000

// Función para contar cuántas veces aparece la palabra clave en una línea
int count_occurrences(char *line, const char *word) {
    int count = 0;
    char *pos = line;
    int word_len = strlen(word);

    // Buscar todas las apariciones de la palabra clave en la línea
    while ((pos = strstr(pos, word)) != NULL) {
        count++;
        pos += word_len;  // Mover el puntero después de la palabra clave
    }

    return count;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo> <palabra_clave>\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    char *word = argv[2];
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error: No se puede abrir el archivo %s\n", filename);
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    int total_count = 0;

    // Leer cada línea del archivo y contar las ocurrencias de la palabra clave
    while (fgets(line, sizeof(line), file)) {
        total_count += count_occurrences(line, word);
    }

    fclose(file);

    // Imprimir el resultado
    printf("La palabra '%s' aparece %d veces en el archivo.\n", word, total_count);

    return 0;
}
