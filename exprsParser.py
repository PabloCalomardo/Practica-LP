# Generated from exprs.g4 by ANTLR 4.13.1
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
        4,1,11,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,2,
        1,2,3,2,31,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,8,11,45,0,14,1,0,0,0,
        2,26,1,0,0,0,4,30,1,0,0,0,6,32,1,0,0,0,8,37,1,0,0,0,10,40,1,0,0,
        0,12,45,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,27,3,
        6,3,0,18,27,3,10,5,0,19,27,3,8,4,0,20,21,5,1,0,0,21,22,3,6,3,0,22,
        23,5,2,0,0,23,24,5,5,0,0,24,27,1,0,0,0,25,27,3,4,2,0,26,17,1,0,0,
        0,26,18,1,0,0,0,26,19,1,0,0,0,26,20,1,0,0,0,26,25,1,0,0,0,27,3,1,
        0,0,0,28,31,5,5,0,0,29,31,5,6,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,
        5,1,0,0,0,32,33,5,3,0,0,33,34,5,6,0,0,34,35,5,4,0,0,35,36,3,8,4,
        0,36,7,1,0,0,0,37,38,3,10,5,0,38,39,3,4,2,0,39,9,1,0,0,0,40,41,5,
        1,0,0,41,42,3,12,6,0,42,43,5,2,0,0,43,44,3,4,2,0,44,11,1,0,0,0,45,
        46,7,0,0,0,46,13,1,0,0,0,2,26,30
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\'", "'->'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ID", "WS", "PLUS", "MINUS", 
                      "MULT", "DIV" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_expr2 = 2
    RULE_lambdaExpr = 3
    RULE_infixExprComp = 4
    RULE_infixExpr = 5
    RULE_operador = 6

    ruleNames =  [ "root", "expr", "expr2", "lambdaExpr", "infixExprComp", 
                   "infixExpr", "operador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    ID=6
    WS=7
    PLUS=8
    MINUS=9
    MULT=10
    DIV=11

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

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def EOF(self):
            return self.getToken(exprsParser.EOF, 0)

        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr()
            self.state = 15
            self.match(exprsParser.EOF)
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
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExprComp(self):
            return self.getTypedRuleContext(exprsParser.InfixExprCompContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacio" ):
                return visitor.visitOperacio(self)
            else:
                return visitor.visitChildren(self)


    class ExpresioLambdaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(exprsParser.LambdaExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresioLambda" ):
                return visitor.visitExpresioLambda(self)
            else:
                return visitor.visitChildren(self)


    class NumovarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(exprsParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumovar" ):
                return visitor.visitNumovar(self)
            else:
                return visitor.visitChildren(self)


    class FuncionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambdaExpr(self):
            return self.getTypedRuleContext(exprsParser.LambdaExprContext,0)

        def NUMBER(self):
            return self.getToken(exprsParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)


    class OperacioincompletaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExpr(self):
            return self.getTypedRuleContext(exprsParser.InfixExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacioincompleta" ):
                return visitor.visitOperacioincompleta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = exprsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = exprsParser.ExpresioLambdaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.lambdaExpr()
                pass

            elif la_ == 2:
                localctx = exprsParser.OperacioincompletaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.infixExpr()
                pass

            elif la_ == 3:
                localctx = exprsParser.OperacioContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.infixExprComp()
                pass

            elif la_ == 4:
                localctx = exprsParser.FuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(exprsParser.T__0)
                self.state = 21
                self.lambdaExpr()
                self.state = 22
                self.match(exprsParser.T__1)
                self.state = 23
                self.match(exprsParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = exprsParser.NumovarContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.expr2()
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
            return exprsParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(exprsParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self):

        localctx = exprsParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr2)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(exprsParser.NUMBER)
                pass
            elif token in [6]:
                localctx = exprsParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(exprsParser.ID)
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


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_lambdaExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LambdafuncContext(LambdaExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LambdaExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprsParser.ID, 0)
        def infixExprComp(self):
            return self.getTypedRuleContext(exprsParser.InfixExprCompContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdafunc" ):
                return visitor.visitLambdafunc(self)
            else:
                return visitor.visitChildren(self)



    def lambdaExpr(self):

        localctx = exprsParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lambdaExpr)
        try:
            localctx = exprsParser.LambdafuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(exprsParser.T__2)
            self.state = 33
            self.match(exprsParser.ID)
            self.state = 34
            self.match(exprsParser.T__3)
            self.state = 35
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
            return exprsParser.RULE_infixExprComp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperaciobinariaContext(InfixExprCompContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InfixExprCompContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def infixExpr(self):
            return self.getTypedRuleContext(exprsParser.InfixExprContext,0)

        def expr2(self):
            return self.getTypedRuleContext(exprsParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperaciobinaria" ):
                return visitor.visitOperaciobinaria(self)
            else:
                return visitor.visitChildren(self)



    def infixExprComp(self):

        localctx = exprsParser.InfixExprCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_infixExprComp)
        try:
            localctx = exprsParser.OperaciobinariaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.infixExpr()
            self.state = 38
            self.expr2()
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
            return exprsParser.RULE_infixExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperaciounariaContext(InfixExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InfixExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operador(self):
            return self.getTypedRuleContext(exprsParser.OperadorContext,0)

        def expr2(self):
            return self.getTypedRuleContext(exprsParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperaciounaria" ):
                return visitor.visitOperaciounaria(self)
            else:
                return visitor.visitChildren(self)



    def infixExpr(self):

        localctx = exprsParser.InfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_infixExpr)
        try:
            localctx = exprsParser.OperaciounariaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(exprsParser.T__0)
            self.state = 41
            self.operador()
            self.state = 42
            self.match(exprsParser.T__1)
            self.state = 43
            self.expr2()
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
            return self.getToken(exprsParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(exprsParser.MINUS, 0)

        def MULT(self):
            return self.getToken(exprsParser.MULT, 0)

        def DIV(self):
            return self.getToken(exprsParser.DIV, 0)

        def getRuleIndex(self):
            return exprsParser.RULE_operador

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = exprsParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
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





