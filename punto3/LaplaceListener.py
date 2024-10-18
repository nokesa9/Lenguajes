# Generated from Laplace.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#transform.
    def enterTransform(self, ctx:LaplaceParser.TransformContext):
        pass

    # Exit a parse tree produced by LaplaceParser#transform.
    def exitTransform(self, ctx:LaplaceParser.TransformContext):
        pass


    # Enter a parse tree produced by LaplaceParser#expr.
    def enterExpr(self, ctx:LaplaceParser.ExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expr.
    def exitExpr(self, ctx:LaplaceParser.ExprContext):
        pass



del LaplaceParser