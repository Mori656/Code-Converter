from antlr4 import *
from MarkdownParserVisitor import MarkdownParserVisitor
from MarkdownParser import MarkdownParser

class ListItem:
    def __init__(self, text, indent):
        self.text = text
        self.children = []
        self.indent = indent

def nest_items(items):
    stack = []
    root = []

    for item in items:
        while stack and stack[-1].indent >= item.indent:
            stack.pop()

        if stack:
            stack[-1].children.append(item)
        else:
            root.append(item)

        stack.append(item)

    return root


def render_list(items):
    html = "<ul>\n"
    for item in items:
        if item.children:
            html += render_list(item.children)
        else:
            html += f"<li>{item.text}</li>\n"
    html += "</ul>\n"
    return html



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

    def visitCodeSpan(self, ctx: MarkdownParser.CodeSpanContext):
        return f"<code>{ctx.getText().strip('`')}</code>"

    def visitInlineElement(self, ctx: MarkdownParser.InlineElementContext):
        return self.visitChildrenAsText(ctx)

    def visitInlineElementNoItalic(self, ctx: MarkdownParser.InlineElementNoItalicContext):
        return self.visitChildrenAsText(ctx)
    
    def visitInlineElementNoBold(self, ctx: MarkdownParser.InlineElementNoBoldContext):
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

    # def visitUnorderedList(self, ctx: MarkdownParser.UnorderedListContext):
    #     return f"<ul>\n{self.visitInlineListElement(ctx)}</ul>\n"
    def visitUnorderedList(self, ctx: MarkdownParser.UnorderedListContext):
        items = []

        for child in ctx.unorderedListItem():
            item = child.accept(self)
            items.append(item)

        nested = nest_items(items)
        return render_list(nested)

    def visitOrderedList(self, ctx: MarkdownParser.OrderedListContext):
        return f"<ol>\n{self.visitInlineListElement(ctx)}</ol>\n"

    # def visitUnorderedListItem(self, ctx: MarkdownParser.UnorderedListItemContext):
        # return f"<li>{self.visitInlineListElement(ctx)}</li>\n"
    def visitUnorderedListItem(self, ctx: MarkdownParser.UnorderedListItemContext):
        indent = ( len(ctx.SPACE().getText()) if ctx.SPACE() else 0 )
        text = self.visitInlineListElement(ctx)
        return  (text, indent)

    def visitOrderedListItem(self, ctx: MarkdownParser.OrderedListItemContext):
        return f"<li>{self.visitInlineListElement(ctx)}</li>\n"

    def visitInlineListElement(self, ctx: MarkdownParser.InlineListElementContext):
        return self.visitChildrenAsText(ctx)

    # ======================
    # Tekst
    # ======================

    def visitText(self, ctx: MarkdownParser.TextContext):
        return ctx.getText()
