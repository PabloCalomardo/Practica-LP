grammar exprs;

root : expr EOF            // l'etiqueta ja és root
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


lambdaExpr: '\\' expr3 '->' infixExprComp    #lambdafunc
    ;

infixExprComp: infixExpr (expr2|expr3) #operaciobinaria
    ;

infixExpr: '(' operador ')' (expr2|expr3)     #operaciounaria
    ;

operador : PLUS | MINUS | MULT | DIV ;

NUMBER: [0-9]+;
ID: [a-z]+;
WS: [ \n]+ -> skip; // Ignora espais en blanc

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';