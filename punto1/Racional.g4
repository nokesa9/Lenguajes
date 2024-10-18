grammar Racional;

// Regla principal: permite hacer operaciones con fracciones
expr   : expr op=('*'|'/') expr         # MulDiv
       | expr op=('+'|'-') expr         # AddSub
       | '(' expr ')'                   # Parens
       | fraction                       # FractionExpr
       ;

// Definir una fracción como dos números separados por '/'
fraction : INT '/' INT ;

// Token para enteros
INT : [0-9]+ ;

// Omitir espacios en blanco
WS : [ \t\r\n]+ -> skip ;
