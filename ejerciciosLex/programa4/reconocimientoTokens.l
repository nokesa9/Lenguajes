%{
#include <stdio.h>
%}

%%

[0-9]+(\.[0-9]+)?    { printf("NUMBER: %s\n", yytext); }
"+"                  { printf("ADD: %s\n", yytext); }
"-"                  { printf("SUB: %s\n", yytext); }
"*"                  { printf("MUL: %s\n", yytext); }
"/"                  { printf("DIV: %s\n", yytext); }
"abs"                { printf("ABS: %s\n", yytext); }
[\n]                 { printf("EOL: End of Line\n"); }
[ \t]+               { /* Ignorar espacios en blanco y tabulaciones */ }
.                    { printf("Token no reconocido: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
