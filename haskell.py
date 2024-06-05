from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0
        taulaSimbols = {}

    def visitExpresioLambda(self, ctx):
        [operador, expressio1, expressio2] = list(ctx.getChildren())
        return self.visitChildren(ctx)
        

        # Visit a parse tree produced by exprsParser#Operacio.
    def visitOperacio(self, ctx:exprsParser.OperacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        [numero] = list(ctx.getChildren())
        print(numero)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        [var] = list(ctx.getChildren())
        print(var)


    # Visit a parse tree produced by exprsParser#multiplicaciodivisio.
    def visitMultiplicaciodivisio(self, ctx:exprsParser.MultiplicaciodivisioContext):
        [operador, expressio1, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '*'):
            print('  ' *  self.nivell + '*')
        else:
            print('  ' *  self.nivell + '/')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1


    # Visit a parse tree produced by exprsParser#sumaresta.
    def visitSumaresta(self, ctx:exprsParser.SumarestaContext):
        [operador, expressio1, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '+'):
            print('  ' *  self.nivell + '+')
        else:
            print('  ' *  self.nivell + '-')
        
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1