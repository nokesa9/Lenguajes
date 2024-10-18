grammar Laplace;

transform : 'L(' expr ')' ;

expr : expr ('+'|'-') expr
     | expr ('*'|'/') expr
     | expr '^' expr          // Manejar el operador de potencia
     | '-' expr               // Manejar el signo negativo
     | 'exp' '(' expr ')'
     | 'sin' '(' expr ')'
     | 'cos' '(' expr ')'
     | NUMBER 't'             // Manejar coeficientes como 2t
     | 't'
     | NUMBER ;

NUMBER : '-'? [0-9]+ ;   // Permitir números negativos
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
WS     : [ \t\r\n]+ -> skip ;
