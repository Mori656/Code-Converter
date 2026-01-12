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
        4,1,20,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,12,1,
        42,9,1,1,2,1,2,1,3,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,4,1,
        4,1,5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,6,1,6,1,7,1,7,1,
        7,1,7,5,7,72,8,7,10,7,12,7,75,9,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,85,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,4,
        11,97,8,11,11,11,12,11,98,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,109,8,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,0,4,2,0,12,14,16,16,1,0,8,9,1,
        0,10,11,1,0,6,7,111,0,32,1,0,0,0,2,34,1,0,0,0,4,43,1,0,0,0,6,45,
        1,0,0,0,8,54,1,0,0,0,10,56,1,0,0,0,12,65,1,0,0,0,14,67,1,0,0,0,16,
        76,1,0,0,0,18,84,1,0,0,0,20,86,1,0,0,0,22,94,1,0,0,0,24,108,1,0,
        0,0,26,110,1,0,0,0,28,112,1,0,0,0,30,114,1,0,0,0,32,33,3,2,1,0,33,
        1,1,0,0,0,34,40,3,6,3,0,35,36,3,4,2,0,36,37,3,6,3,0,37,39,1,0,0,
        0,38,35,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,3,1,
        0,0,0,42,40,1,0,0,0,43,44,7,0,0,0,44,5,1,0,0,0,45,51,3,10,5,0,46,
        47,3,8,4,0,47,48,3,10,5,0,48,50,1,0,0,0,49,46,1,0,0,0,50,53,1,0,
        0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,7,1,0,0,0,53,51,1,0,0,0,54,55,
        7,1,0,0,55,9,1,0,0,0,56,62,3,14,7,0,57,58,3,12,6,0,58,59,3,14,7,
        0,59,61,1,0,0,0,60,57,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,11,1,0,0,0,64,62,1,0,0,0,65,66,7,2,0,0,66,13,1,0,0,0,
        67,73,3,18,9,0,68,69,3,16,8,0,69,70,3,18,9,0,70,72,1,0,0,0,71,68,
        1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,15,1,0,0,0,
        75,73,1,0,0,0,76,77,7,3,0,0,77,17,1,0,0,0,78,85,3,20,10,0,79,85,
        3,22,11,0,80,85,3,26,13,0,81,85,3,28,14,0,82,85,3,30,15,0,83,85,
        3,24,12,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,
        0,84,82,1,0,0,0,84,83,1,0,0,0,85,19,1,0,0,0,86,87,5,16,0,0,87,88,
        5,2,0,0,88,89,3,0,0,0,89,90,5,3,0,0,90,91,5,2,0,0,91,92,3,0,0,0,
        92,93,5,3,0,0,93,21,1,0,0,0,94,96,5,15,0,0,95,97,3,18,9,0,96,95,
        1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,23,1,0,0,0,
        100,101,5,2,0,0,101,102,3,0,0,0,102,103,5,3,0,0,103,109,1,0,0,0,
        104,105,5,4,0,0,105,106,3,0,0,0,106,107,5,5,0,0,107,109,1,0,0,0,
        108,100,1,0,0,0,108,104,1,0,0,0,109,25,1,0,0,0,110,111,5,17,0,0,
        111,27,1,0,0,0,112,113,5,18,0,0,113,29,1,0,0,0,114,115,5,16,0,0,
        115,31,1,0,0,0,7,40,51,62,73,84,98,108
    ]

class LatexParser ( Parser ):

    grammarFileName = "LatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'{'", "'}'", "'('", "')'", "'^'", 
                     "'_'", "'+'", "'-'", "'*'", "'/'", "'='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "BACKSLASH", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "CARET", "UNDERSCORE", "PLUS", "MINUS", 
                      "STAR", "SLASH", "EQUALS", "LT", "GT", "FUNCTIONCMD", 
                      "COMMAND", "NUMBER", "IDENT", "WS", "OTHER" ]

    RULE_expr = 0
    RULE_relationExpr = 1
    RULE_relationOp = 2
    RULE_additiveExpr = 3
    RULE_addOp = 4
    RULE_multiplicativeExpr = 5
    RULE_multOp = 6
    RULE_postfixExpr = 7
    RULE_postfixOp = 8
    RULE_primaryExpr = 9
    RULE_fracExpr = 10
    RULE_functionExpr = 11
    RULE_group = 12
    RULE_numberAtom = 13
    RULE_identAtom = 14
    RULE_commandAtom = 15

    ruleNames =  [ "expr", "relationExpr", "relationOp", "additiveExpr", 
                   "addOp", "multiplicativeExpr", "multOp", "postfixExpr", 
                   "postfixOp", "primaryExpr", "fracExpr", "functionExpr", 
                   "group", "numberAtom", "identAtom", "commandAtom" ]

    EOF = Token.EOF
    BACKSLASH=1
    LBRACE=2
    RBRACE=3
    LPAREN=4
    RPAREN=5
    CARET=6
    UNDERSCORE=7
    PLUS=8
    MINUS=9
    STAR=10
    SLASH=11
    EQUALS=12
    LT=13
    GT=14
    FUNCTIONCMD=15
    COMMAND=16
    NUMBER=17
    IDENT=18
    WS=19
    OTHER=20

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

        def relationExpr(self):
            return self.getTypedRuleContext(LatexParser.RelationExprContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.relationExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.AdditiveExprContext,i)


        def relationOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.RelationOpContext)
            else:
                return self.getTypedRuleContext(LatexParser.RelationOpContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_relationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationExpr" ):
                listener.enterRelationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationExpr" ):
                listener.exitRelationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationExpr" ):
                return visitor.visitRelationExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationExpr(self):

        localctx = LatexParser.RelationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relationExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.additiveExpr()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 94208) != 0):
                self.state = 35
                self.relationOp()
                self.state = 36
                self.additiveExpr()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(LatexParser.EQUALS, 0)

        def LT(self):
            return self.getToken(LatexParser.LT, 0)

        def GT(self):
            return self.getToken(LatexParser.GT, 0)

        def COMMAND(self):
            return self.getToken(LatexParser.COMMAND, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_relationOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationOp" ):
                listener.enterRelationOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationOp" ):
                listener.exitRelationOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationOp" ):
                return visitor.visitRelationOp(self)
            else:
                return visitor.visitChildren(self)




    def relationOp(self):

        localctx = LatexParser.RelationOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 94208) != 0)):
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


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.MultiplicativeExprContext,i)


        def addOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.AddOpContext)
            else:
                return self.getTypedRuleContext(LatexParser.AddOpContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = LatexParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.multiplicativeExpr()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 46
                self.addOp()
                self.state = 47
                self.multiplicativeExpr()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(LatexParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LatexParser.MINUS, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = LatexParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
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


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.PostfixExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.PostfixExprContext,i)


        def multOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.MultOpContext)
            else:
                return self.getTypedRuleContext(LatexParser.MultOpContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = LatexParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.postfixExpr()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 57
                self.multOp()
                self.state = 58
                self.postfixExpr()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(LatexParser.STAR, 0)

        def SLASH(self):
            return self.getToken(LatexParser.SLASH, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_multOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOp" ):
                listener.enterMultOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOp" ):
                listener.exitMultOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultOp" ):
                return visitor.visitMultOp(self)
            else:
                return visitor.visitChildren(self)




    def multOp(self):

        localctx = LatexParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.PrimaryExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.PrimaryExprContext,i)


        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(LatexParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_postfixExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpr" ):
                listener.enterPostfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpr" ):
                listener.exitPostfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpr" ):
                return visitor.visitPostfixExpr(self)
            else:
                return visitor.visitChildren(self)




    def postfixExpr(self):

        localctx = LatexParser.PostfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_postfixExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.primaryExpr()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 68
                self.postfixOp()
                self.state = 69
                self.primaryExpr()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LatexParser.CARET, 0)

        def UNDERSCORE(self):
            return self.getToken(LatexParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_postfixOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixOp" ):
                listener.enterPostfixOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixOp" ):
                listener.exitPostfixOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixOp" ):
                return visitor.visitPostfixOp(self)
            else:
                return visitor.visitChildren(self)




    def postfixOp(self):

        localctx = LatexParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_postfixOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fracExpr(self):
            return self.getTypedRuleContext(LatexParser.FracExprContext,0)


        def functionExpr(self):
            return self.getTypedRuleContext(LatexParser.FunctionExprContext,0)


        def numberAtom(self):
            return self.getTypedRuleContext(LatexParser.NumberAtomContext,0)


        def identAtom(self):
            return self.getTypedRuleContext(LatexParser.IdentAtomContext,0)


        def commandAtom(self):
            return self.getTypedRuleContext(LatexParser.CommandAtomContext,0)


        def group(self):
            return self.getTypedRuleContext(LatexParser.GroupContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = LatexParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primaryExpr)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.fracExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.functionExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.numberAtom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.identAtom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.commandAtom()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.group()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FracExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(LatexParser.COMMAND, 0)

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
            return LatexParser.RULE_fracExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFracExpr" ):
                listener.enterFracExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFracExpr" ):
                listener.exitFracExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFracExpr" ):
                return visitor.visitFracExpr(self)
            else:
                return visitor.visitChildren(self)




    def fracExpr(self):

        localctx = LatexParser.FracExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fracExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(LatexParser.COMMAND)
            self.state = 87
            self.match(LatexParser.LBRACE)
            self.state = 88
            self.expr()
            self.state = 89
            self.match(LatexParser.RBRACE)
            self.state = 90
            self.match(LatexParser.LBRACE)
            self.state = 91
            self.expr()
            self.state = 92
            self.match(LatexParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTIONCMD(self):
            return self.getToken(LatexParser.FUNCTIONCMD, 0)

        def primaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.PrimaryExprContext)
            else:
                return self.getTypedRuleContext(LatexParser.PrimaryExprContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_functionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpr" ):
                return visitor.visitFunctionExpr(self)
            else:
                return visitor.visitChildren(self)




    def functionExpr(self):

        localctx = LatexParser.FunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(LatexParser.FUNCTIONCMD)
            self.state = 96 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 95
                    self.primaryExpr()

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(LatexParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LatexParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(LatexParser.RBRACE, 0)

        def LPAREN(self):
            return self.getToken(LatexParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LatexParser.RPAREN, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)




    def group(self):

        localctx = LatexParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_group)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(LatexParser.LBRACE)
                self.state = 101
                self.expr()
                self.state = 102
                self.match(LatexParser.RBRACE)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(LatexParser.LPAREN)
                self.state = 105
                self.expr()
                self.state = 106
                self.match(LatexParser.RPAREN)
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


    class NumberAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LatexParser.NUMBER, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_numberAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)




    def numberAtom(self):

        localctx = LatexParser.NumberAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_numberAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(LatexParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LatexParser.IDENT, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_identAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentAtom" ):
                listener.enterIdentAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentAtom" ):
                listener.exitIdentAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentAtom" ):
                return visitor.visitIdentAtom(self)
            else:
                return visitor.visitChildren(self)




    def identAtom(self):

        localctx = LatexParser.IdentAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LatexParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(LatexParser.COMMAND, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_commandAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandAtom" ):
                listener.enterCommandAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandAtom" ):
                listener.exitCommandAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandAtom" ):
                return visitor.visitCommandAtom(self)
            else:
                return visitor.visitChildren(self)




    def commandAtom(self):

        localctx = LatexParser.CommandAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_commandAtom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(LatexParser.COMMAND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





