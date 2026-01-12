# Generated from MarkdownParser.g4 by ANTLR 4.13.2
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
        4,1,25,327,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,81,8,1,
        1,2,5,2,84,8,2,10,2,12,2,87,9,2,1,2,1,2,5,2,91,8,2,10,2,12,2,94,
        9,2,1,2,1,2,1,3,5,3,99,8,3,10,3,12,3,102,9,3,1,3,1,3,5,3,106,8,3,
        10,3,12,3,109,9,3,1,3,1,3,1,4,5,4,114,8,4,10,4,12,4,117,9,4,1,4,
        1,4,5,4,121,8,4,10,4,12,4,124,9,4,1,4,1,4,1,5,5,5,129,8,5,10,5,12,
        5,132,9,5,1,5,1,5,5,5,136,8,5,10,5,12,5,139,9,5,1,5,1,5,1,6,5,6,
        144,8,6,10,6,12,6,147,9,6,1,6,1,6,5,6,151,8,6,10,6,12,6,154,9,6,
        1,6,1,6,1,7,5,7,159,8,7,10,7,12,7,162,9,7,1,7,1,7,5,7,166,8,7,10,
        7,12,7,169,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,181,8,
        8,1,9,1,9,1,9,1,9,3,9,187,8,9,1,10,1,10,1,10,1,10,3,10,193,8,10,
        1,11,1,11,1,11,1,11,3,11,199,8,11,1,12,1,12,1,12,1,12,3,12,205,8,
        12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,213,8,13,1,14,1,14,5,14,217,
        8,14,10,14,12,14,220,9,14,1,14,1,14,1,15,1,15,5,15,226,8,15,10,15,
        12,15,229,9,15,1,15,1,15,1,16,1,16,5,16,235,8,16,10,16,12,16,238,
        9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,5,18,249,8,18,
        10,18,12,18,252,9,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,21,4,21,264,8,21,11,21,12,21,265,1,22,4,22,269,8,22,11,22,12,22,
        270,1,22,1,22,1,23,1,23,5,23,277,8,23,10,23,12,23,280,9,23,1,23,
        1,23,1,23,1,24,4,24,286,8,24,11,24,12,24,287,1,25,4,25,291,8,25,
        11,25,12,25,292,1,26,3,26,296,8,26,1,26,1,26,5,26,300,8,26,10,26,
        12,26,303,9,26,1,26,1,26,1,27,3,27,308,8,27,1,27,1,27,5,27,312,8,
        27,10,27,12,27,315,9,27,1,27,1,27,1,28,1,28,4,28,321,8,28,11,28,
        12,28,322,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,0,358,0,63,
        1,0,0,0,2,80,1,0,0,0,4,85,1,0,0,0,6,100,1,0,0,0,8,115,1,0,0,0,10,
        130,1,0,0,0,12,145,1,0,0,0,14,160,1,0,0,0,16,180,1,0,0,0,18,186,
        1,0,0,0,20,192,1,0,0,0,22,198,1,0,0,0,24,204,1,0,0,0,26,212,1,0,
        0,0,28,214,1,0,0,0,30,223,1,0,0,0,32,232,1,0,0,0,34,241,1,0,0,0,
        36,246,1,0,0,0,38,255,1,0,0,0,40,258,1,0,0,0,42,263,1,0,0,0,44,268,
        1,0,0,0,46,274,1,0,0,0,48,285,1,0,0,0,50,290,1,0,0,0,52,295,1,0,
        0,0,54,307,1,0,0,0,56,318,1,0,0,0,58,324,1,0,0,0,60,62,3,2,1,0,61,
        60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,
        0,65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,81,3,4,2,0,69,81,3,
        6,3,0,70,81,3,8,4,0,71,81,3,10,5,0,72,81,3,12,6,0,73,81,3,14,7,0,
        74,81,3,46,23,0,75,81,3,48,24,0,76,81,3,50,25,0,77,81,3,56,28,0,
        78,81,3,42,21,0,79,81,5,14,0,0,80,68,1,0,0,0,80,69,1,0,0,0,80,70,
        1,0,0,0,80,71,1,0,0,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,
        80,75,1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,
        0,0,0,81,3,1,0,0,0,82,84,5,15,0,0,83,82,1,0,0,0,84,87,1,0,0,0,85,
        83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,92,5,6,0,
        0,89,91,3,16,8,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,
        1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,14,0,0,96,5,1,0,0,0,
        97,99,5,15,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,
        1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,107,5,5,0,0,104,106,
        3,16,8,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,
        1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,14,0,0,111,7,1,
        0,0,0,112,114,5,15,0,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,
        0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,122,5,
        4,0,0,119,121,3,16,8,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,1,
        0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,126,5,
        14,0,0,126,9,1,0,0,0,127,129,5,15,0,0,128,127,1,0,0,0,129,132,1,
        0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,130,1,
        0,0,0,133,137,5,3,0,0,134,136,3,16,8,0,135,134,1,0,0,0,136,139,1,
        0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,1,
        0,0,0,140,141,5,14,0,0,141,11,1,0,0,0,142,144,5,15,0,0,143,142,1,
        0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,
        0,0,0,147,145,1,0,0,0,148,152,5,2,0,0,149,151,3,16,8,0,150,149,1,
        0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,1,
        0,0,0,154,152,1,0,0,0,155,156,5,14,0,0,156,13,1,0,0,0,157,159,5,
        15,0,0,158,157,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,
        0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,167,5,1,0,0,164,166,3,
        16,8,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,
        0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,14,0,0,171,15,1,
        0,0,0,172,181,3,28,14,0,173,181,3,30,15,0,174,181,3,32,16,0,175,
        181,3,34,17,0,176,181,3,38,19,0,177,181,3,40,20,0,178,181,3,58,29,
        0,179,181,5,15,0,0,180,172,1,0,0,0,180,173,1,0,0,0,180,174,1,0,0,
        0,180,175,1,0,0,0,180,176,1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,
        0,180,179,1,0,0,0,181,17,1,0,0,0,182,187,3,28,14,0,183,187,3,32,
        16,0,184,187,3,36,18,0,185,187,3,58,29,0,186,182,1,0,0,0,186,183,
        1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,19,1,0,0,0,188,193,3,
        30,15,0,189,193,3,32,16,0,190,193,3,36,18,0,191,193,3,58,29,0,192,
        188,1,0,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,
        21,1,0,0,0,194,199,3,28,14,0,195,199,3,30,15,0,196,199,3,36,18,0,
        197,199,3,58,29,0,198,194,1,0,0,0,198,195,1,0,0,0,198,196,1,0,0,
        0,198,197,1,0,0,0,199,23,1,0,0,0,200,205,3,28,14,0,201,205,3,30,
        15,0,202,205,3,32,16,0,203,205,3,58,29,0,204,200,1,0,0,0,204,201,
        1,0,0,0,204,202,1,0,0,0,204,203,1,0,0,0,205,25,1,0,0,0,206,213,3,
        28,14,0,207,213,3,30,15,0,208,213,3,32,16,0,209,213,3,40,20,0,210,
        213,3,58,29,0,211,213,5,15,0,0,212,206,1,0,0,0,212,207,1,0,0,0,212,
        208,1,0,0,0,212,209,1,0,0,0,212,210,1,0,0,0,212,211,1,0,0,0,213,
        27,1,0,0,0,214,218,5,7,0,0,215,217,3,20,10,0,216,215,1,0,0,0,217,
        220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,
        218,1,0,0,0,221,222,5,7,0,0,222,29,1,0,0,0,223,227,5,10,0,0,224,
        226,3,18,9,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,
        228,1,0,0,0,228,230,1,0,0,0,229,227,1,0,0,0,230,231,5,10,0,0,231,
        31,1,0,0,0,232,236,5,13,0,0,233,235,3,22,11,0,234,233,1,0,0,0,235,
        238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,
        236,1,0,0,0,239,240,5,13,0,0,240,33,1,0,0,0,241,242,3,36,18,0,242,
        243,5,19,0,0,243,244,3,58,29,0,244,245,5,20,0,0,245,35,1,0,0,0,246,
        250,5,17,0,0,247,249,3,24,12,0,248,247,1,0,0,0,249,252,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,
        254,5,18,0,0,254,37,1,0,0,0,255,256,5,21,0,0,256,257,3,34,17,0,257,
        39,1,0,0,0,258,259,5,11,0,0,259,260,3,58,29,0,260,261,5,11,0,0,261,
        41,1,0,0,0,262,264,3,44,22,0,263,262,1,0,0,0,264,265,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,43,1,0,0,0,267,269,3,16,8,0,268,
        267,1,0,0,0,269,270,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,
        272,1,0,0,0,272,273,5,14,0,0,273,45,1,0,0,0,274,278,5,23,0,0,275,
        277,5,24,0,0,276,275,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,281,1,0,0,0,280,278,1,0,0,0,281,282,5,25,0,0,282,
        283,5,14,0,0,283,47,1,0,0,0,284,286,3,52,26,0,285,284,1,0,0,0,286,
        287,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,49,1,0,0,0,289,291,
        3,54,27,0,290,289,1,0,0,0,291,292,1,0,0,0,292,290,1,0,0,0,292,293,
        1,0,0,0,293,51,1,0,0,0,294,296,5,15,0,0,295,294,1,0,0,0,295,296,
        1,0,0,0,296,297,1,0,0,0,297,301,5,8,0,0,298,300,3,26,13,0,299,298,
        1,0,0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,304,
        1,0,0,0,303,301,1,0,0,0,304,305,5,14,0,0,305,53,1,0,0,0,306,308,
        5,15,0,0,307,306,1,0,0,0,307,308,1,0,0,0,308,309,1,0,0,0,309,313,
        5,9,0,0,310,312,3,26,13,0,311,310,1,0,0,0,312,315,1,0,0,0,313,311,
        1,0,0,0,313,314,1,0,0,0,314,316,1,0,0,0,315,313,1,0,0,0,316,317,
        5,14,0,0,317,55,1,0,0,0,318,320,5,12,0,0,319,321,3,16,8,0,320,319,
        1,0,0,0,321,322,1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,57,1,
        0,0,0,324,325,5,22,0,0,325,59,1,0,0,0,34,63,80,85,92,100,107,115,
        122,130,137,145,152,160,167,180,186,192,198,204,212,218,227,236,
        250,265,270,278,287,292,295,301,307,313,322
    ]

class MarkdownParser ( Parser ):

    grammarFileName = "MarkdownParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'**'", "<INVALID>", 
                     "<INVALID>", "'*'", "'`'", "'>'", "'~~'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'('", "')'", 
                     "'!'", "<INVALID>", "<INVALID>", "<INVALID>", "'```'" ]

    symbolicNames = [ "<INVALID>", "HEADING6", "HEADING5", "HEADING4", "HEADING3", 
                      "HEADING2", "HEADING1", "BOLD", "UNORDERED_LIST_MARKER", 
                      "ORDERED_LIST_MARKER", "ITALIC", "BACKTICK", "BLOCKQUOTE", 
                      "STRIKETHROUGH", "NEWLINE", "SPACE", "SPACESKIP", 
                      "LINK_OPEN", "LINK_CLOSE", "LINK_HREF_OPEN", "LINK_HREF_CLOSE", 
                      "IMAGE", "TEXT", "TRIPLE_BACKTICK", "CODE_BLOCK_CONTENT", 
                      "CODE_BLOCK_END" ]

    RULE_document = 0
    RULE_block = 1
    RULE_heading1 = 2
    RULE_heading2 = 3
    RULE_heading3 = 4
    RULE_heading4 = 5
    RULE_heading5 = 6
    RULE_heading6 = 7
    RULE_inlineElement = 8
    RULE_inlineElementNoItalic = 9
    RULE_inlineElementNoBold = 10
    RULE_inlineElementNoStrikethrough = 11
    RULE_inlineElementNoLink = 12
    RULE_inlineListElement = 13
    RULE_boldText = 14
    RULE_italicText = 15
    RULE_strikethroughText = 16
    RULE_link = 17
    RULE_linkText = 18
    RULE_image = 19
    RULE_codeSpan = 20
    RULE_paragraph = 21
    RULE_inlineContentLine = 22
    RULE_codeBlock = 23
    RULE_unorderedList = 24
    RULE_orderedList = 25
    RULE_unorderedListItem = 26
    RULE_orderedListItem = 27
    RULE_blockquote = 28
    RULE_text = 29

    ruleNames =  [ "document", "block", "heading1", "heading2", "heading3", 
                   "heading4", "heading5", "heading6", "inlineElement", 
                   "inlineElementNoItalic", "inlineElementNoBold", "inlineElementNoStrikethrough", 
                   "inlineElementNoLink", "inlineListElement", "boldText", 
                   "italicText", "strikethroughText", "link", "linkText", 
                   "image", "codeSpan", "paragraph", "inlineContentLine", 
                   "codeBlock", "unorderedList", "orderedList", "unorderedListItem", 
                   "orderedListItem", "blockquote", "text" ]

    EOF = Token.EOF
    HEADING6=1
    HEADING5=2
    HEADING4=3
    HEADING3=4
    HEADING2=5
    HEADING1=6
    BOLD=7
    UNORDERED_LIST_MARKER=8
    ORDERED_LIST_MARKER=9
    ITALIC=10
    BACKTICK=11
    BLOCKQUOTE=12
    STRIKETHROUGH=13
    NEWLINE=14
    SPACE=15
    SPACESKIP=16
    LINK_OPEN=17
    LINK_CLOSE=18
    LINK_HREF_OPEN=19
    LINK_HREF_CLOSE=20
    IMAGE=21
    TEXT=22
    TRIPLE_BACKTICK=23
    CODE_BLOCK_CONTENT=24
    CODE_BLOCK_END=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MarkdownParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.BlockContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.BlockContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = MarkdownParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14876670) != 0):
                self.state = 60
                self.block()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(MarkdownParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def heading1(self):
            return self.getTypedRuleContext(MarkdownParser.Heading1Context,0)


        def heading2(self):
            return self.getTypedRuleContext(MarkdownParser.Heading2Context,0)


        def heading3(self):
            return self.getTypedRuleContext(MarkdownParser.Heading3Context,0)


        def heading4(self):
            return self.getTypedRuleContext(MarkdownParser.Heading4Context,0)


        def heading5(self):
            return self.getTypedRuleContext(MarkdownParser.Heading5Context,0)


        def heading6(self):
            return self.getTypedRuleContext(MarkdownParser.Heading6Context,0)


        def codeBlock(self):
            return self.getTypedRuleContext(MarkdownParser.CodeBlockContext,0)


        def unorderedList(self):
            return self.getTypedRuleContext(MarkdownParser.UnorderedListContext,0)


        def orderedList(self):
            return self.getTypedRuleContext(MarkdownParser.OrderedListContext,0)


        def blockquote(self):
            return self.getTypedRuleContext(MarkdownParser.BlockquoteContext,0)


        def paragraph(self):
            return self.getTypedRuleContext(MarkdownParser.ParagraphContext,0)


        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MarkdownParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.heading1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.heading2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.heading3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.heading4()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.heading5()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.heading6()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.codeBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.unorderedList()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.orderedList()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.blockquote()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.paragraph()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 79
                self.match(MarkdownParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING1(self):
            return self.getToken(MarkdownParser.HEADING1, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading1" ):
                listener.enterHeading1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading1" ):
                listener.exitHeading1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading1" ):
                return visitor.visitHeading1(self)
            else:
                return visitor.visitChildren(self)




    def heading1(self):

        localctx = MarkdownParser.Heading1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_heading1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 82
                self.match(MarkdownParser.SPACE)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(MarkdownParser.HEADING1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 89
                self.inlineElement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING2(self):
            return self.getToken(MarkdownParser.HEADING2, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading2" ):
                listener.enterHeading2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading2" ):
                listener.exitHeading2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading2" ):
                return visitor.visitHeading2(self)
            else:
                return visitor.visitChildren(self)




    def heading2(self):

        localctx = MarkdownParser.Heading2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_heading2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 97
                self.match(MarkdownParser.SPACE)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(MarkdownParser.HEADING2)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 104
                self.inlineElement()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING3(self):
            return self.getToken(MarkdownParser.HEADING3, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading3" ):
                listener.enterHeading3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading3" ):
                listener.exitHeading3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading3" ):
                return visitor.visitHeading3(self)
            else:
                return visitor.visitChildren(self)




    def heading3(self):

        localctx = MarkdownParser.Heading3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_heading3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 112
                self.match(MarkdownParser.SPACE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(MarkdownParser.HEADING3)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 119
                self.inlineElement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING4(self):
            return self.getToken(MarkdownParser.HEADING4, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading4" ):
                listener.enterHeading4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading4" ):
                listener.exitHeading4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading4" ):
                return visitor.visitHeading4(self)
            else:
                return visitor.visitChildren(self)




    def heading4(self):

        localctx = MarkdownParser.Heading4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_heading4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 127
                self.match(MarkdownParser.SPACE)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(MarkdownParser.HEADING4)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 134
                self.inlineElement()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING5(self):
            return self.getToken(MarkdownParser.HEADING5, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading5" ):
                listener.enterHeading5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading5" ):
                listener.exitHeading5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading5" ):
                return visitor.visitHeading5(self)
            else:
                return visitor.visitChildren(self)




    def heading5(self):

        localctx = MarkdownParser.Heading5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_heading5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 142
                self.match(MarkdownParser.SPACE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(MarkdownParser.HEADING5)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 149
                self.inlineElement()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING6(self):
            return self.getToken(MarkdownParser.HEADING6, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.SPACE)
            else:
                return self.getToken(MarkdownParser.SPACE, i)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading6" ):
                listener.enterHeading6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading6" ):
                listener.exitHeading6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading6" ):
                return visitor.visitHeading6(self)
            else:
                return visitor.visitChildren(self)




    def heading6(self):

        localctx = MarkdownParser.Heading6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_heading6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 157
                self.match(MarkdownParser.SPACE)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(MarkdownParser.HEADING6)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0):
                self.state = 164
                self.inlineElement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldText(self):
            return self.getTypedRuleContext(MarkdownParser.BoldTextContext,0)


        def italicText(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicTextContext,0)


        def strikethroughText(self):
            return self.getTypedRuleContext(MarkdownParser.StrikethroughTextContext,0)


        def link(self):
            return self.getTypedRuleContext(MarkdownParser.LinkContext,0)


        def image(self):
            return self.getTypedRuleContext(MarkdownParser.ImageContext,0)


        def codeSpan(self):
            return self.getTypedRuleContext(MarkdownParser.CodeSpanContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def SPACE(self):
            return self.getToken(MarkdownParser.SPACE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineElement" ):
                listener.enterInlineElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineElement" ):
                listener.exitInlineElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineElement" ):
                return visitor.visitInlineElement(self)
            else:
                return visitor.visitChildren(self)




    def inlineElement(self):

        localctx = MarkdownParser.InlineElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_inlineElement)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.link()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.image()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.codeSpan()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.text()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 179
                self.match(MarkdownParser.SPACE)
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


    class InlineElementNoItalicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldText(self):
            return self.getTypedRuleContext(MarkdownParser.BoldTextContext,0)


        def strikethroughText(self):
            return self.getTypedRuleContext(MarkdownParser.StrikethroughTextContext,0)


        def linkText(self):
            return self.getTypedRuleContext(MarkdownParser.LinkTextContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineElementNoItalic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineElementNoItalic" ):
                listener.enterInlineElementNoItalic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineElementNoItalic" ):
                listener.exitInlineElementNoItalic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineElementNoItalic" ):
                return visitor.visitInlineElementNoItalic(self)
            else:
                return visitor.visitChildren(self)




    def inlineElementNoItalic(self):

        localctx = MarkdownParser.InlineElementNoItalicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_inlineElementNoItalic)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.boldText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.linkText()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.text()
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


    class InlineElementNoBoldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def italicText(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicTextContext,0)


        def strikethroughText(self):
            return self.getTypedRuleContext(MarkdownParser.StrikethroughTextContext,0)


        def linkText(self):
            return self.getTypedRuleContext(MarkdownParser.LinkTextContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineElementNoBold

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineElementNoBold" ):
                listener.enterInlineElementNoBold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineElementNoBold" ):
                listener.exitInlineElementNoBold(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineElementNoBold" ):
                return visitor.visitInlineElementNoBold(self)
            else:
                return visitor.visitChildren(self)




    def inlineElementNoBold(self):

        localctx = MarkdownParser.InlineElementNoBoldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_inlineElementNoBold)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.linkText()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.text()
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


    class InlineElementNoStrikethroughContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldText(self):
            return self.getTypedRuleContext(MarkdownParser.BoldTextContext,0)


        def italicText(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicTextContext,0)


        def linkText(self):
            return self.getTypedRuleContext(MarkdownParser.LinkTextContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineElementNoStrikethrough

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineElementNoStrikethrough" ):
                listener.enterInlineElementNoStrikethrough(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineElementNoStrikethrough" ):
                listener.exitInlineElementNoStrikethrough(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineElementNoStrikethrough" ):
                return visitor.visitInlineElementNoStrikethrough(self)
            else:
                return visitor.visitChildren(self)




    def inlineElementNoStrikethrough(self):

        localctx = MarkdownParser.InlineElementNoStrikethroughContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_inlineElementNoStrikethrough)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.italicText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.linkText()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.text()
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


    class InlineElementNoLinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldText(self):
            return self.getTypedRuleContext(MarkdownParser.BoldTextContext,0)


        def italicText(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicTextContext,0)


        def strikethroughText(self):
            return self.getTypedRuleContext(MarkdownParser.StrikethroughTextContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineElementNoLink

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineElementNoLink" ):
                listener.enterInlineElementNoLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineElementNoLink" ):
                listener.exitInlineElementNoLink(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineElementNoLink" ):
                return visitor.visitInlineElementNoLink(self)
            else:
                return visitor.visitChildren(self)




    def inlineElementNoLink(self):

        localctx = MarkdownParser.InlineElementNoLinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inlineElementNoLink)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.strikethroughText()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.text()
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


    class InlineListElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boldText(self):
            return self.getTypedRuleContext(MarkdownParser.BoldTextContext,0)


        def italicText(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicTextContext,0)


        def strikethroughText(self):
            return self.getTypedRuleContext(MarkdownParser.StrikethroughTextContext,0)


        def codeSpan(self):
            return self.getTypedRuleContext(MarkdownParser.CodeSpanContext,0)


        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def SPACE(self):
            return self.getToken(MarkdownParser.SPACE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineListElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineListElement" ):
                listener.enterInlineListElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineListElement" ):
                listener.exitInlineListElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineListElement" ):
                return visitor.visitInlineListElement(self)
            else:
                return visitor.visitChildren(self)




    def inlineListElement(self):

        localctx = MarkdownParser.InlineListElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_inlineListElement)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.strikethroughText()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.codeSpan()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.text()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.match(MarkdownParser.SPACE)
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


    class BoldTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLD(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.BOLD)
            else:
                return self.getToken(MarkdownParser.BOLD, i)

        def inlineElementNoBold(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementNoBoldContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementNoBoldContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_boldText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoldText" ):
                listener.enterBoldText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoldText" ):
                listener.exitBoldText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoldText" ):
                return visitor.visitBoldText(self)
            else:
                return visitor.visitChildren(self)




    def boldText(self):

        localctx = MarkdownParser.BoldTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boldText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MarkdownParser.BOLD)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4334592) != 0):
                self.state = 215
                self.inlineElementNoBold()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self.match(MarkdownParser.BOLD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItalicTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITALIC(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.ITALIC)
            else:
                return self.getToken(MarkdownParser.ITALIC, i)

        def inlineElementNoItalic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementNoItalicContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementNoItalicContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_italicText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItalicText" ):
                listener.enterItalicText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItalicText" ):
                listener.exitItalicText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItalicText" ):
                return visitor.visitItalicText(self)
            else:
                return visitor.visitChildren(self)




    def italicText(self):

        localctx = MarkdownParser.ItalicTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_italicText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MarkdownParser.ITALIC)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4333696) != 0):
                self.state = 224
                self.inlineElementNoItalic()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self.match(MarkdownParser.ITALIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrikethroughTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRIKETHROUGH(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.STRIKETHROUGH)
            else:
                return self.getToken(MarkdownParser.STRIKETHROUGH, i)

        def inlineElementNoStrikethrough(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementNoStrikethroughContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementNoStrikethroughContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_strikethroughText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrikethroughText" ):
                listener.enterStrikethroughText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrikethroughText" ):
                listener.exitStrikethroughText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrikethroughText" ):
                return visitor.visitStrikethroughText(self)
            else:
                return visitor.visitChildren(self)




    def strikethroughText(self):

        localctx = MarkdownParser.StrikethroughTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_strikethroughText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MarkdownParser.STRIKETHROUGH)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4326528) != 0):
                self.state = 233
                self.inlineElementNoStrikethrough()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(MarkdownParser.STRIKETHROUGH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linkText(self):
            return self.getTypedRuleContext(MarkdownParser.LinkTextContext,0)


        def LINK_HREF_OPEN(self):
            return self.getToken(MarkdownParser.LINK_HREF_OPEN, 0)

        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def LINK_HREF_CLOSE(self):
            return self.getToken(MarkdownParser.LINK_HREF_CLOSE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = MarkdownParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.linkText()
            self.state = 242
            self.match(MarkdownParser.LINK_HREF_OPEN)
            self.state = 243
            self.text()
            self.state = 244
            self.match(MarkdownParser.LINK_HREF_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINK_OPEN(self):
            return self.getToken(MarkdownParser.LINK_OPEN, 0)

        def LINK_CLOSE(self):
            return self.getToken(MarkdownParser.LINK_CLOSE, 0)

        def inlineElementNoLink(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementNoLinkContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementNoLinkContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_linkText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkText" ):
                listener.enterLinkText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkText" ):
                listener.exitLinkText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkText" ):
                return visitor.visitLinkText(self)
            else:
                return visitor.visitChildren(self)




    def linkText(self):

        localctx = MarkdownParser.LinkTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_linkText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MarkdownParser.LINK_OPEN)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4203648) != 0):
                self.state = 247
                self.inlineElementNoLink()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.match(MarkdownParser.LINK_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMAGE(self):
            return self.getToken(MarkdownParser.IMAGE, 0)

        def link(self):
            return self.getTypedRuleContext(MarkdownParser.LinkContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_image

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage" ):
                listener.enterImage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage" ):
                listener.exitImage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImage" ):
                return visitor.visitImage(self)
            else:
                return visitor.visitChildren(self)




    def image(self):

        localctx = MarkdownParser.ImageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_image)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MarkdownParser.IMAGE)
            self.state = 256
            self.link()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeSpanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKTICK(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.BACKTICK)
            else:
                return self.getToken(MarkdownParser.BACKTICK, i)

        def text(self):
            return self.getTypedRuleContext(MarkdownParser.TextContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_codeSpan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeSpan" ):
                listener.enterCodeSpan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeSpan" ):
                listener.exitCodeSpan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeSpan" ):
                return visitor.visitCodeSpan(self)
            else:
                return visitor.visitChildren(self)




    def codeSpan(self):

        localctx = MarkdownParser.CodeSpanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_codeSpan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MarkdownParser.BACKTICK)
            self.state = 259
            self.text()
            self.state = 260
            self.match(MarkdownParser.BACKTICK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inlineContentLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineContentLineContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineContentLineContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagraph" ):
                return visitor.visitParagraph(self)
            else:
                return visitor.visitChildren(self)




    def paragraph(self):

        localctx = MarkdownParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paragraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 262
                    self.inlineContentLine()

                else:
                    raise NoViableAltException(self)
                self.state = 265 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineContentLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_inlineContentLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineContentLine" ):
                listener.enterInlineContentLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineContentLine" ):
                listener.exitInlineContentLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineContentLine" ):
                return visitor.visitInlineContentLine(self)
            else:
                return visitor.visitChildren(self)




    def inlineContentLine(self):

        localctx = MarkdownParser.InlineContentLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_inlineContentLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 267
                self.inlineElement()
                self.state = 270 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6466688) != 0)):
                    break

            self.state = 272
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRIPLE_BACKTICK(self):
            return self.getToken(MarkdownParser.TRIPLE_BACKTICK, 0)

        def CODE_BLOCK_END(self):
            return self.getToken(MarkdownParser.CODE_BLOCK_END, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def CODE_BLOCK_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.CODE_BLOCK_CONTENT)
            else:
                return self.getToken(MarkdownParser.CODE_BLOCK_CONTENT, i)

        def getRuleIndex(self):
            return MarkdownParser.RULE_codeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeBlock" ):
                listener.enterCodeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeBlock" ):
                listener.exitCodeBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeBlock" ):
                return visitor.visitCodeBlock(self)
            else:
                return visitor.visitChildren(self)




    def codeBlock(self):

        localctx = MarkdownParser.CodeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_codeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MarkdownParser.TRIPLE_BACKTICK)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 275
                self.match(MarkdownParser.CODE_BLOCK_CONTENT)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
            self.match(MarkdownParser.CODE_BLOCK_END)
            self.state = 282
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnorderedListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unorderedListItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.UnorderedListItemContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.UnorderedListItemContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_unorderedList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnorderedList" ):
                listener.enterUnorderedList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnorderedList" ):
                listener.exitUnorderedList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnorderedList" ):
                return visitor.visitUnorderedList(self)
            else:
                return visitor.visitChildren(self)




    def unorderedList(self):

        localctx = MarkdownParser.UnorderedListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unorderedList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 284
                    self.unorderedListItem()

                else:
                    raise NoViableAltException(self)
                self.state = 287 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderedListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderedListItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.OrderedListItemContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.OrderedListItemContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_orderedList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderedList" ):
                listener.enterOrderedList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderedList" ):
                listener.exitOrderedList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderedList" ):
                return visitor.visitOrderedList(self)
            else:
                return visitor.visitChildren(self)




    def orderedList(self):

        localctx = MarkdownParser.OrderedListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_orderedList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 289
                    self.orderedListItem()

                else:
                    raise NoViableAltException(self)
                self.state = 292 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnorderedListItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNORDERED_LIST_MARKER(self):
            return self.getToken(MarkdownParser.UNORDERED_LIST_MARKER, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self):
            return self.getToken(MarkdownParser.SPACE, 0)

        def inlineListElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineListElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineListElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_unorderedListItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnorderedListItem" ):
                listener.enterUnorderedListItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnorderedListItem" ):
                listener.exitUnorderedListItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnorderedListItem" ):
                return visitor.visitUnorderedListItem(self)
            else:
                return visitor.visitChildren(self)




    def unorderedListItem(self):

        localctx = MarkdownParser.UnorderedListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unorderedListItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 294
                self.match(MarkdownParser.SPACE)


            self.state = 297
            self.match(MarkdownParser.UNORDERED_LIST_MARKER)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4238464) != 0):
                self.state = 298
                self.inlineListElement()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 304
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderedListItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDERED_LIST_MARKER(self):
            return self.getToken(MarkdownParser.ORDERED_LIST_MARKER, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def SPACE(self):
            return self.getToken(MarkdownParser.SPACE, 0)

        def inlineListElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineListElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineListElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_orderedListItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderedListItem" ):
                listener.enterOrderedListItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderedListItem" ):
                listener.exitOrderedListItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderedListItem" ):
                return visitor.visitOrderedListItem(self)
            else:
                return visitor.visitChildren(self)




    def orderedListItem(self):

        localctx = MarkdownParser.OrderedListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_orderedListItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 306
                self.match(MarkdownParser.SPACE)


            self.state = 309
            self.match(MarkdownParser.ORDERED_LIST_MARKER)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4238464) != 0):
                self.state = 310
                self.inlineListElement()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCKQUOTE(self):
            return self.getToken(MarkdownParser.BLOCKQUOTE, 0)

        def inlineElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.InlineElementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.InlineElementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_blockquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockquote" ):
                listener.enterBlockquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockquote" ):
                listener.exitBlockquote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockquote" ):
                return visitor.visitBlockquote(self)
            else:
                return visitor.visitChildren(self)




    def blockquote(self):

        localctx = MarkdownParser.BlockquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blockquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MarkdownParser.BLOCKQUOTE)
            self.state = 320 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 319
                    self.inlineElement()

                else:
                    raise NoViableAltException(self)
                self.state = 322 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(MarkdownParser.TEXT, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = MarkdownParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MarkdownParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





