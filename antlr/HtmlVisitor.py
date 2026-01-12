from antlr4 import *
from antlr.MarkdownParserVisitor import MarkdownParserVisitor
from antlr.MarkdownParser import MarkdownParser


class MarkdownToHtmlVisitor(MarkdownParserVisitor):

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
    # Dokument / bloki
    # ======================

    def visitDocument(self, ctx: MarkdownParser.DocumentContext):
        return self.visitChildrenAsText(ctx)

    def visitBlock(self, ctx: MarkdownParser.BlockContext):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Nagłówki
    # ======================

    def visitHeading1(self, ctx: MarkdownParser.Heading1Context):
        return f"<h1>{self.visitChildrenAsText(ctx)}</h1>\n"

    def visitHeading2(self, ctx: MarkdownParser.Heading2Context):
        return f"<h2>{self.visitChildrenAsText(ctx)}</h2>\n"

    def visitHeading3(self, ctx: MarkdownParser.Heading3Context):
        return f"<h3>{self.visitChildrenAsText(ctx)}</h3>\n"

    def visitHeading4(self, ctx: MarkdownParser.Heading4Context):
        return f"<h4>{self.visitChildrenAsText(ctx)}</h4>\n"

    def visitHeading5(self, ctx: MarkdownParser.Heading5Context):
        return f"<h5>{self.visitChildrenAsText(ctx)}</h5>\n"

    def visitHeading6(self, ctx: MarkdownParser.Heading6Context):
        return f"<h6>{self.visitChildrenAsText(ctx)}</h6>\n"

    # ======================
    # Inline
    # ======================

    def visitBoldText(self, ctx: MarkdownParser.BoldTextContext):
        return f"<strong>{self.visitChildrenAsText(ctx)}</strong>"

    def visitItalicText(self, ctx: MarkdownParser.ItalicTextContext):
        return f"<em>{self.visitChildrenAsText(ctx)}</em>"
    
    def visitStrikethroughText(self, ctx:MarkdownParser.StrikethroughTextContext):
        return f"<del>{self.visitChildrenAsText(ctx)}</del>"

    def visitCodeSpan(self, ctx: MarkdownParser.CodeSpanContext):
        return f"<code>{ctx.getText().strip('`')}</code>"

    def visitInlineElement(self, ctx: MarkdownParser.InlineElementContext):
        return self.visitChildrenAsText(ctx)

    def visitInlineElementNoItalic(self, ctx: MarkdownParser.InlineElementNoItalicContext):
        return self.visitChildrenAsText(ctx)
    
    def visitInlineElementNoBold(self, ctx: MarkdownParser.InlineElementNoBoldContext):
        return self.visitChildrenAsText(ctx)
    
    def visitInlineElementNoStrikethrough(self, ctx):
        return self.visitChildrenAsText(ctx)
    
    def visitInlineElementNoLink(self, ctx):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Paragrafy
    # ======================

    def visitParagraph(self, ctx: MarkdownParser.ParagraphContext):
        return f"<p>{self.visitChildrenAsText(ctx)}</p>\n"

    def visitInlineContentLine(self, ctx: MarkdownParser.InlineContentLineContext):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Code block
    # ======================

    def visitCodeBlock(self, ctx: MarkdownParser.CodeBlockContext):
        # ctx.getText() zwykle zawiera ```...```
        code = ctx.getText()
        code = code.replace("```", "").strip()
        return f"<pre><code>{code}</code></pre>\n"

    # ======================
    # Listy
    # ======================

    def visitUnorderedList(self, ctx: MarkdownParser.UnorderedListContext):
        return f"<ul>\n{self.visitInlineListElement(ctx)}</ul>\n"

    def visitOrderedList(self, ctx: MarkdownParser.OrderedListContext):
        return f"<ol>\n{self.visitInlineListElement(ctx)}</ol>\n"

    def visitUnorderedListItem(self, ctx: MarkdownParser.UnorderedListItemContext):
        return f"<li>{self.visitInlineListElement(ctx)}</li>\n"

    def visitOrderedListItem(self, ctx: MarkdownParser.OrderedListItemContext):
        return f"<li>{self.visitInlineListElement(ctx)}</li>\n"

    def visitInlineListElement(self, ctx: MarkdownParser.InlineListElementContext):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Cytat
    # ======================

    def visitBlockquote(self, ctx:MarkdownParser.BlockquoteContext):
        return f"<blockquote>{self.visitInlineElement(ctx)}</blockquote>\n"
    
    # ======================
    # Link
    # ======================

    def visitLink(self, ctx):
        href = self.visit(ctx.text())
        label = ''.join(self.visit(e) for e in ctx.linkText().inlineElementNoLink())
        return f'<a href="{href}">{label}</a>'

    def visitImage(self, ctx):
        link = ctx.link()
        src = self.visit(link.text())
        alt = ''.join(self.visit(e) for e in link.linkText().inlineElementNoLink())
        return f'<img src="{src}" alt="{alt}">'

    # ======================
    # Tekst
    # ======================

    def visitText(self, ctx: MarkdownParser.TextContext):
        return ctx.getText()
