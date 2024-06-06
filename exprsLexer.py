# Generated from exprs.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,3,1,4,4,4,34,8,4,11,4,12,4,35,1,5,4,5,39,8,5,11,5,12,5,
        40,1,6,4,6,44,8,6,11,6,12,6,45,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,
        10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,1,0,3,1,0,48,57,1,0,97,122,2,0,10,10,32,32,59,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,
        0,0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,33,1,0,0,0,11,38,
        1,0,0,0,13,43,1,0,0,0,15,49,1,0,0,0,17,51,1,0,0,0,19,53,1,0,0,0,
        21,55,1,0,0,0,23,24,5,40,0,0,24,2,1,0,0,0,25,26,5,41,0,0,26,4,1,
        0,0,0,27,28,5,92,0,0,28,6,1,0,0,0,29,30,5,45,0,0,30,31,5,62,0,0,
        31,8,1,0,0,0,32,34,7,0,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,10,1,0,0,0,37,39,7,1,0,0,38,37,1,0,0,0,39,40,
        1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,12,1,0,0,0,42,44,7,2,0,0,
        43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,47,1,
        0,0,0,47,48,6,6,0,0,48,14,1,0,0,0,49,50,5,43,0,0,50,16,1,0,0,0,51,
        52,5,45,0,0,52,18,1,0,0,0,53,54,5,42,0,0,54,20,1,0,0,0,55,56,5,47,
        0,0,56,22,1,0,0,0,4,0,35,40,45,1,6,0,0
    ]

class exprsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    ID = 6
    WS = 7
    PLUS = 8
    MINUS = 9
    MULT = 10
    DIV = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'\\'", "'->'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ID", "WS", "PLUS", "MINUS", "MULT", "DIV" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "ID", "WS", 
                  "PLUS", "MINUS", "MULT", "DIV" ]

    grammarFileName = "exprs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


