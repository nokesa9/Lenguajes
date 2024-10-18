# Generated from Racional.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .RacionalParser import RacionalParser
else:
    from RacionalParser import RacionalParser

# This class defines a complete generic visitor for a parse tree produced by RacionalParser.

class RacionalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RacionalParser#FractionExpr.
    def visitFractionExpr(self, ctx:RacionalParser.FractionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#MulDiv.
    def visitMulDiv(self, ctx:RacionalParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#AddSub.
    def visitAddSub(self, ctx:RacionalParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#Parens.
    def visitParens(self, ctx:RacionalParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalParser#fraction.
    def visitFraction(self, ctx:RacionalParser.FractionContext):
        return self.visitChildren(ctx)



del RacionalParser