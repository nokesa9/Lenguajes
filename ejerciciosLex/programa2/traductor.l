%{
#include <stdio.h>
#include <string.h>

void traducir(const char* esp, const char* ing);
%}

%%

comida          { traducir("comida", "food"); }
almuerzo        { traducir("almuerzo", "lunch"); }
pelicula        { traducir("pelicula", "movie"); }
carro           { traducir("carro", "car"); }
flor            { traducir("flor", "flower"); }
celular         { traducir("celular", "cellphone"); }
barco           { traducir("barco", "boat"); }
llave           { traducir("llave", "key"); }
casa            { traducir("casa", "house"); }
jugar           { traducir("jugar", "play"); }
dado            { traducir("dado", "dice"); }
uña             { traducir("uña", "nail"); }
moto            { traducir("moto", "motorcycle"); }
pelota          { traducir("pelota", "ball"); }
numero          { traducir("número", "number"); }

comidas         { traducir("comidas", "foods"); }
almuerzos       { traducir("almuerzos", "lunches"); }
peliculas       { traducir("peliculas", "movies"); }
carros          { traducir("carros", "cars"); }
flores          { traducir("flores", "flowers"); }
celulares       { traducir("celulares", "cellphones"); }
barcos          { traducir("barcos", "boats"); }
llaves          { traducir("llaves", "keys"); }
casas           { traducir("casas", "houses"); }
jugares         { traducir("jugares", "plays"); }
dados           { traducir("dados", "dice"); }
uñas            { traducir("uñas", "nails"); }
motos           { traducir("motos", "motorcycles"); }
pelotas         { traducir("pelotas", "balls"); }
numeros         { traducir("números", "numbers"); }

food            { traducir("comida", "food"); }
lunch           { traducir("almuerzo", "lunch"); }
movie           { traducir("pelicula", "movie"); }
car             { traducir("carro", "car"); }
flower          { traducir("flor", "flower"); }
cellphone       { traducir("celular", "cellphone"); }
boat            { traducir("barco", "boat"); }
key             { traducir("llave", "key"); }
house           { traducir("casa", "house"); }
play            { traducir("jugar", "play"); }
dice            { traducir("dado", "dice"); }
nail            { traducir("uña", "nail"); }
motorcycle      { traducir("moto", "motorcycle"); }
ball            { traducir("pelota", "ball"); }
number          { traducir("número", "number"); }

foods           { traducir("comidas", "foods"); }
lunches         { traducir("almuerzos", "lunches"); }
movies          { traducir("peliculas", "movies"); }
cars            { traducir("carros", "cars"); }
flowers         { traducir("flores", "flowers"); }
cellphones      { traducir("celulares", "cellphones"); }
boats           { traducir("barcos", "boats"); }
keys            { traducir("llaves", "keys"); }
houses          { traducir("casas", "houses"); }
plays           { traducir("jugares", "plays"); }
dice            { traducir("dados", "dice"); }
nails           { traducir("uñas", "nails"); }
motorcycles     { traducir("motos", "motorcycles"); }
balls           { traducir("pelotas", "balls"); }
numbers         { traducir("números", "numbers"); }

%%

void traducir(const char* esp, const char* ing) {
    if (strcmp(yytext, esp) == 0) {
        printf("%s\n", ing);
    } else {
        printf("%s\n", esp);
    }
}

int main() {
    yylex();
    return 0;
}
