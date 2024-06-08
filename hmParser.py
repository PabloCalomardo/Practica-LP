# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,0,3,0,31,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,43,
        8,1,1,2,1,2,1,3,1,3,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,3,5,57,8,
        5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,3,9,79,8,9,1,10,1,10,1,10,1,10,1,10,3,10,86,8,
        10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,
        10,13,87,0,30,1,0,0,0,2,42,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,8,50,
        1,0,0,0,10,56,1,0,0,0,12,58,1,0,0,0,14,62,1,0,0,0,16,70,1,0,0,0,
        18,75,1,0,0,0,20,80,1,0,0,0,22,87,1,0,0,0,24,25,3,2,1,0,25,26,5,
        0,0,1,26,31,1,0,0,0,27,28,3,8,4,0,28,29,5,0,0,1,29,31,1,0,0,0,30,
        24,1,0,0,0,30,27,1,0,0,0,31,1,1,0,0,0,32,43,3,16,8,0,33,43,3,20,
        10,0,34,43,3,18,9,0,35,36,5,1,0,0,36,37,3,16,8,0,37,38,5,2,0,0,38,
        39,3,4,2,0,39,43,1,0,0,0,40,43,3,4,2,0,41,43,3,6,3,0,42,32,1,0,0,
        0,42,33,1,0,0,0,42,34,1,0,0,0,42,35,1,0,0,0,42,40,1,0,0,0,42,41,
        1,0,0,0,43,3,1,0,0,0,44,45,5,6,0,0,45,5,1,0,0,0,46,47,5,7,0,0,47,
        7,1,0,0,0,48,51,3,12,6,0,49,51,3,14,7,0,50,48,1,0,0,0,50,49,1,0,
        0,0,51,9,1,0,0,0,52,57,5,8,0,0,53,54,5,8,0,0,54,55,5,3,0,0,55,57,
        3,10,5,0,56,52,1,0,0,0,56,53,1,0,0,0,57,11,1,0,0,0,58,59,5,6,0,0,
        59,60,5,4,0,0,60,61,5,8,0,0,61,13,1,0,0,0,62,63,5,1,0,0,63,64,3,
        22,11,0,64,65,5,2,0,0,65,66,5,4,0,0,66,67,5,8,0,0,67,68,5,3,0,0,
        68,69,3,10,5,0,69,15,1,0,0,0,70,71,5,5,0,0,71,72,3,6,3,0,72,73,5,
        3,0,0,73,74,3,18,9,0,74,17,1,0,0,0,75,78,3,20,10,0,76,79,3,4,2,0,
        77,79,3,6,3,0,78,76,1,0,0,0,78,77,1,0,0,0,79,19,1,0,0,0,80,81,5,
        1,0,0,81,82,3,22,11,0,82,85,5,2,0,0,83,86,3,4,2,0,84,86,3,6,3,0,
        85,83,1,0,0,0,85,84,1,0,0,0,86,21,1,0,0,0,87,88,7,0,0,0,88,23,1,
        0,0,0,6,30,42,50,56,78,85
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'->'", "'::'", "'\\'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "ID", "CAP", "WS", 
                      "PLUS", "MINUS", "MULT", "DIV" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_expr2 = 2
    RULE_expr3 = 3
    RULE_assig = 4
    RULE_expr4 = 5
    RULE_normAssig = 6
    RULE_opAssig = 7
    RULE_lambdaExpr = 8
    RULE_infixExprComp = 9
    RULE_infixExpr = 10
    RULE_operador = 11

    ruleNames =  [ "root", "expr", "expr2", "expr3", "assig", "expr4", "normAssig", 
                   "opAssig", "lambdaExpr", "infixExprComp", "infixExpr", 
                   "operador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    ID=7
    CAP=8
    WS=9
    PLUS=10
    MINUS=11
    MULT=12
    DIV=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_root

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignacioContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assig(self):
            return self.getTypedRuleContext(hmParser.AssigContext,0)

        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)


    class ExpressioContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)

        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressio" ):
                return visitor.visitExpressio(self)
            else:
                return visitor.visitChildren(self)



    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = hmParser.ExpressioContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.expr()
                self.state = 25
                self.match(hmParser.EOF)
                pass

            elif la_ == 2:
                localctx = hmParser.AssignacioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.assig()
                self.state = 28
                self.match(hmParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExprComp(self):
            return self.getTypedRuleContext(hmParser.InfixExprCompContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacio" ):
                return visitor.visitOperacio(self)
            else:
                return visitor.visitChildren(self)


    class ExpresioLambdaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(hmParser.LambdaExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresioLambda" ):
                return visitor.visitExpresioLambda(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(hmParser.Expr3Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(hmParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class FuncionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(hmParser.LambdaExprContext,0)

        def expr2(self):
            return self.getTypedRuleContext(hmParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)


    class OperacioincompletaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExpr(self):
            return self.getTypedRuleContext(hmParser.InfixExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacioincompleta" ):
                return visitor.visitOperacioincompleta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = hmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = hmParser.ExpresioLambdaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.lambdaExpr()
                pass

            elif la_ == 2:
                localctx = hmParser.OperacioincompletaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.infixExpr()
                pass

            elif la_ == 3:
                localctx = hmParser.OperacioContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.infixExprComp()
                pass

            elif la_ == 4:
                localctx = hmParser.FuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(hmParser.T__0)
                self.state = 36
                self.lambdaExpr()
                self.state = 37
                self.match(hmParser.T__1)
                self.state = 38
                self.expr2()
                pass

            elif la_ == 5:
                localctx = hmParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.expr2()
                pass

            elif la_ == 6:
                localctx = hmParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 41
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(hmParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self):

        localctx = hmParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr2)
        try:
            localctx = hmParser.NumeroContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(hmParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self):

        localctx = hmParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr3)
        try:
            localctx = hmParser.VariableContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(hmParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_assig

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NormalassigContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def normAssig(self):
            return self.getTypedRuleContext(hmParser.NormAssigContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalassig" ):
                return visitor.visitNormalassig(self)
            else:
                return visitor.visitChildren(self)


    class OperassigContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def opAssig(self):
            return self.getTypedRuleContext(hmParser.OpAssigContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperassig" ):
                return visitor.visitOperassig(self)
            else:
                return visitor.visitChildren(self)



    def assig(self):

        localctx = hmParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assig)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = hmParser.NormalassigContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.normAssig()
                pass
            elif token in [1]:
                localctx = hmParser.OperassigContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.opAssig()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CapContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CAP(self):
            return self.getToken(hmParser.CAP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCap" ):
                return visitor.visitCap(self)
            else:
                return visitor.visitChildren(self)


    class CaprecContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CAP(self):
            return self.getToken(hmParser.CAP, 0)
        def expr4(self):
            return self.getTypedRuleContext(hmParser.Expr4Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaprec" ):
                return visitor.visitCaprec(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self):

        localctx = hmParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr4)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = hmParser.CapContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(hmParser.CAP)
                pass

            elif la_ == 2:
                localctx = hmParser.CaprecContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(hmParser.CAP)
                self.state = 54
                self.match(hmParser.T__2)
                self.state = 55
                self.expr4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormAssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_normAssig

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NassigContext(NormAssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.NormAssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(hmParser.NUMBER, 0)
        def CAP(self):
            return self.getToken(hmParser.CAP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNassig" ):
                return visitor.visitNassig(self)
            else:
                return visitor.visitChildren(self)



    def normAssig(self):

        localctx = hmParser.NormAssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_normAssig)
        try:
            localctx = hmParser.NassigContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(hmParser.NUMBER)
            self.state = 59
            self.match(hmParser.T__3)
            self.state = 60
            self.match(hmParser.CAP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_opAssig

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OpassigContext(OpAssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.OpAssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador(self):
            return self.getTypedRuleContext(hmParser.OperadorContext,0)

        def CAP(self):
            return self.getToken(hmParser.CAP, 0)
        def expr4(self):
            return self.getTypedRuleContext(hmParser.Expr4Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpassig" ):
                return visitor.visitOpassig(self)
            else:
                return visitor.visitChildren(self)



    def opAssig(self):

        localctx = hmParser.OpAssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opAssig)
        try:
            localctx = hmParser.OpassigContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(hmParser.T__0)
            self.state = 63
            self.operador()
            self.state = 64
            self.match(hmParser.T__1)
            self.state = 65
            self.match(hmParser.T__3)
            self.state = 66
            self.match(hmParser.CAP)
            self.state = 67
            self.match(hmParser.T__2)
            self.state = 68
            self.expr4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_lambdaExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LambdafuncContext(LambdaExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.LambdaExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(hmParser.Expr3Context,0)

        def infixExprComp(self):
            return self.getTypedRuleContext(hmParser.InfixExprCompContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdafunc" ):
                return visitor.visitLambdafunc(self)
            else:
                return visitor.visitChildren(self)



    def lambdaExpr(self):

        localctx = hmParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lambdaExpr)
        try:
            localctx = hmParser.LambdafuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(hmParser.T__4)
            self.state = 71
            self.expr3()
            self.state = 72
            self.match(hmParser.T__2)
            self.state = 73
            self.infixExprComp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InfixExprCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_infixExprComp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperaciobinariaContext(InfixExprCompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.InfixExprCompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExpr(self):
            return self.getTypedRuleContext(hmParser.InfixExprContext,0)

        def expr2(self):
            return self.getTypedRuleContext(hmParser.Expr2Context,0)

        def expr3(self):
            return self.getTypedRuleContext(hmParser.Expr3Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperaciobinaria" ):
                return visitor.visitOperaciobinaria(self)
            else:
                return visitor.visitChildren(self)



    def infixExprComp(self):

        localctx = hmParser.InfixExprCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_infixExprComp)
        try:
            localctx = hmParser.OperaciobinariaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.infixExpr()
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 76
                self.expr2()
                pass
            elif token in [7]:
                self.state = 77
                self.expr3()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_infixExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperaciounariaContext(InfixExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.InfixExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador(self):
            return self.getTypedRuleContext(hmParser.OperadorContext,0)

        def expr2(self):
            return self.getTypedRuleContext(hmParser.Expr2Context,0)

        def expr3(self):
            return self.getTypedRuleContext(hmParser.Expr3Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperaciounaria" ):
                return visitor.visitOperaciounaria(self)
            else:
                return visitor.visitChildren(self)



    def infixExpr(self):

        localctx = hmParser.InfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_infixExpr)
        try:
            localctx = hmParser.OperaciounariaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(hmParser.T__0)
            self.state = 81
            self.operador()
            self.state = 82
            self.match(hmParser.T__1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 83
                self.expr2()
                pass
            elif token in [7]:
                self.state = 84
                self.expr3()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(hmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(hmParser.MINUS, 0)

        def MULT(self):
            return self.getToken(hmParser.MULT, 0)

        def DIV(self):
            return self.getToken(hmParser.DIV, 0)

        def getRuleIndex(self):
            return hmParser.RULE_operador

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = hmParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





