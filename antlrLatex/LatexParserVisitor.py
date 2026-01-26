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


    # Visit a parse tree produced by LatexParser#term.
    def visitTerm(self, ctx:LatexParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#fraction.
    def visitFraction(self, ctx:LatexParser.FractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#scriptable.
    def visitScriptable(self, ctx:LatexParser.ScriptableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#scriptOp.
    def visitScriptOp(self, ctx:LatexParser.ScriptOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#atom.
    def visitAtom(self, ctx:LatexParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#nbsp.
    def visitNbsp(self, ctx:LatexParser.NbspContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#operator.
    def visitOperator(self, ctx:LatexParser.OperatorContext):
        return self.visitChildren(ctx)



del LatexParser