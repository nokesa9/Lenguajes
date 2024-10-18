# Generated from MapFilter.g4 by ANTLR 4.13.0
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
        4,1,10,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,29,
        8,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,5,4,46,8,4,10,4,12,4,49,9,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,
        8,10,12,0,0,50,0,28,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,
        0,8,42,1,0,0,0,10,50,1,0,0,0,12,52,1,0,0,0,14,15,5,1,0,0,15,16,5,
        2,0,0,16,17,3,12,6,0,17,18,5,3,0,0,18,19,3,2,1,0,19,20,5,4,0,0,20,
        29,1,0,0,0,21,22,5,5,0,0,22,23,5,2,0,0,23,24,3,12,6,0,24,25,5,3,
        0,0,25,26,3,2,1,0,26,27,5,4,0,0,27,29,1,0,0,0,28,14,1,0,0,0,28,21,
        1,0,0,0,29,1,1,0,0,0,30,33,3,4,2,0,31,33,3,6,3,0,32,30,1,0,0,0,32,
        31,1,0,0,0,33,3,1,0,0,0,34,35,5,6,0,0,35,36,3,8,4,0,36,37,5,7,0,
        0,37,5,1,0,0,0,38,39,5,2,0,0,39,40,3,8,4,0,40,41,5,4,0,0,41,7,1,
        0,0,0,42,47,3,10,5,0,43,44,5,3,0,0,44,46,3,10,5,0,45,43,1,0,0,0,
        46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,9,1,0,0,0,49,47,1,0,
        0,0,50,51,5,8,0,0,51,11,1,0,0,0,52,53,5,9,0,0,53,13,1,0,0,0,3,28,
        32,47
    ]

class MapFilterParser ( Parser ):

    grammarFileName = "MapFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "ID", "WS" ]

    RULE_command = 0
    RULE_iterable = 1
    RULE_list = 2
    RULE_tuple = 3
    RULE_elements = 4
    RULE_element = 5
    RULE_function = 6

    ruleNames =  [ "command", "iterable", "list", "tuple", "elements", "element", 
                   "function" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT=8
    ID=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapFilterParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FilterCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapFilterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(MapFilterParser.FunctionContext,0)

        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterCommand" ):
                listener.enterFilterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterCommand" ):
                listener.exitFilterCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterCommand" ):
                return visitor.visitFilterCommand(self)
            else:
                return visitor.visitChildren(self)


    class MapCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MapFilterParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(MapFilterParser.FunctionContext,0)

        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapCommand" ):
                listener.enterMapCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapCommand" ):
                listener.exitMapCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapCommand" ):
                return visitor.visitMapCommand(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = MapFilterParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MapFilterParser.MapCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(MapFilterParser.T__0)
                self.state = 15
                self.match(MapFilterParser.T__1)
                self.state = 16
                self.function()
                self.state = 17
                self.match(MapFilterParser.T__2)
                self.state = 18
                self.iterable()
                self.state = 19
                self.match(MapFilterParser.T__3)
                pass
            elif token in [5]:
                localctx = MapFilterParser.FilterCommandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(MapFilterParser.T__4)
                self.state = 22
                self.match(MapFilterParser.T__1)
                self.state = 23
                self.function()
                self.state = 24
                self.match(MapFilterParser.T__2)
                self.state = 25
                self.iterable()
                self.state = 26
                self.match(MapFilterParser.T__3)
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


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapFilterParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(MapFilterParser.TupleContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = MapFilterParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_iterable)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.tuple_()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapFilterParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MapFilterParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MapFilterParser.T__5)
            self.state = 35
            self.elements()
            self.state = 36
            self.match(MapFilterParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapFilterParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = MapFilterParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tuple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MapFilterParser.T__1)
            self.state = 39
            self.elements()
            self.state = 40
            self.match(MapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFilterParser.ElementContext)
            else:
                return self.getTypedRuleContext(MapFilterParser.ElementContext,i)


        def getRuleIndex(self):
            return MapFilterParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = MapFilterParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.element()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 43
                self.match(MapFilterParser.T__2)
                self.state = 44
                self.element()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapFilterParser.INT, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MapFilterParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MapFilterParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFilterParser.ID, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MapFilterParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MapFilterParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





