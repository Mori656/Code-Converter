# Generated from LatexParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete listener for a parse tree produced by LatexParser.
class LatexParserListener(ParseTreeListener):

    # Enter a parse tree produced by LatexParser#expr.
    def enterExpr(self, ctx:LatexParser.ExprContext):
        pass

    # Exit a parse tree produced by LatexParser#expr.
    def exitExpr(self, ctx:LatexParser.ExprContext):
        pass


    # Enter a parse tree produced by LatexParser#relationExpr.
    def enterRelationExpr(self, ctx:LatexParser.RelationExprContext):
        pass

    # Exit a parse tree produced by LatexParser#relationExpr.
    def exitRelationExpr(self, ctx:LatexParser.RelationExprContext):
        pass


    # Enter a parse tree produced by LatexParser#relationOp.
    def enterRelationOp(self, ctx:LatexParser.RelationOpContext):
        pass

    # Exit a parse tree produced by LatexParser#relationOp.
    def exitRelationOp(self, ctx:LatexParser.RelationOpContext):
        pass


    # Enter a parse tree produced by LatexParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:LatexParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by LatexParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:LatexParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by LatexParser#addOp.
    def enterAddOp(self, ctx:LatexParser.AddOpContext):
        pass

    # Exit a parse tree produced by LatexParser#addOp.
    def exitAddOp(self, ctx:LatexParser.AddOpContext):
        pass


    # Enter a parse tree produced by LatexParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:LatexParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by LatexParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:LatexParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by LatexParser#multOp.
    def enterMultOp(self, ctx:LatexParser.MultOpContext):
        pass

    # Exit a parse tree produced by LatexParser#multOp.
    def exitMultOp(self, ctx:LatexParser.MultOpContext):
        pass


    # Enter a parse tree produced by LatexParser#postfixExpr.
    def enterPostfixExpr(self, ctx:LatexParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by LatexParser#postfixExpr.
    def exitPostfixExpr(self, ctx:LatexParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by LatexParser#postfixOp.
    def enterPostfixOp(self, ctx:LatexParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by LatexParser#postfixOp.
    def exitPostfixOp(self, ctx:LatexParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by LatexParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:LatexParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by LatexParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:LatexParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by LatexParser#fracExpr.
    def enterFracExpr(self, ctx:LatexParser.FracExprContext):
        pass

    # Exit a parse tree produced by LatexParser#fracExpr.
    def exitFracExpr(self, ctx:LatexParser.FracExprContext):
        pass


    # Enter a parse tree produced by LatexParser#functionExpr.
    def enterFunctionExpr(self, ctx:LatexParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by LatexParser#functionExpr.
    def exitFunctionExpr(self, ctx:LatexParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by LatexParser#group.
    def enterGroup(self, ctx:LatexParser.GroupContext):
        pass

    # Exit a parse tree produced by LatexParser#group.
    def exitGroup(self, ctx:LatexParser.GroupContext):
        pass


    # Enter a parse tree produced by LatexParser#numberAtom.
    def enterNumberAtom(self, ctx:LatexParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by LatexParser#numberAtom.
    def exitNumberAtom(self, ctx:LatexParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by LatexParser#identAtom.
    def enterIdentAtom(self, ctx:LatexParser.IdentAtomContext):
        pass

    # Exit a parse tree produced by LatexParser#identAtom.
    def exitIdentAtom(self, ctx:LatexParser.IdentAtomContext):
        pass


    # Enter a parse tree produced by LatexParser#commandAtom.
    def enterCommandAtom(self, ctx:LatexParser.CommandAtomContext):
        pass

    # Exit a parse tree produced by LatexParser#commandAtom.
    def exitCommandAtom(self, ctx:LatexParser.CommandAtomContext):
        pass



del LatexParser