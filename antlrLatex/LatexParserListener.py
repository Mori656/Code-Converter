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


    # Enter a parse tree produced by LatexParser#term.
    def enterTerm(self, ctx:LatexParser.TermContext):
        pass

    # Exit a parse tree produced by LatexParser#term.
    def exitTerm(self, ctx:LatexParser.TermContext):
        pass


    # Enter a parse tree produced by LatexParser#fraction.
    def enterFraction(self, ctx:LatexParser.FractionContext):
        pass

    # Exit a parse tree produced by LatexParser#fraction.
    def exitFraction(self, ctx:LatexParser.FractionContext):
        pass


    # Enter a parse tree produced by LatexParser#root.
    def enterRoot(self, ctx:LatexParser.RootContext):
        pass

    # Exit a parse tree produced by LatexParser#root.
    def exitRoot(self, ctx:LatexParser.RootContext):
        pass


    # Enter a parse tree produced by LatexParser#scriptable.
    def enterScriptable(self, ctx:LatexParser.ScriptableContext):
        pass

    # Exit a parse tree produced by LatexParser#scriptable.
    def exitScriptable(self, ctx:LatexParser.ScriptableContext):
        pass


    # Enter a parse tree produced by LatexParser#subscript.
    def enterSubscript(self, ctx:LatexParser.SubscriptContext):
        pass

    # Exit a parse tree produced by LatexParser#subscript.
    def exitSubscript(self, ctx:LatexParser.SubscriptContext):
        pass


    # Enter a parse tree produced by LatexParser#superscript.
    def enterSuperscript(self, ctx:LatexParser.SuperscriptContext):
        pass

    # Exit a parse tree produced by LatexParser#superscript.
    def exitSuperscript(self, ctx:LatexParser.SuperscriptContext):
        pass


    # Enter a parse tree produced by LatexParser#scriptOp.
    def enterScriptOp(self, ctx:LatexParser.ScriptOpContext):
        pass

    # Exit a parse tree produced by LatexParser#scriptOp.
    def exitScriptOp(self, ctx:LatexParser.ScriptOpContext):
        pass


    # Enter a parse tree produced by LatexParser#atom.
    def enterAtom(self, ctx:LatexParser.AtomContext):
        pass

    # Exit a parse tree produced by LatexParser#atom.
    def exitAtom(self, ctx:LatexParser.AtomContext):
        pass


    # Enter a parse tree produced by LatexParser#nbsp.
    def enterNbsp(self, ctx:LatexParser.NbspContext):
        pass

    # Exit a parse tree produced by LatexParser#nbsp.
    def exitNbsp(self, ctx:LatexParser.NbspContext):
        pass


    # Enter a parse tree produced by LatexParser#operator.
    def enterOperator(self, ctx:LatexParser.OperatorContext):
        pass

    # Exit a parse tree produced by LatexParser#operator.
    def exitOperator(self, ctx:LatexParser.OperatorContext):
        pass



del LatexParser