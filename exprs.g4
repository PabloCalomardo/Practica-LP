grammar exprs;

root : expr             // l'etiqueta ja és root
     ;

expr :
     | expr '*' expr   # multiplicacio
     | expr '/' expr   # divisio
     | <assoc=right> expr'^' expr   # potencia     
     |expr '+' expr   # suma
     | expr '-' expr   # resta


     | NUM             # numero
     ;

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip;