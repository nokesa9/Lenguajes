# Generated from Racional.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .RacionalParser import RacionalParser
else:
    from RacionalParser import RacionalParser

# This class defines a complete listener for a parse tree produced by RacionalParser.
class RacionalListener(ParseTreeListener):

    # Enter a parse tree produced by RacionalParser#FractionExpr.
    def enterFractionExpr(self, ctx:RacionalParser.FractionExprContext):
        pass

    # Exit a parse tree produced by RacionalParser#FractionExpr.
    def exitFractionExpr(self, ctx:RacionalParser.FractionExprContext):
        pass


    # Enter a parse tree produced by RacionalParser#MulDiv.
    def enterMulDiv(self, ctx:RacionalParser.MulDivContext):
        pass

    # Exit a parse tree produced by RacionalParser#MulDiv.
    def exitMulDiv(self, ctx:RacionalParser.MulDivContext):
        pass


    # Enter a parse tree produced by RacionalParser#AddSub.
    def enterAddSub(self, ctx:RacionalParser.AddSubContext):
        pass

    # Exit a parse tree produced by RacionalParser#AddSub.
    def exitAddSub(self, ctx:RacionalParser.AddSubContext):
        pass


    # Enter a parse tree produced by RacionalParser#Parens.
    def enterParens(self, ctx:RacionalParser.ParensContext):
        pass

    # Exit a parse tree produced by RacionalParser#Parens.
    def exitParens(self, ctx:RacionalParser.ParensContext):
        pass


    # Enter a parse tree produced by RacionalParser#fraction.
    def enterFraction(self, ctx:RacionalParser.FractionContext):
        pass

    # Exit a parse tree produced by RacionalParser#fraction.
    def exitFraction(self, ctx:RacionalParser.FractionContext):
        pass



del RacionalParser