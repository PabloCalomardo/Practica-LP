# Generated from exprs.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#ExpresioLambda.
    def visitExpresioLambda(self, ctx:exprsParser.ExpresioLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#Operacio.
    def visitOperacio(self, ctx:exprsParser.OperacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:exprsParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#multiplicaciodivisio.
    def visitMultiplicaciodivisio(self, ctx:exprsParser.MultiplicaciodivisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#sumaresta.
    def visitSumaresta(self, ctx:exprsParser.SumarestaContext):
        return self.visitChildren(ctx)



del exprsParser