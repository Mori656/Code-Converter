from antlrLatex.LatexParser import LatexParser
from antlrLatex.LatexParserVisitor import LatexParserVisitor

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

    LATEX_OPERATORS = {
        'surd': '\u221A',
        'coprod': '\u2210',
        'bigvee': '\u22C1',
        'bigwedge': '\u22C0',
        'biguplus': '\u2A04',
        'bigcap': '\u22C2',
        'bigcup': '\u22C3',
        'int': '&#x222B;',
        'intop': '\u222B',
        'iint': '\u222C',
        'iiint': '\u222D',
        'prod': '\u220F',
        'sum': '\u2211',
        'bigotimes': '\u2A02',
        'bigoplus': '\u2A01',
        'bigodot': '\u2A00',
        'oint': '\u222E',
        'ointop': '\u222E',
        'oiint': '\u222F',
        'oiiint': '\u2230',
        'bigsqcup': '\u2A06',
        'smallint': '\u222B',
        'triangleleft': '\u25C3',
        'triangleright': '\u25B9',
        'bigtriangleup': '\u25B3',
        'bigtriangledown': '\u25BD',
        'wedge': '\u2227',
        'land': '\u2227',
        'vee': '\u2228',
        'lor': '\u2228',
        'cap': '\u2229',
        'cup': '\u222A',
        'ddagger': '\u2021',
        'dagger': '\u2020',
        'sqcap': '\u2293',
        'sqcup': '\u2294',
        'uplus': '\u228E',
        'amalg': '\u2A3F',
        'diamond': '\u22C4',
        'bullet': '\u2219',
        'wr': '\u2240',
        'div': '\u00F7',
        'odot': '\u2299',
        'oslash': '\u2298',
        'otimes': '\u2297',
        'ominus': '\u2296',
        'oplus': '\u2295',
        'mp': '\u2213',
        'pm': '\u00B1',
        'circ': '\u2218',
        'bigcirc': '\u25EF',
        'setminus': '\u2216',
        'cdot': '\u22C5',
        'ast': '\u2217',
        'times': '\u00D7',
        'star': '\u22C6',
        'propto': '\u221D',
        'sqsubseteq': '\u2291',
        'sqsupseteq': '\u2292',
        'parallel': '\u2225',
        'mid': '\u2223',
        'dashv': '\u22A3',
        'vdash': '\u22A2',
        'leq': '\u2264',
        'le': '\u2264',
        'geq': '\u2265',
        'ge': '\u2265',
        'lt': '\u003C',
        'gt': '\u003E',
        'succ': '\u227B',
        'prec': '\u227A',
        'approx': '\u2248',
        'succeq': '\u2AB0',
        'preceq': '\u2AAF',
        'supset': '\u2283',
        'subset': '\u2282',
        'supseteq': '\u2287',
        'subseteq': '\u2286',
        'in': '\u2208',
        'ni': '\u220B',
        'notin': '\u2209',
        'owns': '\u220B',
        'gg': '\u226B',
        'll': '\u226A',
        'sim': '\u223C',
        'simeq': '\u2243',
        'perp': '\u27C2',
        'equiv': '\u2261',
        'asymp': '\u224D',
        'smile': '\u2323',
        'frown': '\u2322',
        'ne': '\u2260',
        'neq': '\u2260',
        'cong': '\u2245',
        'doteq': '\u2250',
        'bowtie': '\u22C8',
        'models': '\u22A7',
    }

    def visitExpr(self, ctx: LatexParser.ExprContext):
        # presentation math: sequence becomes mrow
        children = [self.visit(c) for c in ctx.term()]
        return f"<mrow>{''.join(children)}</mrow>"

    def visitTerm(self, ctx: LatexParser.TermContext):
        if ctx.fraction():
            return self.visit(ctx.fraction())
        elif ctx.root():
            return self.visit(ctx.root())
        else:
            return self.visit(ctx.scriptable())

    def visitFraction(self, ctx: LatexParser.FractionContext):
        num = self.visit(ctx.expr(0))
        den = self.visit(ctx.expr(1))
        return f"<mfrac>{num}{den}</mfrac>"

    def visitRoot(self, ctx: LatexParser.RootContext):
        if (len(ctx.expr()) == 2):
            # nth root version
            degree = self.visit(ctx.expr(0))
            num    = self.visit(ctx.expr(1))
            return f"<mroot>{num}{degree}</mroot>"
        else:
            # square root version
            num    = self.visit(ctx.expr(0))
            return f"<msqrt>{num}</msqrt>"

    def visitScriptable(self, ctx: LatexParser.ScriptableContext):
        base = self.visit(ctx.atom())
        sub = None
        sup = None

        if ctx.subscript():
            sub = self.visit(ctx.subscript().atom())

        if ctx.superscript():
            sup = self.visit(ctx.superscript().atom())

        if sub and sup:
            return f"<msubsup>{base}{sub}{sup}</msubsup>"
        elif sub:
            return f"<msub>{base}{sub}</msub>"
        elif sup:
            return f"<msup>{base}{sup}</msup>"
        else:
            return base

    def visitAtom(self, ctx: LatexParser.AtomContext):
        if ctx.NUMBER():
            return f"<mn>{ctx.NUMBER().getText()}</mn>"
        if ctx.IDENT():
            return f"<mi>{ctx.IDENT().getText()}</mi>"
        if ctx.COMMAND():
            ctxmnd = ctx.COMMAND().getText()[1:]  # Usuń backslash
            if ctxmnd in self.LATEX_OPERATORS:
                return f"<mo>{self.LATEX_OPERATORS[ctxmnd]}</mo>\n"
            return f"<mi>{self.LATEX_COMMANDS[ctxmnd] if ctxmnd in self.LATEX_COMMANDS else ctxmnd}</mi>\n"
        if ctx.operator():
            return f"<mo>{ctx.operator().getText()}</mo>"
        if ctx.LPAREN():
            inner = self.visit(ctx.expr())
            return f"<mrow><mo>(</mo>{inner}<mo>)</mo></mrow>"
        if ctx.LBRACE():
            inner = self.visit(ctx.expr())
            return f"<mrow>{inner}</mrow>"
        if ctx.nbsp():
            return "<mtext>&nbsp;</mtext>"
        raise Exception("Unhandled atom type")
