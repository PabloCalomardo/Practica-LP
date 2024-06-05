grammar exprs;

root : expr             // l'etiqueta ja és root
     ;

expr: lambdaExpr    #ExpresioLambda
    | infixExpr     #Operacio
    | NUMBER        #numero
    | ID            #variable
    ;

lambdaExpr: '\\' ID '->' expr;

infixExpr: 
      (MULT | DIV | '(' MULT ')' | '(' DIV ')') expr expr    #multiplicaciodivisio
     | (PLUS | MINUS | '(' PLUS ')' | '(' MINUS ')') expr expr     #sumaresta 
    ;

NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip; // Ignora espais en blanc

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';