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
        4,1,26,332,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,83,8,1,1,2,5,2,86,8,2,10,2,12,2,89,9,2,1,2,1,2,5,2,93,8,2,10,2,
        12,2,96,9,2,1,2,1,2,1,3,5,3,101,8,3,10,3,12,3,104,9,3,1,3,1,3,5,
        3,108,8,3,10,3,12,3,111,9,3,1,3,1,3,1,4,5,4,116,8,4,10,4,12,4,119,
        9,4,1,4,1,4,5,4,123,8,4,10,4,12,4,126,9,4,1,4,1,4,1,5,5,5,131,8,
        5,10,5,12,5,134,9,5,1,5,1,5,5,5,138,8,5,10,5,12,5,141,9,5,1,5,1,
        5,1,6,5,6,146,8,6,10,6,12,6,149,9,6,1,6,1,6,5,6,153,8,6,10,6,12,
        6,156,9,6,1,6,1,6,1,7,5,7,161,8,7,10,7,12,7,164,9,7,1,7,1,7,5,7,
        168,8,7,10,7,12,7,171,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,184,8,8,1,9,1,9,1,9,1,9,3,9,190,8,9,1,10,1,10,1,10,1,10,
        3,10,196,8,10,1,11,1,11,1,11,1,11,3,11,202,8,11,1,12,1,12,1,12,1,
        12,3,12,208,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,216,8,13,1,14,
        1,14,5,14,220,8,14,10,14,12,14,223,9,14,1,14,1,14,1,15,1,15,5,15,
        229,8,15,10,15,12,15,232,9,15,1,15,1,15,1,16,1,16,5,16,238,8,16,
        10,16,12,16,241,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        5,18,252,8,18,10,18,12,18,255,9,18,1,18,1,18,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,21,4,21,267,8,21,11,21,12,21,268,1,22,4,22,272,
        8,22,11,22,12,22,273,1,22,1,22,1,23,1,23,5,23,280,8,23,10,23,12,
        23,283,9,23,1,23,1,23,1,23,1,24,4,24,289,8,24,11,24,12,24,290,1,
        25,4,25,294,8,25,11,25,12,25,295,1,26,3,26,299,8,26,1,26,1,26,5,
        26,303,8,26,10,26,12,26,306,9,26,1,26,1,26,1,27,3,27,311,8,27,1,
        27,1,27,5,27,315,8,27,10,27,12,27,318,9,27,1,27,1,27,1,28,1,28,4,
        28,324,8,28,11,28,12,28,325,1,29,1,29,1,30,1,30,1,30,0,0,31,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,0,0,363,0,65,1,0,0,0,2,82,1,0,0,0,4,87,1,0,0,0,
        6,102,1,0,0,0,8,117,1,0,0,0,10,132,1,0,0,0,12,147,1,0,0,0,14,162,
        1,0,0,0,16,183,1,0,0,0,18,189,1,0,0,0,20,195,1,0,0,0,22,201,1,0,
        0,0,24,207,1,0,0,0,26,215,1,0,0,0,28,217,1,0,0,0,30,226,1,0,0,0,
        32,235,1,0,0,0,34,244,1,0,0,0,36,249,1,0,0,0,38,258,1,0,0,0,40,261,
        1,0,0,0,42,266,1,0,0,0,44,271,1,0,0,0,46,277,1,0,0,0,48,288,1,0,
        0,0,50,293,1,0,0,0,52,298,1,0,0,0,54,310,1,0,0,0,56,321,1,0,0,0,
        58,327,1,0,0,0,60,329,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,
        1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,
        68,69,5,0,0,1,69,1,1,0,0,0,70,83,3,4,2,0,71,83,3,6,3,0,72,83,3,8,
        4,0,73,83,3,10,5,0,74,83,3,12,6,0,75,83,3,14,7,0,76,83,3,46,23,0,
        77,83,3,48,24,0,78,83,3,50,25,0,79,83,3,56,28,0,80,83,3,42,21,0,
        81,83,5,14,0,0,82,70,1,0,0,0,82,71,1,0,0,0,82,72,1,0,0,0,82,73,1,
        0,0,0,82,74,1,0,0,0,82,75,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,0,82,
        78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,3,1,0,0,
        0,84,86,5,15,0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,
        1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,94,5,6,0,0,91,93,3,16,8,0,
        92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,
        0,0,0,96,94,1,0,0,0,97,98,5,14,0,0,98,5,1,0,0,0,99,101,5,15,0,0,
        100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,
        105,1,0,0,0,104,102,1,0,0,0,105,109,5,5,0,0,106,108,3,16,8,0,107,
        106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        112,1,0,0,0,111,109,1,0,0,0,112,113,5,14,0,0,113,7,1,0,0,0,114,116,
        5,15,0,0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,
        1,0,0,0,118,120,1,0,0,0,119,117,1,0,0,0,120,124,5,4,0,0,121,123,
        3,16,8,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,14,0,0,128,9,1,
        0,0,0,129,131,5,15,0,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,1,
        0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,135,139,5,
        3,0,0,136,138,3,16,8,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,
        0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,5,
        14,0,0,143,11,1,0,0,0,144,146,5,15,0,0,145,144,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,
        0,0,0,150,154,5,2,0,0,151,153,3,16,8,0,152,151,1,0,0,0,153,156,1,
        0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,154,1,
        0,0,0,157,158,5,14,0,0,158,13,1,0,0,0,159,161,5,15,0,0,160,159,1,
        0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,165,1,
        0,0,0,164,162,1,0,0,0,165,169,5,1,0,0,166,168,3,16,8,0,167,166,1,
        0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,1,
        0,0,0,171,169,1,0,0,0,172,173,5,14,0,0,173,15,1,0,0,0,174,184,3,
        28,14,0,175,184,3,30,15,0,176,184,3,32,16,0,177,184,3,34,17,0,178,
        184,3,38,19,0,179,184,3,40,20,0,180,184,3,58,29,0,181,184,3,60,30,
        0,182,184,5,15,0,0,183,174,1,0,0,0,183,175,1,0,0,0,183,176,1,0,0,
        0,183,177,1,0,0,0,183,178,1,0,0,0,183,179,1,0,0,0,183,180,1,0,0,
        0,183,181,1,0,0,0,183,182,1,0,0,0,184,17,1,0,0,0,185,190,3,28,14,
        0,186,190,3,32,16,0,187,190,3,36,18,0,188,190,3,60,30,0,189,185,
        1,0,0,0,189,186,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,19,1,
        0,0,0,191,196,3,30,15,0,192,196,3,32,16,0,193,196,3,36,18,0,194,
        196,3,60,30,0,195,191,1,0,0,0,195,192,1,0,0,0,195,193,1,0,0,0,195,
        194,1,0,0,0,196,21,1,0,0,0,197,202,3,28,14,0,198,202,3,30,15,0,199,
        202,3,36,18,0,200,202,3,60,30,0,201,197,1,0,0,0,201,198,1,0,0,0,
        201,199,1,0,0,0,201,200,1,0,0,0,202,23,1,0,0,0,203,208,3,28,14,0,
        204,208,3,30,15,0,205,208,3,32,16,0,206,208,3,60,30,0,207,203,1,
        0,0,0,207,204,1,0,0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,25,1,0,
        0,0,209,216,3,28,14,0,210,216,3,30,15,0,211,216,3,32,16,0,212,216,
        3,40,20,0,213,216,3,60,30,0,214,216,5,15,0,0,215,209,1,0,0,0,215,
        210,1,0,0,0,215,211,1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,215,
        214,1,0,0,0,216,27,1,0,0,0,217,221,5,7,0,0,218,220,3,20,10,0,219,
        218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,
        224,1,0,0,0,223,221,1,0,0,0,224,225,5,7,0,0,225,29,1,0,0,0,226,230,
        5,10,0,0,227,229,3,18,9,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,
        1,0,0,0,230,231,1,0,0,0,231,233,1,0,0,0,232,230,1,0,0,0,233,234,
        5,10,0,0,234,31,1,0,0,0,235,239,5,13,0,0,236,238,3,22,11,0,237,236,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,
        1,0,0,0,241,239,1,0,0,0,242,243,5,13,0,0,243,33,1,0,0,0,244,245,
        3,36,18,0,245,246,5,19,0,0,246,247,3,60,30,0,247,248,5,20,0,0,248,
        35,1,0,0,0,249,253,5,17,0,0,250,252,3,24,12,0,251,250,1,0,0,0,252,
        255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,
        253,1,0,0,0,256,257,5,18,0,0,257,37,1,0,0,0,258,259,5,21,0,0,259,
        260,3,34,17,0,260,39,1,0,0,0,261,262,5,11,0,0,262,263,3,60,30,0,
        263,264,5,11,0,0,264,41,1,0,0,0,265,267,3,44,22,0,266,265,1,0,0,
        0,267,268,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,43,1,0,0,0,
        270,272,3,16,8,0,271,270,1,0,0,0,272,273,1,0,0,0,273,271,1,0,0,0,
        273,274,1,0,0,0,274,275,1,0,0,0,275,276,5,14,0,0,276,45,1,0,0,0,
        277,281,5,24,0,0,278,280,5,25,0,0,279,278,1,0,0,0,280,283,1,0,0,
        0,281,279,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,0,283,281,1,0,0,
        0,284,285,5,26,0,0,285,286,5,14,0,0,286,47,1,0,0,0,287,289,3,52,
        26,0,288,287,1,0,0,0,289,290,1,0,0,0,290,288,1,0,0,0,290,291,1,0,
        0,0,291,49,1,0,0,0,292,294,3,54,27,0,293,292,1,0,0,0,294,295,1,0,
        0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,51,1,0,0,0,297,299,5,15,
        0,0,298,297,1,0,0,0,298,299,1,0,0,0,299,300,1,0,0,0,300,304,5,8,
        0,0,301,303,3,26,13,0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,1,
        0,0,0,304,305,1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,0,307,308,5,
        14,0,0,308,53,1,0,0,0,309,311,5,15,0,0,310,309,1,0,0,0,310,311,1,
        0,0,0,311,312,1,0,0,0,312,316,5,9,0,0,313,315,3,26,13,0,314,313,
        1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,319,
        1,0,0,0,318,316,1,0,0,0,319,320,5,14,0,0,320,55,1,0,0,0,321,323,
        5,12,0,0,322,324,3,16,8,0,323,322,1,0,0,0,324,325,1,0,0,0,325,323,
        1,0,0,0,325,326,1,0,0,0,326,57,1,0,0,0,327,328,5,22,0,0,328,59,1,
        0,0,0,329,330,5,23,0,0,330,61,1,0,0,0,34,65,82,87,94,102,109,117,
        124,132,139,147,154,162,169,183,189,195,201,207,215,221,230,239,
        253,268,273,281,290,295,298,304,310,316,325
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
                     "'!'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'```'" ]

    symbolicNames = [ "<INVALID>", "HEADING6", "HEADING5", "HEADING4", "HEADING3", 
                      "HEADING2", "HEADING1", "BOLD", "UNORDERED_LIST_MARKER", 
                      "ORDERED_LIST_MARKER", "ITALIC", "BACKTICK", "BLOCKQUOTE", 
                      "STRIKETHROUGH", "NEWLINE", "SPACE", "SPACESKIP", 
                      "LINK_OPEN", "LINK_CLOSE", "LINK_HREF_OPEN", "LINK_HREF_CLOSE", 
                      "IMAGE", "BREAKLINE", "TEXT", "TRIPLE_BACKTICK", "CODE_BLOCK_CONTENT", 
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
    RULE_breakline = 29
    RULE_text = 30

    ruleNames =  [ "document", "block", "heading1", "heading2", "heading3", 
                   "heading4", "heading5", "heading6", "inlineElement", 
                   "inlineElementNoItalic", "inlineElementNoBold", "inlineElementNoStrikethrough", 
                   "inlineElementNoLink", "inlineListElement", "boldText", 
                   "italicText", "strikethroughText", "link", "linkText", 
                   "image", "codeSpan", "paragraph", "inlineContentLine", 
                   "codeBlock", "unorderedList", "orderedList", "unorderedListItem", 
                   "orderedListItem", "blockquote", "breakline", "text" ]

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
    BREAKLINE=22
    TEXT=23
    TRIPLE_BACKTICK=24
    CODE_BLOCK_CONTENT=25
    CODE_BLOCK_END=26

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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31653886) != 0):
                self.state = 62
                self.block()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.heading1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.heading2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.heading3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.heading4()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.heading5()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.heading6()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.codeBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.unorderedList()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.orderedList()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 79
                self.blockquote()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 80
                self.paragraph()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 81
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
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 84
                self.match(MarkdownParser.SPACE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(MarkdownParser.HEADING1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 91
                self.inlineElement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 99
                self.match(MarkdownParser.SPACE)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(MarkdownParser.HEADING2)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 106
                self.inlineElement()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 114
                self.match(MarkdownParser.SPACE)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(MarkdownParser.HEADING3)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 121
                self.inlineElement()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 129
                self.match(MarkdownParser.SPACE)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(MarkdownParser.HEADING4)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 136
                self.inlineElement()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
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
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 144
                self.match(MarkdownParser.SPACE)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(MarkdownParser.HEADING5)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 151
                self.inlineElement()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
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
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 159
                self.match(MarkdownParser.SPACE)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(MarkdownParser.HEADING6)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0):
                self.state = 166
                self.inlineElement()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
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


        def breakline(self):
            return self.getTypedRuleContext(MarkdownParser.BreaklineContext,0)


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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.link()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.image()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.codeSpan()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.breakline()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.text()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.boldText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.linkText()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.strikethroughText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.linkText()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.italicText()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.linkText()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
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
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.strikethroughText()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.boldText()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.italicText()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.strikethroughText()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.codeSpan()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.text()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
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
            self.state = 217
            self.match(MarkdownParser.BOLD)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8528896) != 0):
                self.state = 218
                self.inlineElementNoBold()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
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
            self.state = 226
            self.match(MarkdownParser.ITALIC)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8528000) != 0):
                self.state = 227
                self.inlineElementNoItalic()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
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
            self.state = 235
            self.match(MarkdownParser.STRIKETHROUGH)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8520832) != 0):
                self.state = 236
                self.inlineElementNoStrikethrough()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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
            self.state = 244
            self.linkText()
            self.state = 245
            self.match(MarkdownParser.LINK_HREF_OPEN)
            self.state = 246
            self.text()
            self.state = 247
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
            self.state = 249
            self.match(MarkdownParser.LINK_OPEN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8397952) != 0):
                self.state = 250
                self.inlineElementNoLink()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
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
            self.state = 258
            self.match(MarkdownParser.IMAGE)
            self.state = 259
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
            self.state = 261
            self.match(MarkdownParser.BACKTICK)
            self.state = 262
            self.text()
            self.state = 263
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
            self.state = 266 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 265
                    self.inlineContentLine()

                else:
                    raise NoViableAltException(self)
                self.state = 268 
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
            self.state = 271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 270
                self.inlineElement()
                self.state = 273 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14855296) != 0)):
                    break

            self.state = 275
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
            self.state = 277
            self.match(MarkdownParser.TRIPLE_BACKTICK)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 278
                self.match(MarkdownParser.CODE_BLOCK_CONTENT)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.match(MarkdownParser.CODE_BLOCK_END)
            self.state = 285
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
            self.state = 288 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 287
                    self.unorderedListItem()

                else:
                    raise NoViableAltException(self)
                self.state = 290 
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
            self.state = 293 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 292
                    self.orderedListItem()

                else:
                    raise NoViableAltException(self)
                self.state = 295 
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
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 297
                self.match(MarkdownParser.SPACE)


            self.state = 300
            self.match(MarkdownParser.UNORDERED_LIST_MARKER)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8432768) != 0):
                self.state = 301
                self.inlineListElement()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 309
                self.match(MarkdownParser.SPACE)


            self.state = 312
            self.match(MarkdownParser.ORDERED_LIST_MARKER)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8432768) != 0):
                self.state = 313
                self.inlineListElement()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
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
            self.state = 321
            self.match(MarkdownParser.BLOCKQUOTE)
            self.state = 323 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 322
                    self.inlineElement()

                else:
                    raise NoViableAltException(self)
                self.state = 325 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreaklineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAKLINE(self):
            return self.getToken(MarkdownParser.BREAKLINE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_breakline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakline" ):
                listener.enterBreakline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakline" ):
                listener.exitBreakline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakline" ):
                return visitor.visitBreakline(self)
            else:
                return visitor.visitChildren(self)




    def breakline(self):

        localctx = MarkdownParser.BreaklineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MarkdownParser.BREAKLINE)
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
        self.enterRule(localctx, 60, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MarkdownParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





