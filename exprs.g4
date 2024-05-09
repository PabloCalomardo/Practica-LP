grammar exprs;

root : expr             // l'etiqueta ja és root
     | instr
     ;

expr : <assoc=right> expr '^' expr   # potencia
     | expr ('*' | '/') expr   # muldiv
     | expr ('+' | '-') expr   # sumaresta
     | NUM             # numero
     | VAR     #variable
     ;

cond : VAR '=' expr #igual
     | VAR '<>' expr #diferent
     | VAR '<=' expr #menorigual
     | VAR '>=' expr #mesgranigual
     | VAR '<' expr #menor
     | VAR '>' expr #major
     ;

instr2 : instr instr2 
     | instr   
     ;

instr: VAR ':=' expr #assignacio
     | WRITE expr #escriu
     | IF cond THEN instr2 END #if
     | WHILE cond DO instr2 END #while
     ;

WRITE : 'write' ;
IF : 'if' ;
THEN : 'then' ;
END : 'end' ;
WHILE : 'while';
DO : 'do';
VAR : [a-z]+ ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip;