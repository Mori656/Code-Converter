# Generated from LatexParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,3,3,46,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,56,8,4,
        1,4,1,4,1,4,3,4,61,8,4,3,4,63,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,86,8,8,
        1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,
        0,8,9,1,0,10,18,94,0,23,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,40,1,
        0,0,0,8,62,1,0,0,0,10,64,1,0,0,0,12,67,1,0,0,0,14,70,1,0,0,0,16,
        85,1,0,0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,
        0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,31,3,
        4,2,0,28,31,3,6,3,0,29,31,3,8,4,0,30,27,1,0,0,0,30,28,1,0,0,0,30,
        29,1,0,0,0,31,3,1,0,0,0,32,33,5,20,0,0,33,34,5,2,0,0,34,35,3,0,0,
        0,35,36,5,3,0,0,36,37,5,2,0,0,37,38,3,0,0,0,38,39,5,3,0,0,39,5,1,
        0,0,0,40,45,5,21,0,0,41,42,5,6,0,0,42,43,3,0,0,0,43,44,5,7,0,0,44,
        46,1,0,0,0,45,41,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,2,0,
        0,48,49,3,0,0,0,49,50,5,3,0,0,50,7,1,0,0,0,51,63,3,16,8,0,52,53,
        3,16,8,0,53,55,3,12,6,0,54,56,3,10,5,0,55,54,1,0,0,0,55,56,1,0,0,
        0,56,63,1,0,0,0,57,58,3,16,8,0,58,60,3,10,5,0,59,61,3,12,6,0,60,
        59,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,51,1,0,0,0,62,52,1,0,0,
        0,62,57,1,0,0,0,63,9,1,0,0,0,64,65,5,9,0,0,65,66,3,16,8,0,66,11,
        1,0,0,0,67,68,5,8,0,0,68,69,3,16,8,0,69,13,1,0,0,0,70,71,7,0,0,0,
        71,15,1,0,0,0,72,86,5,23,0,0,73,86,5,24,0,0,74,86,5,22,0,0,75,76,
        5,4,0,0,76,77,3,0,0,0,77,78,5,5,0,0,78,86,1,0,0,0,79,80,5,2,0,0,
        80,81,3,0,0,0,81,82,5,3,0,0,82,86,1,0,0,0,83,86,3,20,10,0,84,86,
        3,18,9,0,85,72,1,0,0,0,85,73,1,0,0,0,85,74,1,0,0,0,85,75,1,0,0,0,
        85,79,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,87,88,5,
        19,0,0,88,19,1,0,0,0,89,90,7,1,0,0,90,21,1,0,0,0,7,25,30,45,55,60,
        62,85
    ]

class LatexParser ( Parser ):

    grammarFileName = "LatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "'^'", "'_'", "'!'", "'*'", "'/'", "'+'", "'-'", 
                     "'<'", "'>'", "'='", "'.'", "'~'" ]

    symbolicNames = [ "<INVALID>", "BACKSLASH", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "LBRACK", "RBRACK", "CARET", "UNDERSCORE", 
                      "EXCLAMATION", "ASTERISK", "SLASH", "PLUS", "MINUS", 
                      "LT", "GT", "EQUALS", "DOT", "TILDE", "FRAC", "SQRT", 
                      "COMMAND", "NUMBER", "IDENT", "WHITESPACE" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_fraction = 2
    RULE_root = 3
    RULE_scriptable = 4
    RULE_subscript = 5
    RULE_superscript = 6
    RULE_scriptOp = 7
    RULE_atom = 8
    RULE_nbsp = 9
    RULE_operator = 10

    ruleNames =  [ "expr", "term", "fraction", "root", "scriptable", "subscript", 
                   "superscript", "scriptOp", "atom", "nbsp", "operator" ]

    EOF = Token.EOF
    BACKSLASH=1
    LBRACE=2
    RBRACE=3
    LPAREN=4
    RPAREN=5
    LBRACK=6
    RBRACK=7
    CARET=8
    UNDERSCORE=9
    EXCLAMATION=10
    ASTERISK=11
    SLASH=12
    PLUS=13
    MINUS=14
    LT=15
    GT=16
    EQUALS=17
    DOT=18
    TILDE=19
    FRAC=20
    SQRT=21
    COMMAND=22
    NUMBER=23
    IDENT=24
    WHITESPACE=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TermContext)
            else:
                return self.getTypedRuleContext(LatexParser.TermContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = LatexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.term()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33553428) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fraction(self):
            return self.getTypedRuleContext(LatexParser.FractionContext,0)


        def root(self):
            return self.getTypedRuleContext(LatexParser.RootContext,0)


        def scriptable(self):
            return self.getTypedRuleContext(LatexParser.ScriptableContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LatexParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.fraction()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.root()
                pass
            elif token in [2, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.scriptable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRAC(self):
            return self.getToken(LatexParser.FRAC, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.LBRACE)
            else:
                return self.getToken(LatexParser.LBRACE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.ExprContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.RBRACE)
            else:
                return self.getToken(LatexParser.RBRACE, i)

        def getRuleIndex(self):
            return LatexParser.RULE_fraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFraction" ):
                listener.enterFraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFraction" ):
                listener.exitFraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFraction" ):
                return visitor.visitFraction(self)
            else:
                return visitor.visitChildren(self)




    def fraction(self):

        localctx = LatexParser.FractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(LatexParser.FRAC)
            self.state = 33
            self.match(LatexParser.LBRACE)
            self.state = 34
            self.expr()
            self.state = 35
            self.match(LatexParser.RBRACE)
            self.state = 36
            self.match(LatexParser.LBRACE)
            self.state = 37
            self.expr()
            self.state = 38
            self.match(LatexParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQRT(self):
            return self.getToken(LatexParser.SQRT, 0)

        def LBRACE(self):
            return self.getToken(LatexParser.LBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(LatexParser.RBRACE, 0)

        def LBRACK(self):
            return self.getToken(LatexParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(LatexParser.RBRACK, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = LatexParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(LatexParser.SQRT)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 41
                self.match(LatexParser.LBRACK)
                self.state = 42
                self.expr()
                self.state = 43
                self.match(LatexParser.RBRACK)


            self.state = 47
            self.match(LatexParser.LBRACE)
            self.state = 48
            self.expr()
            self.state = 49
            self.match(LatexParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LatexParser.AtomContext,0)


        def superscript(self):
            return self.getTypedRuleContext(LatexParser.SuperscriptContext,0)


        def subscript(self):
            return self.getTypedRuleContext(LatexParser.SubscriptContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_scriptable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScriptable" ):
                listener.enterScriptable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScriptable" ):
                listener.exitScriptable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScriptable" ):
                return visitor.visitScriptable(self)
            else:
                return visitor.visitChildren(self)




    def scriptable(self):

        localctx = LatexParser.ScriptableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scriptable)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.atom()
                self.state = 53
                self.superscript()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 54
                    self.subscript()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.atom()
                self.state = 58
                self.subscript()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 59
                    self.superscript()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LatexParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(LatexParser.AtomContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_subscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript" ):
                listener.enterSubscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript" ):
                listener.exitSubscript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript" ):
                return visitor.visitSubscript(self)
            else:
                return visitor.visitChildren(self)




    def subscript(self):

        localctx = LatexParser.SubscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LatexParser.UNDERSCORE)
            self.state = 65
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperscriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LatexParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LatexParser.AtomContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_superscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperscript" ):
                listener.enterSuperscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperscript" ):
                listener.exitSuperscript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperscript" ):
                return visitor.visitSuperscript(self)
            else:
                return visitor.visitChildren(self)




    def superscript(self):

        localctx = LatexParser.SuperscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_superscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(LatexParser.CARET)
            self.state = 68
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LatexParser.CARET, 0)

        def UNDERSCORE(self):
            return self.getToken(LatexParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_scriptOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScriptOp" ):
                listener.enterScriptOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScriptOp" ):
                listener.exitScriptOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScriptOp" ):
                return visitor.visitScriptOp(self)
            else:
                return visitor.visitChildren(self)




    def scriptOp(self):

        localctx = LatexParser.ScriptOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_scriptOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LatexParser.NUMBER, 0)

        def IDENT(self):
            return self.getToken(LatexParser.IDENT, 0)

        def COMMAND(self):
            return self.getToken(LatexParser.COMMAND, 0)

        def LPAREN(self):
            return self.getToken(LatexParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(LatexParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(LatexParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(LatexParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LatexParser.RBRACE, 0)

        def operator(self):
            return self.getTypedRuleContext(LatexParser.OperatorContext,0)


        def nbsp(self):
            return self.getTypedRuleContext(LatexParser.NbspContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = LatexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(LatexParser.NUMBER)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(LatexParser.IDENT)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(LatexParser.COMMAND)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(LatexParser.LPAREN)
                self.state = 76
                self.expr()
                self.state = 77
                self.match(LatexParser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.match(LatexParser.LBRACE)
                self.state = 80
                self.expr()
                self.state = 81
                self.match(LatexParser.RBRACE)
                pass
            elif token in [10, 11, 12, 13, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.operator()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.nbsp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NbspContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(LatexParser.TILDE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_nbsp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNbsp" ):
                listener.enterNbsp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNbsp" ):
                listener.exitNbsp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNbsp" ):
                return visitor.visitNbsp(self)
            else:
                return visitor.visitChildren(self)




    def nbsp(self):

        localctx = LatexParser.NbspContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nbsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(LatexParser.TILDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATION(self):
            return self.getToken(LatexParser.EXCLAMATION, 0)

        def ASTERISK(self):
            return self.getToken(LatexParser.ASTERISK, 0)

        def SLASH(self):
            return self.getToken(LatexParser.SLASH, 0)

        def PLUS(self):
            return self.getToken(LatexParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LatexParser.MINUS, 0)

        def LT(self):
            return self.getToken(LatexParser.LT, 0)

        def GT(self):
            return self.getToken(LatexParser.GT, 0)

        def EQUALS(self):
            return self.getToken(LatexParser.EQUALS, 0)

        def DOT(self):
            return self.getToken(LatexParser.DOT, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = LatexParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 523264) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





