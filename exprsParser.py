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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,15,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,30,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,43,8,
        3,1,3,1,3,1,3,3,3,48,8,3,1,3,0,0,4,0,2,4,6,0,0,55,0,8,1,0,0,0,2,
        14,1,0,0,0,4,16,1,0,0,0,6,47,1,0,0,0,8,9,3,2,1,0,9,1,1,0,0,0,10,
        15,3,4,2,0,11,15,3,6,3,0,12,15,5,5,0,0,13,15,5,6,0,0,14,10,1,0,0,
        0,14,11,1,0,0,0,14,12,1,0,0,0,14,13,1,0,0,0,15,3,1,0,0,0,16,17,5,
        1,0,0,17,18,5,6,0,0,18,19,5,2,0,0,19,20,3,2,1,0,20,5,1,0,0,0,21,
        30,5,10,0,0,22,30,5,11,0,0,23,24,5,3,0,0,24,25,5,10,0,0,25,30,5,
        4,0,0,26,27,5,3,0,0,27,28,5,11,0,0,28,30,5,4,0,0,29,21,1,0,0,0,29,
        22,1,0,0,0,29,23,1,0,0,0,29,26,1,0,0,0,30,31,1,0,0,0,31,32,3,2,1,
        0,32,33,3,2,1,0,33,48,1,0,0,0,34,43,5,8,0,0,35,43,5,9,0,0,36,37,
        5,3,0,0,37,38,5,8,0,0,38,43,5,4,0,0,39,40,5,3,0,0,40,41,5,9,0,0,
        41,43,5,4,0,0,42,34,1,0,0,0,42,35,1,0,0,0,42,36,1,0,0,0,42,39,1,
        0,0,0,43,44,1,0,0,0,44,45,3,2,1,0,45,46,3,2,1,0,46,48,1,0,0,0,47,
        29,1,0,0,0,47,42,1,0,0,0,48,7,1,0,0,0,4,14,29,42,47
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'->'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ID", "WS", "PLUS", "MINUS", 
                      "MULT", "DIV" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_lambdaExpr = 2
    RULE_infixExpr = 3

    ruleNames =  [ "root", "expr", "lambdaExpr", "infixExpr" ]

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
            self.state = 8
            self.expr()
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

        def infixExpr(self):
            return self.getTypedRuleContext(exprsParser.InfixExprContext,0)


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


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(exprsParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = exprsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = exprsParser.ExpresioLambdaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.lambdaExpr()
                pass
            elif token in [3, 8, 9, 10, 11]:
                localctx = exprsParser.OperacioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.infixExpr()
                pass
            elif token in [5]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(exprsParser.NUMBER)
                pass
            elif token in [6]:
                localctx = exprsParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 13
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

        def ID(self):
            return self.getToken(exprsParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_lambdaExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpr(self):

        localctx = exprsParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lambdaExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(exprsParser.T__0)
            self.state = 17
            self.match(exprsParser.ID)
            self.state = 18
            self.match(exprsParser.T__1)
            self.state = 19
            self.expr()
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



    class MultiplicaciodivisioContext(InfixExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InfixExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)

        def MULT(self):
            return self.getToken(exprsParser.MULT, 0)
        def DIV(self):
            return self.getToken(exprsParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicaciodivisio" ):
                return visitor.visitMultiplicaciodivisio(self)
            else:
                return visitor.visitChildren(self)


    class SumarestaContext(InfixExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InfixExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(exprsParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(exprsParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaresta" ):
                return visitor.visitSumaresta(self)
            else:
                return visitor.visitChildren(self)



    def infixExpr(self):

        localctx = exprsParser.InfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_infixExpr)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = exprsParser.MultiplicaciodivisioContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 21
                    self.match(exprsParser.MULT)
                    pass

                elif la_ == 2:
                    self.state = 22
                    self.match(exprsParser.DIV)
                    pass

                elif la_ == 3:
                    self.state = 23
                    self.match(exprsParser.T__2)
                    self.state = 24
                    self.match(exprsParser.MULT)
                    self.state = 25
                    self.match(exprsParser.T__3)
                    pass

                elif la_ == 4:
                    self.state = 26
                    self.match(exprsParser.T__2)
                    self.state = 27
                    self.match(exprsParser.DIV)
                    self.state = 28
                    self.match(exprsParser.T__3)
                    pass


                self.state = 31
                self.expr()
                self.state = 32
                self.expr()
                pass

            elif la_ == 2:
                localctx = exprsParser.SumarestaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 34
                    self.match(exprsParser.PLUS)
                    pass

                elif la_ == 2:
                    self.state = 35
                    self.match(exprsParser.MINUS)
                    pass

                elif la_ == 3:
                    self.state = 36
                    self.match(exprsParser.T__2)
                    self.state = 37
                    self.match(exprsParser.PLUS)
                    self.state = 38
                    self.match(exprsParser.T__3)
                    pass

                elif la_ == 4:
                    self.state = 39
                    self.match(exprsParser.T__2)
                    self.state = 40
                    self.match(exprsParser.MINUS)
                    self.state = 41
                    self.match(exprsParser.T__3)
                    pass


                self.state = 44
                self.expr()
                self.state = 45
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





