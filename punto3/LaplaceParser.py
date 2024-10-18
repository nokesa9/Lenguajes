# Generated from Laplace.g4 by ANTLR 4.13.0
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
        4,1,15,47,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,31,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,42,8,1,10,1,
        12,1,45,9,1,1,1,0,1,2,2,0,2,0,2,1,0,3,4,1,0,5,6,53,0,4,1,0,0,0,2,
        30,1,0,0,0,4,5,5,1,0,0,5,6,3,2,1,0,6,7,5,2,0,0,7,1,1,0,0,0,8,9,6,
        1,-1,0,9,10,5,4,0,0,10,31,3,2,1,7,11,12,5,8,0,0,12,13,5,9,0,0,13,
        14,3,2,1,0,14,15,5,2,0,0,15,31,1,0,0,0,16,17,5,10,0,0,17,18,5,9,
        0,0,18,19,3,2,1,0,19,20,5,2,0,0,20,31,1,0,0,0,21,22,5,11,0,0,22,
        23,5,9,0,0,23,24,3,2,1,0,24,25,5,2,0,0,25,31,1,0,0,0,26,27,5,13,
        0,0,27,31,5,12,0,0,28,31,5,12,0,0,29,31,5,13,0,0,30,8,1,0,0,0,30,
        11,1,0,0,0,30,16,1,0,0,0,30,21,1,0,0,0,30,26,1,0,0,0,30,28,1,0,0,
        0,30,29,1,0,0,0,31,43,1,0,0,0,32,33,10,10,0,0,33,34,7,0,0,0,34,42,
        3,2,1,11,35,36,10,9,0,0,36,37,7,1,0,0,37,42,3,2,1,10,38,39,10,8,
        0,0,39,40,5,7,0,0,40,42,3,2,1,9,41,32,1,0,0,0,41,35,1,0,0,0,41,38,
        1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,3,1,0,0,0,45,
        43,1,0,0,0,3,30,41,43
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'L('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'exp'", "'('", "'sin'", "'cos'", "'t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "ID", "WS" ]

    RULE_transform = 0
    RULE_expr = 1

    ruleNames =  [ "transform", "expr" ]

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
    NUMBER=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_transform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransform" ):
                listener.enterTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransform" ):
                listener.exitTransform(self)




    def transform(self):

        localctx = LaplaceParser.TransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_transform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(LaplaceParser.T__0)
            self.state = 5
            self.expr(0)
            self.state = 6
            self.match(LaplaceParser.T__1)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.ExprContext,i)


        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaplaceParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 9
                self.match(LaplaceParser.T__3)
                self.state = 10
                self.expr(7)
                pass

            elif la_ == 2:
                self.state = 11
                self.match(LaplaceParser.T__7)
                self.state = 12
                self.match(LaplaceParser.T__8)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(LaplaceParser.T__1)
                pass

            elif la_ == 3:
                self.state = 16
                self.match(LaplaceParser.T__9)
                self.state = 17
                self.match(LaplaceParser.T__8)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(LaplaceParser.T__1)
                pass

            elif la_ == 4:
                self.state = 21
                self.match(LaplaceParser.T__10)
                self.state = 22
                self.match(LaplaceParser.T__8)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(LaplaceParser.T__1)
                pass

            elif la_ == 5:
                self.state = 26
                self.match(LaplaceParser.NUMBER)
                self.state = 27
                self.match(LaplaceParser.T__11)
                pass

            elif la_ == 6:
                self.state = 28
                self.match(LaplaceParser.T__11)
                pass

            elif la_ == 7:
                self.state = 29
                self.match(LaplaceParser.NUMBER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LaplaceParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = LaplaceParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = LaplaceParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 39
                        self.match(LaplaceParser.T__6)
                        self.state = 40
                        self.expr(9)
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




