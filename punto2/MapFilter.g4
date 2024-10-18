grammar MapFilter;

// Regla principal: aplicar MAP o FILTER
command : 'MAP' '(' function ',' iterable ')'   # MapCommand
        | 'FILTER' '(' function ',' iterable ')' # FilterCommand
        ;

// Definir un iterable como una lista o una tupla
iterable : list | tuple ;
list     : '[' elements ']' ;
tuple    : '(' elements ')' ;
elements : element (',' element)* ;
element  : INT ;

// Definir una función que opera sobre los elementos
function : ID ;

// Tokens para enteros y el nombre de la función
INT : [0-9]+ ;
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
WS  : [ \t\r\n]+ -> skip ;


