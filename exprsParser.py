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
        4,1,21,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,3,0,13,
        8,0,1,1,1,1,1,1,3,1,18,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,29,8,1,10,1,12,1,32,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,3,1,3,3,3,
        58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,77,8,4,1,4,0,1,2,5,0,2,4,6,8,0,2,1,0,2,3,1,0,4,5,87,
        0,12,1,0,0,0,2,17,1,0,0,0,4,51,1,0,0,0,6,57,1,0,0,0,8,76,1,0,0,0,
        10,13,3,2,1,0,11,13,3,8,4,0,12,10,1,0,0,0,12,11,1,0,0,0,13,1,1,0,
        0,0,14,15,6,1,-1,0,15,18,5,20,0,0,16,18,5,19,0,0,17,14,1,0,0,0,17,
        16,1,0,0,0,18,30,1,0,0,0,19,20,10,5,0,0,20,21,5,1,0,0,21,29,3,2,
        1,5,22,23,10,4,0,0,23,24,7,0,0,0,24,29,3,2,1,5,25,26,10,3,0,0,26,
        27,7,1,0,0,27,29,3,2,1,4,28,19,1,0,0,0,28,22,1,0,0,0,28,25,1,0,0,
        0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,0,32,30,1,
        0,0,0,33,34,5,19,0,0,34,35,5,6,0,0,35,52,3,2,1,0,36,37,5,19,0,0,
        37,38,5,7,0,0,38,52,3,2,1,0,39,40,5,19,0,0,40,41,5,8,0,0,41,52,3,
        2,1,0,42,43,5,19,0,0,43,44,5,9,0,0,44,52,3,2,1,0,45,46,5,19,0,0,
        46,47,5,10,0,0,47,52,3,2,1,0,48,49,5,19,0,0,49,50,5,11,0,0,50,52,
        3,2,1,0,51,33,1,0,0,0,51,36,1,0,0,0,51,39,1,0,0,0,51,42,1,0,0,0,
        51,45,1,0,0,0,51,48,1,0,0,0,52,5,1,0,0,0,53,54,3,8,4,0,54,55,3,6,
        3,0,55,58,1,0,0,0,56,58,3,8,4,0,57,53,1,0,0,0,57,56,1,0,0,0,58,7,
        1,0,0,0,59,60,5,19,0,0,60,61,5,12,0,0,61,77,3,2,1,0,62,63,5,13,0,
        0,63,77,3,2,1,0,64,65,5,14,0,0,65,66,3,4,2,0,66,67,5,15,0,0,67,68,
        3,6,3,0,68,69,5,16,0,0,69,77,1,0,0,0,70,71,5,17,0,0,71,72,3,4,2,
        0,72,73,5,18,0,0,73,74,3,6,3,0,74,75,5,16,0,0,75,77,1,0,0,0,76,59,
        1,0,0,0,76,62,1,0,0,0,76,64,1,0,0,0,76,70,1,0,0,0,77,9,1,0,0,0,7,
        12,17,28,30,51,57,76
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "'='", 
                     "'<>'", "'<='", "'>='", "'<'", "'>'", "':='", "'write'", 
                     "'if'", "'then'", "'end'", "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WRITE", "IF", "THEN", "END", "WHILE", 
                      "DO", "VAR", "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_cond = 2
    RULE_instr2 = 3
    RULE_instr = 4

    ruleNames =  [ "root", "expr", "cond", "instr2", "instr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    WRITE=13
    IF=14
    THEN=15
    END=16
    WHILE=17
    DO=18
    VAR=19
    NUM=20
    WS=21

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
            self.state = 12
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
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
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(exprsParser.NUM)
                pass
            elif token in [19]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(exprsParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.PotenciaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 20
                        self.match(exprsParser.T__0)
                        self.state = 21
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.MuldivContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 23
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.SumarestaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 26
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 27
                        self.expr(4)
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MenorigualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorigual" ):
                return visitor.visitMenorigual(self)
            else:
                return visitor.visitChildren(self)


    class MajorContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMajor" ):
                return visitor.visitMajor(self)
            else:
                return visitor.visitChildren(self)


    class MenorContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenor" ):
                return visitor.visitMenor(self)
            else:
                return visitor.visitChildren(self)


    class IgualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgual" ):
                return visitor.visitIgual(self)
            else:
                return visitor.visitChildren(self)


    class DiferentContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiferent" ):
                return visitor.visitDiferent(self)
            else:
                return visitor.visitChildren(self)


    class MesgranigualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMesgranigual" ):
                return visitor.visitMesgranigual(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = exprsParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cond)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = exprsParser.IgualContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(exprsParser.VAR)
                self.state = 34
                self.match(exprsParser.T__5)
                self.state = 35
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = exprsParser.DiferentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(exprsParser.VAR)
                self.state = 37
                self.match(exprsParser.T__6)
                self.state = 38
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = exprsParser.MenorigualContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(exprsParser.VAR)
                self.state = 40
                self.match(exprsParser.T__7)
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = exprsParser.MesgranigualContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.match(exprsParser.VAR)
                self.state = 43
                self.match(exprsParser.T__8)
                self.state = 44
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = exprsParser.MenorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.match(exprsParser.VAR)
                self.state = 46
                self.match(exprsParser.T__9)
                self.state = 47
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = exprsParser.MajorContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(exprsParser.VAR)
                self.state = 49
                self.match(exprsParser.T__10)
                self.state = 50
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self):
            return self.getTypedRuleContext(exprsParser.InstrContext,0)


        def instr2(self):
            return self.getTypedRuleContext(exprsParser.Instr2Context,0)


        def getRuleIndex(self):
            return exprsParser.RULE_instr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr2" ):
                return visitor.visitInstr2(self)
            else:
                return visitor.visitChildren(self)




    def instr2(self):

        localctx = exprsParser.Instr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instr2)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.instr()
                self.state = 54
                self.instr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.instr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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


    class WhileContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(exprsParser.WHILE, 0)
        def cond(self):
            return self.getTypedRuleContext(exprsParser.CondContext,0)

        def DO(self):
            return self.getToken(exprsParser.DO, 0)
        def instr2(self):
            return self.getTypedRuleContext(exprsParser.Instr2Context,0)

        def END(self):
            return self.getToken(exprsParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(exprsParser.IF, 0)
        def cond(self):
            return self.getTypedRuleContext(exprsParser.CondContext,0)

        def THEN(self):
            return self.getToken(exprsParser.THEN, 0)
        def instr2(self):
            return self.getTypedRuleContext(exprsParser.Instr2Context,0)

        def END(self):
            return self.getToken(exprsParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def instr(self):

        localctx = exprsParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instr)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = exprsParser.AssignacioContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(exprsParser.VAR)
                self.state = 60
                self.match(exprsParser.T__11)
                self.state = 61
                self.expr(0)
                pass
            elif token in [13]:
                localctx = exprsParser.EscriuContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(exprsParser.WRITE)
                self.state = 63
                self.expr(0)
                pass
            elif token in [14]:
                localctx = exprsParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(exprsParser.IF)
                self.state = 65
                self.cond()
                self.state = 66
                self.match(exprsParser.THEN)
                self.state = 67
                self.instr2()
                self.state = 68
                self.match(exprsParser.END)
                pass
            elif token in [17]:
                localctx = exprsParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(exprsParser.WHILE)
                self.state = 71
                self.cond()
                self.state = 72
                self.match(exprsParser.DO)
                self.state = 73
                self.instr2()
                self.state = 74
                self.match(exprsParser.END)
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
         




