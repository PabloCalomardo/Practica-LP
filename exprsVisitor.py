# Generated from exprs.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#expressio.
    def visitExpressio(self, ctx:exprsParser.ExpressioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#ExpresioLambda.
    def visitExpresioLambda(self, ctx:exprsParser.ExpresioLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#Operacioincompleta.
    def visitOperacioincompleta(self, ctx:exprsParser.OperacioincompletaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#Operacio.
    def visitOperacio(self, ctx:exprsParser.OperacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#funcion.
    def visitFuncion(self, ctx:exprsParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#num.
    def visitNum(self, ctx:exprsParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#var.
    def visitVar(self, ctx:exprsParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#normalassig.
    def visitNormalassig(self, ctx:exprsParser.NormalassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#operassig.
    def visitOperassig(self, ctx:exprsParser.OperassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#cap.
    def visitCap(self, ctx:exprsParser.CapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#caprec.
    def visitCaprec(self, ctx:exprsParser.CaprecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#nassig.
    def visitNassig(self, ctx:exprsParser.NassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#opassig.
    def visitOpassig(self, ctx:exprsParser.OpassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#lambdafunc.
    def visitLambdafunc(self, ctx:exprsParser.LambdafuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#operaciobinaria.
    def visitOperaciobinaria(self, ctx:exprsParser.OperaciobinariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#operaciounaria.
    def visitOperaciounaria(self, ctx:exprsParser.OperaciounariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#operador.
    def visitOperador(self, ctx:exprsParser.OperadorContext):
        return self.visitChildren(ctx)



del exprsParser