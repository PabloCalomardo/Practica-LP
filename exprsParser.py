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
        4,1,10,37,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,
        3,1,14,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,12,
        1,28,9,1,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,0,1,2,3,0,2,4,0,2,1,
        0,2,3,1,0,4,5,39,0,8,1,0,0,0,2,13,1,0,0,0,4,34,1,0,0,0,6,9,3,2,1,
        0,7,9,3,4,2,0,8,6,1,0,0,0,8,7,1,0,0,0,9,1,1,0,0,0,10,11,6,1,-1,0,
        11,14,5,9,0,0,12,14,5,8,0,0,13,10,1,0,0,0,13,12,1,0,0,0,14,26,1,
        0,0,0,15,16,10,5,0,0,16,17,5,1,0,0,17,25,3,2,1,5,18,19,10,4,0,0,
        19,20,7,0,0,0,20,25,3,2,1,5,21,22,10,3,0,0,22,23,7,1,0,0,23,25,3,
        2,1,4,24,15,1,0,0,0,24,18,1,0,0,0,24,21,1,0,0,0,25,28,1,0,0,0,26,
        24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,0,0,29,30,5,8,0,
        0,30,31,5,6,0,0,31,35,3,2,1,0,32,33,5,7,0,0,33,35,3,2,1,0,34,29,
        1,0,0,0,34,32,1,0,0,0,35,5,1,0,0,0,5,8,13,24,26,34
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "':='", 
                     "'write'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WRITE", "VAR", 
                      "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_instr = 2

    ruleNames =  [ "root", "expr", "instr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WRITE=7
    VAR=8
    NUM=9
    WS=10

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


        def instr(self):
            return self.getTypedRuleContext(exprsParser.InstrContext,0)


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
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.instr()
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
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class SumarestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaresta" ):
                return visitor.visitSumaresta(self)
            else:
                return visitor.visitChildren(self)


    class MuldivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldiv" ):
                return visitor.visitMuldiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.match(exprsParser.NUM)
                pass
            elif token in [8]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(exprsParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.PotenciaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 16
                        self.match(exprsParser.T__0)
                        self.state = 17
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.MuldivContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 19
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 20
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.SumarestaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 22
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 23
                        self.expr(4)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_instr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignacioContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)


    class EscriuContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(exprsParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriu" ):
                return visitor.visitEscriu(self)
            else:
                return visitor.visitChildren(self)



    def instr(self):

        localctx = exprsParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instr)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = exprsParser.AssignacioContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(exprsParser.VAR)
                self.state = 30
                self.match(exprsParser.T__5)
                self.state = 31
                self.expr(0)
                pass
            elif token in [7]:
                localctx = exprsParser.EscriuContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(exprsParser.WRITE)
                self.state = 33
                self.expr(0)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




