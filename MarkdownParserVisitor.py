# Generated from MarkdownParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkdownParser import MarkdownParser
else:
    from MarkdownParser import MarkdownParser

# This class defines a complete generic visitor for a parse tree produced by MarkdownParser.

class MarkdownParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MarkdownParser#document.
    def visitDocument(self, ctx:MarkdownParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#block.
    def visitBlock(self, ctx:MarkdownParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading1.
    def visitHeading1(self, ctx:MarkdownParser.Heading1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading2.
    def visitHeading2(self, ctx:MarkdownParser.Heading2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading3.
    def visitHeading3(self, ctx:MarkdownParser.Heading3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading4.
    def visitHeading4(self, ctx:MarkdownParser.Heading4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading5.
    def visitHeading5(self, ctx:MarkdownParser.Heading5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading6.
    def visitHeading6(self, ctx:MarkdownParser.Heading6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineElement.
    def visitInlineElement(self, ctx:MarkdownParser.InlineElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineElementNoItalic.
    def visitInlineElementNoItalic(self, ctx:MarkdownParser.InlineElementNoItalicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineElementNoBold.
    def visitInlineElementNoBold(self, ctx:MarkdownParser.InlineElementNoBoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineElementNoStrikethrough.
    def visitInlineElementNoStrikethrough(self, ctx:MarkdownParser.InlineElementNoStrikethroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineElementNoLink.
    def visitInlineElementNoLink(self, ctx:MarkdownParser.InlineElementNoLinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineListElement.
    def visitInlineListElement(self, ctx:MarkdownParser.InlineListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#boldText.
    def visitBoldText(self, ctx:MarkdownParser.BoldTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#italicText.
    def visitItalicText(self, ctx:MarkdownParser.ItalicTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#strikethroughText.
    def visitStrikethroughText(self, ctx:MarkdownParser.StrikethroughTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#link.
    def visitLink(self, ctx:MarkdownParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#linkText.
    def visitLinkText(self, ctx:MarkdownParser.LinkTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#image.
    def visitImage(self, ctx:MarkdownParser.ImageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#codeSpan.
    def visitCodeSpan(self, ctx:MarkdownParser.CodeSpanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#paragraph.
    def visitParagraph(self, ctx:MarkdownParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#inlineContentLine.
    def visitInlineContentLine(self, ctx:MarkdownParser.InlineContentLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#codeBlock.
    def visitCodeBlock(self, ctx:MarkdownParser.CodeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#unorderedList.
    def visitUnorderedList(self, ctx:MarkdownParser.UnorderedListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#orderedList.
    def visitOrderedList(self, ctx:MarkdownParser.OrderedListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#unorderedListItem.
    def visitUnorderedListItem(self, ctx:MarkdownParser.UnorderedListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#orderedListItem.
    def visitOrderedListItem(self, ctx:MarkdownParser.OrderedListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#blockquote.
    def visitBlockquote(self, ctx:MarkdownParser.BlockquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#breakline.
    def visitBreakline(self, ctx:MarkdownParser.BreaklineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#text.
    def visitText(self, ctx:MarkdownParser.TextContext):
        return self.visitChildren(ctx)



del MarkdownParser