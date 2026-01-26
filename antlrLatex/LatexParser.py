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
        4,1,22,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,38,8,3,1,3,1,3,1,3,3,
        3,43,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,60,8,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,
        1,0,6,7,1,0,8,16,67,0,17,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,33,
        1,0,0,0,8,44,1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,63,1,0,0,0,16,
        18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,1,1,0,0,0,21,24,3,4,2,0,22,24,3,6,3,0,23,21,1,0,0,0,23,22,1,
        0,0,0,24,3,1,0,0,0,25,26,5,18,0,0,26,27,5,2,0,0,27,28,3,0,0,0,28,
        29,5,3,0,0,29,30,5,2,0,0,30,31,3,0,0,0,31,32,5,3,0,0,32,5,1,0,0,
        0,33,37,3,10,5,0,34,35,3,8,4,0,35,36,3,10,5,0,36,38,1,0,0,0,37,34,
        1,0,0,0,37,38,1,0,0,0,38,42,1,0,0,0,39,40,3,8,4,0,40,41,3,10,5,0,
        41,43,1,0,0,0,42,39,1,0,0,0,42,43,1,0,0,0,43,7,1,0,0,0,44,45,7,0,
        0,0,45,9,1,0,0,0,46,60,5,20,0,0,47,60,5,21,0,0,48,60,5,19,0,0,49,
        50,5,4,0,0,50,51,3,0,0,0,51,52,5,5,0,0,52,60,1,0,0,0,53,54,5,2,0,
        0,54,55,3,0,0,0,55,56,5,3,0,0,56,60,1,0,0,0,57,60,3,14,7,0,58,60,
        3,12,6,0,59,46,1,0,0,0,59,47,1,0,0,0,59,48,1,0,0,0,59,49,1,0,0,0,
        59,53,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,11,1,0,0,0,61,62,5,
        17,0,0,62,13,1,0,0,0,63,64,7,1,0,0,64,15,1,0,0,0,5,19,23,37,42,59
    ]

class LatexParser ( Parser ):

    grammarFileName = "LatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'{'", "'}'", "'('", "')'", "'^'", 
                     "'_'", "'!'", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", 
                     "'='", "'.'", "'~'" ]

    symbolicNames = [ "<INVALID>", "BACKSLASH", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "CARET", "UNDERSCORE", "EXCLAMATION", "ASTERISK", 
                      "SLASH", "PLUS", "MINUS", "LT", "GT", "EQUALS", "DOT", 
                      "TILDE", "FRAC", "COMMAND", "NUMBER", "IDENT", "WHITESPACE" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_fraction = 2
    RULE_scriptable = 3
    RULE_scriptOp = 4
    RULE_atom = 5
    RULE_nbsp = 6
    RULE_operator = 7

    ruleNames =  [ "expr", "term", "fraction", "scriptable", "scriptOp", 
                   "atom", "nbsp", "operator" ]

    EOF = Token.EOF
    BACKSLASH=1
    LBRACE=2
    RBRACE=3
    LPAREN=4
    RPAREN=5
    CARET=6
    UNDERSCORE=7
    EXCLAMATION=8
    ASTERISK=9
    SLASH=10
    PLUS=11
    MINUS=12
    LT=13
    GT=14
    EQUALS=15
    DOT=16
    TILDE=17
    FRAC=18
    COMMAND=19
    NUMBER=20
    IDENT=21
    WHITESPACE=22

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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.term()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194068) != 0)):
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
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.fraction()
                pass
            elif token in [2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
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
            self.state = 25
            self.match(LatexParser.FRAC)
            self.state = 26
            self.match(LatexParser.LBRACE)
            self.state = 27
            self.expr()
            self.state = 28
            self.match(LatexParser.RBRACE)
            self.state = 29
            self.match(LatexParser.LBRACE)
            self.state = 30
            self.expr()
            self.state = 31
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

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.AtomContext)
            else:
                return self.getTypedRuleContext(LatexParser.AtomContext,i)


        def scriptOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.ScriptOpContext)
            else:
                return self.getTypedRuleContext(LatexParser.ScriptOpContext,i)


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
        self.enterRule(localctx, 6, self.RULE_scriptable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.atom()
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 34
                self.scriptOp()
                self.state = 35
                self.atom()


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 39
                self.scriptOp()
                self.state = 40
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
        self.enterRule(localctx, 8, self.RULE_scriptOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(LatexParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(LatexParser.IDENT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(LatexParser.COMMAND)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(LatexParser.LPAREN)
                self.state = 50
                self.expr()
                self.state = 51
                self.match(LatexParser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(LatexParser.LBRACE)
                self.state = 54
                self.expr()
                self.state = 55
                self.match(LatexParser.RBRACE)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.operator()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
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
        self.enterRule(localctx, 12, self.RULE_nbsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130816) != 0)):
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





