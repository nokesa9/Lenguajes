# Generated from MapFilter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete generic visitor for a parse tree produced by MapFilterParser.

class MapFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapFilterParser#MapCommand.
    def visitMapCommand(self, ctx:MapFilterParser.MapCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#FilterCommand.
    def visitFilterCommand(self, ctx:MapFilterParser.FilterCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#iterable.
    def visitIterable(self, ctx:MapFilterParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#list.
    def visitList(self, ctx:MapFilterParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#tuple.
    def visitTuple(self, ctx:MapFilterParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#elements.
    def visitElements(self, ctx:MapFilterParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#element.
    def visitElement(self, ctx:MapFilterParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#function.
    def visitFunction(self, ctx:MapFilterParser.FunctionContext):
        return self.visitChildren(ctx)



del MapFilterParser