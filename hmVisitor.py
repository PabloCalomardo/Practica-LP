# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#expressio.
    def visitExpressio(self, ctx:hmParser.ExpressioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#assignacio.
    def visitAssignacio(self, ctx:hmParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#ExpresioLambda.
    def visitExpresioLambda(self, ctx:hmParser.ExpresioLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#Operacioincompleta.
    def visitOperacioincompleta(self, ctx:hmParser.OperacioincompletaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#Operacio.
    def visitOperacio(self, ctx:hmParser.OperacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#funcion.
    def visitFuncion(self, ctx:hmParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#num.
    def visitNum(self, ctx:hmParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#var.
    def visitVar(self, ctx:hmParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#variable.
    def visitVariable(self, ctx:hmParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#normalassig.
    def visitNormalassig(self, ctx:hmParser.NormalassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operassig.
    def visitOperassig(self, ctx:hmParser.OperassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#cap.
    def visitCap(self, ctx:hmParser.CapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#caprec.
    def visitCaprec(self, ctx:hmParser.CaprecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#nassig.
    def visitNassig(self, ctx:hmParser.NassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#opassig.
    def visitOpassig(self, ctx:hmParser.OpassigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#lambdafunc.
    def visitLambdafunc(self, ctx:hmParser.LambdafuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operaciobinaria.
    def visitOperaciobinaria(self, ctx:hmParser.OperaciobinariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operaciounaria.
    def visitOperaciounaria(self, ctx:hmParser.OperaciounariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operador.
    def visitOperador(self, ctx:hmParser.OperadorContext):
        return self.visitChildren(ctx)



del hmParser