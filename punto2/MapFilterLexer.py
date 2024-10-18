# Generated from MapFilter.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,61,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,4,7,44,8,7,
        11,7,12,7,45,1,8,1,8,5,8,50,8,8,10,8,12,8,53,9,8,1,9,4,9,56,8,9,
        11,9,12,9,57,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,1,0,4,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,
        95,97,122,3,0,9,10,13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,25,1,0,0,0,5,27,1,0,
        0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,43,
        1,0,0,0,17,47,1,0,0,0,19,55,1,0,0,0,21,22,5,77,0,0,22,23,5,65,0,
        0,23,24,5,80,0,0,24,2,1,0,0,0,25,26,5,40,0,0,26,4,1,0,0,0,27,28,
        5,44,0,0,28,6,1,0,0,0,29,30,5,41,0,0,30,8,1,0,0,0,31,32,5,70,0,0,
        32,33,5,73,0,0,33,34,5,76,0,0,34,35,5,84,0,0,35,36,5,69,0,0,36,37,
        5,82,0,0,37,10,1,0,0,0,38,39,5,91,0,0,39,12,1,0,0,0,40,41,5,93,0,
        0,41,14,1,0,0,0,42,44,7,0,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,
        1,0,0,0,45,46,1,0,0,0,46,16,1,0,0,0,47,51,7,1,0,0,48,50,7,2,0,0,
        49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,18,1,
        0,0,0,53,51,1,0,0,0,54,56,7,3,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,6,9,0,0,60,20,1,0,0,
        0,4,0,45,51,57,1,6,0,0
    ]

class MapFilterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    INT = 8
    ID = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'MAP'", "'('", "','", "')'", "'FILTER'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "INT", "ID", "WS" ]

    grammarFileName = "MapFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


