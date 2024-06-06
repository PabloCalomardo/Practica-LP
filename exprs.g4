grammar exprs;

root : expr EOF            // l'etiqueta ja és root
     ;

expr: lambdaExpr    #ExpresioLambda
    | infixExpr     #Operacioincompleta
    | infixExprComp     #Operacio
    | '(' lambdaExpr ')' NUMBER     #funcion
    | expr2         #numovar
    ;

expr2: NUMBER       #numero
    | ID            #variable
    ;


lambdaExpr: '\\' ID '->' infixExprComp    #lambdafunc
    ;

infixExprComp: infixExpr expr2 #operaciobinaria
    ;

infixExpr: '(' operador ')' expr2     #operaciounaria
    ;

NUMBER: [0-9]+;
ID: [a-z]+;
WS: [ \n]+ -> skip; // Ignora espais en blanc

operador : PLUS | MINUS | MULT | DIV ;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';