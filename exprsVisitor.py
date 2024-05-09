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


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#sumaresta.
    def visitSumaresta(self, ctx:exprsParser.SumarestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#muldiv.
    def visitMuldiv(self, ctx:exprsParser.MuldivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#igual.
    def visitIgual(self, ctx:exprsParser.IgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#diferent.
    def visitDiferent(self, ctx:exprsParser.DiferentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#menorigual.
    def visitMenorigual(self, ctx:exprsParser.MenorigualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#mesgranigual.
    def visitMesgranigual(self, ctx:exprsParser.MesgranigualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#menor.
    def visitMenor(self, ctx:exprsParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#major.
    def visitMajor(self, ctx:exprsParser.MajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#instr2.
    def visitInstr2(self, ctx:exprsParser.Instr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#escriu.
    def visitEscriu(self, ctx:exprsParser.EscriuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#if.
    def visitIf(self, ctx:exprsParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#while.
    def visitWhile(self, ctx:exprsParser.WhileContext):
        return self.visitChildren(ctx)



del exprsParser