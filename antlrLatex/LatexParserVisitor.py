# Generated from LatexParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete generic visitor for a parse tree produced by LatexParser.

class LatexParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatexParser#expr.
    def visitExpr(self, ctx:LatexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#relationExpr.
    def visitRelationExpr(self, ctx:LatexParser.RelationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#relationOp.
    def visitRelationOp(self, ctx:LatexParser.RelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:LatexParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#addOp.
    def visitAddOp(self, ctx:LatexParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:LatexParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#multOp.
    def visitMultOp(self, ctx:LatexParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#postfixExpr.
    def visitPostfixExpr(self, ctx:LatexParser.PostfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#postfixOp.
    def visitPostfixOp(self, ctx:LatexParser.PostfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:LatexParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#fracExpr.
    def visitFracExpr(self, ctx:LatexParser.FracExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#functionExpr.
    def visitFunctionExpr(self, ctx:LatexParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#group.
    def visitGroup(self, ctx:LatexParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#numberAtom.
    def visitNumberAtom(self, ctx:LatexParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#identAtom.
    def visitIdentAtom(self, ctx:LatexParser.IdentAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#commandAtom.
    def visitCommandAtom(self, ctx:LatexParser.CommandAtomContext):
        return self.visitChildren(ctx)



del LatexParser