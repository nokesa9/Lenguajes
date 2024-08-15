%{
#include <stdio.h>
%}

%%

[0-9]+(\.[0-9]+)?     { printf("Numero: %s\n", yytext); }
"+"                   { printf("Simbolo: Suma (+)\n"); }
"-"                   { printf("Simbolo: Resta (-)\n"); }
"*"                   { printf("Simbolo: Multiplicación (*)\n"); }
"/"                   { printf("Simbolo: División (/)\n"); }
"="                   { printf("Simbolo: Igual (=)\n"); }
"("                   { printf("Simbolo: Parentesis Izquierdo (()\n"); }
")"                   { printf("Simbolo: Parentesis Derecho ())\n"); }
[\n\t ]+              { /* Ignorar espacios en blanco, tabulaciones y saltos de linea */ }
.                     { printf("Carácter desconocido: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
