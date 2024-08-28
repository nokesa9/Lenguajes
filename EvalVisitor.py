from LabeledExprParser import LabeledExprParser
from LabeledExprVisitor import LabeledExprVisitor

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx: LabeledExprParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitPrintExpr(self, ctx: LabeledExprParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx: LabeledExprParser.IntContext):
        return int(ctx.INT().getText())

    def visitId(self, ctx: LabeledExprParser.IdContext):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        return 0

    def visitMulDiv(self, ctx: LabeledExprParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx: LabeledExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx: LabeledExprParser.ParensContext):
        return self.visit(ctx.expr())
