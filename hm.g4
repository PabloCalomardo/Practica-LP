grammar hm;

root: expr EOF      #expressio
    | assig EOF     #assignacio 
    ;

expr: lambdaExpr    #ExpresioLambda
    | infixExpr     #Operacioincompleta
    | infixExprComp     #Operacio
    | '(' lambdaExpr ')' expr2     #funcion
    | expr2         #num
    | expr3         #var
    ;

expr2: NUMBER       #numero
    ;

expr3: ID           #variable
    ;

assig: normAssig    #normalassig
    | opAssig       #operassig
    ;

expr4: CAP              #cap
    | CAP '->' expr4    #caprec
    ;

normAssig: NUMBER '::' CAP     #nassig
    ;

opAssig: '(' operador ')' '::' CAP '->' expr4    #opassig
    ;

lambdaExpr: '\\' expr3 '->' infixExprComp    #lambdafunc
    ;

infixExprComp: infixExpr (expr2|expr3) #operaciobinaria
    ;

infixExpr: '(' operador ')' (expr2|expr3)     #operaciounaria
    ;

operador : PLUS | MINUS | MULT | DIV ;

NUMBER: [0-9]+;
ID: [a-z]+;
CAP: [A-Z]+;
WS: [ \n]+ -> skip; // Ignora espais en blanc

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';