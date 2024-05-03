grammar exprs;

root : expr             // l'etiqueta ja és root
     | instr
     ;

expr : <assoc=right> expr'^' expr   # potencia
     | expr ('*' | '/') expr   # muldiv
     | expr ('+' | '-') expr   # sumaresta
     | NUM             # numero
     | VAR     #variable
     ;


instr: VAR ':=' expr #assignacio
     | WRITE expr #escriu
     ;

WRITE : 'write' ;
VAR : [a-z]+ ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip;