%{
int num_lineas = 0;
int num_palabras = 0;
int num_caracteres = 0;
%}

%%

[a-zA-Z]+  { num_palabras++; num_caracteres += yyleng; }
[^a-zA-Z\n]+  { num_caracteres += yyleng; }
\n  { num_lineas++; num_caracteres++; }

%%

int main() {
    yylex();
    printf("Numero de lineas: %d\n", num_lineas + 1);
    printf("Numero de palabras: %d\n", num_palabras);
    printf("Numero de caracteres: %d\n", num_caracteres);
    return 0;
}
