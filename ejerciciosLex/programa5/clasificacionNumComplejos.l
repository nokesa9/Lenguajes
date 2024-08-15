%{
#include <stdio.h>
#include <math.h>
%}

%%

[+-]?[0-9]+(\.[0-9]+)?[+-][0-9]+(\.[0-9]+)?[iI]  { printf("Número Complejo (Forma Rectangular): %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?[iI]                        { printf("Número Imaginario: %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?                            { printf("Número Real: %s\n", yytext); }
[+-]?[0-9]+(\.[0-9]+)?e[+-]?[0-9]+                { printf("Número Complejo (Forma Polar): %s\n", yytext); }
[ \t\n]+                                         { /* Ignorar espacios, tabulaciones y saltos de línea */ }
.                                                { printf("Token no reconocido: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
