#!/usr/bin/awk -f

# Función para verificar si un número es primo
function es_primo(n) {
    if (n < 2) return 0;  # Los números menores que 2 no son primos
    for (i = 2; i <= int(sqrt(n)); i++) {
        if (n % i == 0) return 0;  # Si n es divisible por cualquier número que no sea 1 o sí mismo, no es primo
    }
    return 1;  # Si no se encontró ningún divisor, es primo
}

# Para cada número en el archivo
{
    if (es_primo($1)) {
        print $1 " es primo";
    }
}
