from antlr4 import *
from antlrLatex.LatexParserVisitor import LatexParserVisitor
from antlrLatex.LatexParser import LatexParser


class LatexToHtmlVisitor(LatexParserVisitor):

    # Mapowanie komend LaTeX na HTML/Unicode
    LATEX_COMMANDS = {
        'pi': '&pi;',
        'approx': '&approx;',
        'alpha': '&alpha;',
        'beta': '&beta;',
        'gamma': '&gamma;',
        'delta': '&delta;',
        'epsilon': '&epsilon;',
        'theta': '&theta;',
        'lambda': '&lambda;',
        'mu': '&mu;',
        'nu': '&nu;',
        'xi': '&xi;',
        'sigma': '&sigma;',
        'tau': '&tau;',
        'phi': '&phi;',
        'chi': '&chi;',
        'psi': '&psi;',
        'omega': '&omega;',
    }

    # Helper – odwiedź wszystkie dzieci i sklej wynik
    def visitChildrenAsText(self, ctx):
        result = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            visited = child.accept(self)
            if visited is not None:
                result.append(visited)
        return "".join(result)

    # ======================
    # Main expression
    # ======================
    def visitExpr(self, ctx:LatexParser.ExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#relationExpr.
    def visitRelationExpr(self, ctx:LatexParser.RelationExprContext):
        return self.visitChildrenAsText(ctx)





    # Visit a parse tree produced by LatexParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:LatexParser.AdditiveExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#addOp.
    def visitAddOp(self, ctx:LatexParser.AddOpContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:LatexParser.MultiplicativeExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#multOp.
    def visitMultOp(self, ctx:LatexParser.MultOpContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#postfixExpr.
    def visitPostfixExpr(self, ctx:LatexParser.PostfixExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#postfixOp.
    def visitPostfixOp(self, ctx:LatexParser.PostfixOpContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:LatexParser.PrimaryExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#fracExpr.
    def visitFracExpr(self, ctx:LatexParser.FracExprContext):
        return f"<mfrac>\n{self.visitChildrenAsText(ctx)}</mfrac>\n"


    # Visit a parse tree produced by LatexParser#functionExpr.
    def visitFunctionExpr(self, ctx:LatexParser.FunctionExprContext):
        return self.visitChildrenAsText(ctx)


    # Visit a parse tree produced by LatexParser#group.
    def visitGroup(self, ctx:LatexParser.GroupContext):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Relation Operator
    # ======================

    # Visit a parse tree produced by LatexParser#relationOp.
    def visitRelationOp(self, ctx:LatexParser.RelationOpContext):
        ctxmnd = ctx.getText()[1:]  # Usuń backslash
        if ctxmnd in self.LATEX_COMMANDS:
            return f"<mo>{self.LATEX_COMMANDS[ctxmnd]}</mo>\n"
        return f"<mo>{ctx.getText()}</mo>\n"

    # ======================
    # Atoms (identifiers, numbers, commands)
    # ======================

    # Visit a parse tree produced by LatexParser#numberAtom.
    def visitNumberAtom(self, ctx:LatexParser.NumberAtomContext):
        print("Visiting NumberAtom:", ctx.getText())
        return f"<mn>{ctx.getText()}</mn>\n"


    # Visit a parse tree produced by LatexParser#identAtom.
    def visitIdentAtom(self, ctx:LatexParser.IdentAtomContext):
        print("Visiting IdentAtom:", ctx.getText())
        return f"<mi>{ctx.getText()}</mi>\n"


    # Visit a parse tree produced by LatexParser#commandAtom.
    def visitCommandAtom(self, ctx:LatexParser.CommandAtomContext):
        print("Visiting CommandAtom:", ctx.getText())
        ctxmnd = ctx.getText()[1:]  # Usuń backslash
        if ctxmnd in self.LATEX_COMMANDS:
            return f"<mi>{self.LATEX_COMMANDS[ctxmnd]}</mi>\n"
        return f"<mi>{ctx.getText()}</mi>\n"