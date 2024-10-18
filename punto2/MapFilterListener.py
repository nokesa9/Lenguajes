# Generated from MapFilter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete listener for a parse tree produced by MapFilterParser.
class MapFilterListener(ParseTreeListener):

    # Enter a parse tree produced by MapFilterParser#MapCommand.
    def enterMapCommand(self, ctx:MapFilterParser.MapCommandContext):
        pass

    # Exit a parse tree produced by MapFilterParser#MapCommand.
    def exitMapCommand(self, ctx:MapFilterParser.MapCommandContext):
        pass


    # Enter a parse tree produced by MapFilterParser#FilterCommand.
    def enterFilterCommand(self, ctx:MapFilterParser.FilterCommandContext):
        pass

    # Exit a parse tree produced by MapFilterParser#FilterCommand.
    def exitFilterCommand(self, ctx:MapFilterParser.FilterCommandContext):
        pass


    # Enter a parse tree produced by MapFilterParser#iterable.
    def enterIterable(self, ctx:MapFilterParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFilterParser#iterable.
    def exitIterable(self, ctx:MapFilterParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFilterParser#list.
    def enterList(self, ctx:MapFilterParser.ListContext):
        pass

    # Exit a parse tree produced by MapFilterParser#list.
    def exitList(self, ctx:MapFilterParser.ListContext):
        pass


    # Enter a parse tree produced by MapFilterParser#tuple.
    def enterTuple(self, ctx:MapFilterParser.TupleContext):
        pass

    # Exit a parse tree produced by MapFilterParser#tuple.
    def exitTuple(self, ctx:MapFilterParser.TupleContext):
        pass


    # Enter a parse tree produced by MapFilterParser#elements.
    def enterElements(self, ctx:MapFilterParser.ElementsContext):
        pass

    # Exit a parse tree produced by MapFilterParser#elements.
    def exitElements(self, ctx:MapFilterParser.ElementsContext):
        pass


    # Enter a parse tree produced by MapFilterParser#element.
    def enterElement(self, ctx:MapFilterParser.ElementContext):
        pass

    # Exit a parse tree produced by MapFilterParser#element.
    def exitElement(self, ctx:MapFilterParser.ElementContext):
        pass


    # Enter a parse tree produced by MapFilterParser#function.
    def enterFunction(self, ctx:MapFilterParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#function.
    def exitFunction(self, ctx:MapFilterParser.FunctionContext):
        pass



del MapFilterParser