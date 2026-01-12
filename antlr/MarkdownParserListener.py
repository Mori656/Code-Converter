# Generated from MarkdownParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkdownParser import MarkdownParser
else:
    from MarkdownParser import MarkdownParser

# This class defines a complete listener for a parse tree produced by MarkdownParser.
class MarkdownParserListener(ParseTreeListener):

    # Enter a parse tree produced by MarkdownParser#document.
    def enterDocument(self, ctx:MarkdownParser.DocumentContext):
        pass

    # Exit a parse tree produced by MarkdownParser#document.
    def exitDocument(self, ctx:MarkdownParser.DocumentContext):
        pass


    # Enter a parse tree produced by MarkdownParser#block.
    def enterBlock(self, ctx:MarkdownParser.BlockContext):
        pass

    # Exit a parse tree produced by MarkdownParser#block.
    def exitBlock(self, ctx:MarkdownParser.BlockContext):
        pass


    # Enter a parse tree produced by MarkdownParser#heading1.
    def enterHeading1(self, ctx:MarkdownParser.Heading1Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading1.
    def exitHeading1(self, ctx:MarkdownParser.Heading1Context):
        pass


    # Enter a parse tree produced by MarkdownParser#heading2.
    def enterHeading2(self, ctx:MarkdownParser.Heading2Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading2.
    def exitHeading2(self, ctx:MarkdownParser.Heading2Context):
        pass


    # Enter a parse tree produced by MarkdownParser#heading3.
    def enterHeading3(self, ctx:MarkdownParser.Heading3Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading3.
    def exitHeading3(self, ctx:MarkdownParser.Heading3Context):
        pass


    # Enter a parse tree produced by MarkdownParser#heading4.
    def enterHeading4(self, ctx:MarkdownParser.Heading4Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading4.
    def exitHeading4(self, ctx:MarkdownParser.Heading4Context):
        pass


    # Enter a parse tree produced by MarkdownParser#heading5.
    def enterHeading5(self, ctx:MarkdownParser.Heading5Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading5.
    def exitHeading5(self, ctx:MarkdownParser.Heading5Context):
        pass


    # Enter a parse tree produced by MarkdownParser#heading6.
    def enterHeading6(self, ctx:MarkdownParser.Heading6Context):
        pass

    # Exit a parse tree produced by MarkdownParser#heading6.
    def exitHeading6(self, ctx:MarkdownParser.Heading6Context):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineElement.
    def enterInlineElement(self, ctx:MarkdownParser.InlineElementContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineElement.
    def exitInlineElement(self, ctx:MarkdownParser.InlineElementContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineElementNoItalic.
    def enterInlineElementNoItalic(self, ctx:MarkdownParser.InlineElementNoItalicContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineElementNoItalic.
    def exitInlineElementNoItalic(self, ctx:MarkdownParser.InlineElementNoItalicContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineElementNoBold.
    def enterInlineElementNoBold(self, ctx:MarkdownParser.InlineElementNoBoldContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineElementNoBold.
    def exitInlineElementNoBold(self, ctx:MarkdownParser.InlineElementNoBoldContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineElementNoStrikethrough.
    def enterInlineElementNoStrikethrough(self, ctx:MarkdownParser.InlineElementNoStrikethroughContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineElementNoStrikethrough.
    def exitInlineElementNoStrikethrough(self, ctx:MarkdownParser.InlineElementNoStrikethroughContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineElementNoLink.
    def enterInlineElementNoLink(self, ctx:MarkdownParser.InlineElementNoLinkContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineElementNoLink.
    def exitInlineElementNoLink(self, ctx:MarkdownParser.InlineElementNoLinkContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineListElement.
    def enterInlineListElement(self, ctx:MarkdownParser.InlineListElementContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineListElement.
    def exitInlineListElement(self, ctx:MarkdownParser.InlineListElementContext):
        pass


    # Enter a parse tree produced by MarkdownParser#boldText.
    def enterBoldText(self, ctx:MarkdownParser.BoldTextContext):
        pass

    # Exit a parse tree produced by MarkdownParser#boldText.
    def exitBoldText(self, ctx:MarkdownParser.BoldTextContext):
        pass


    # Enter a parse tree produced by MarkdownParser#italicText.
    def enterItalicText(self, ctx:MarkdownParser.ItalicTextContext):
        pass

    # Exit a parse tree produced by MarkdownParser#italicText.
    def exitItalicText(self, ctx:MarkdownParser.ItalicTextContext):
        pass


    # Enter a parse tree produced by MarkdownParser#strikethroughText.
    def enterStrikethroughText(self, ctx:MarkdownParser.StrikethroughTextContext):
        pass

    # Exit a parse tree produced by MarkdownParser#strikethroughText.
    def exitStrikethroughText(self, ctx:MarkdownParser.StrikethroughTextContext):
        pass


    # Enter a parse tree produced by MarkdownParser#link.
    def enterLink(self, ctx:MarkdownParser.LinkContext):
        pass

    # Exit a parse tree produced by MarkdownParser#link.
    def exitLink(self, ctx:MarkdownParser.LinkContext):
        pass


    # Enter a parse tree produced by MarkdownParser#linkText.
    def enterLinkText(self, ctx:MarkdownParser.LinkTextContext):
        pass

    # Exit a parse tree produced by MarkdownParser#linkText.
    def exitLinkText(self, ctx:MarkdownParser.LinkTextContext):
        pass


    # Enter a parse tree produced by MarkdownParser#image.
    def enterImage(self, ctx:MarkdownParser.ImageContext):
        pass

    # Exit a parse tree produced by MarkdownParser#image.
    def exitImage(self, ctx:MarkdownParser.ImageContext):
        pass


    # Enter a parse tree produced by MarkdownParser#codeSpan.
    def enterCodeSpan(self, ctx:MarkdownParser.CodeSpanContext):
        pass

    # Exit a parse tree produced by MarkdownParser#codeSpan.
    def exitCodeSpan(self, ctx:MarkdownParser.CodeSpanContext):
        pass


    # Enter a parse tree produced by MarkdownParser#paragraph.
    def enterParagraph(self, ctx:MarkdownParser.ParagraphContext):
        pass

    # Exit a parse tree produced by MarkdownParser#paragraph.
    def exitParagraph(self, ctx:MarkdownParser.ParagraphContext):
        pass


    # Enter a parse tree produced by MarkdownParser#inlineContentLine.
    def enterInlineContentLine(self, ctx:MarkdownParser.InlineContentLineContext):
        pass

    # Exit a parse tree produced by MarkdownParser#inlineContentLine.
    def exitInlineContentLine(self, ctx:MarkdownParser.InlineContentLineContext):
        pass


    # Enter a parse tree produced by MarkdownParser#codeBlock.
    def enterCodeBlock(self, ctx:MarkdownParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by MarkdownParser#codeBlock.
    def exitCodeBlock(self, ctx:MarkdownParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by MarkdownParser#latexBlock.
    def enterLatexBlock(self, ctx:MarkdownParser.LatexBlockContext):
        pass

    # Exit a parse tree produced by MarkdownParser#latexBlock.
    def exitLatexBlock(self, ctx:MarkdownParser.LatexBlockContext):
        pass


    # Enter a parse tree produced by MarkdownParser#unorderedList.
    def enterUnorderedList(self, ctx:MarkdownParser.UnorderedListContext):
        pass

    # Exit a parse tree produced by MarkdownParser#unorderedList.
    def exitUnorderedList(self, ctx:MarkdownParser.UnorderedListContext):
        pass


    # Enter a parse tree produced by MarkdownParser#orderedList.
    def enterOrderedList(self, ctx:MarkdownParser.OrderedListContext):
        pass

    # Exit a parse tree produced by MarkdownParser#orderedList.
    def exitOrderedList(self, ctx:MarkdownParser.OrderedListContext):
        pass


    # Enter a parse tree produced by MarkdownParser#unorderedListItem.
    def enterUnorderedListItem(self, ctx:MarkdownParser.UnorderedListItemContext):
        pass

    # Exit a parse tree produced by MarkdownParser#unorderedListItem.
    def exitUnorderedListItem(self, ctx:MarkdownParser.UnorderedListItemContext):
        pass


    # Enter a parse tree produced by MarkdownParser#orderedListItem.
    def enterOrderedListItem(self, ctx:MarkdownParser.OrderedListItemContext):
        pass

    # Exit a parse tree produced by MarkdownParser#orderedListItem.
    def exitOrderedListItem(self, ctx:MarkdownParser.OrderedListItemContext):
        pass


    # Enter a parse tree produced by MarkdownParser#blockquote.
    def enterBlockquote(self, ctx:MarkdownParser.BlockquoteContext):
        pass

    # Exit a parse tree produced by MarkdownParser#blockquote.
    def exitBlockquote(self, ctx:MarkdownParser.BlockquoteContext):
        pass


    # Enter a parse tree produced by MarkdownParser#text.
    def enterText(self, ctx:MarkdownParser.TextContext):
        pass

    # Exit a parse tree produced by MarkdownParser#text.
    def exitText(self, ctx:MarkdownParser.TextContext):
        pass



del MarkdownParser