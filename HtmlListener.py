from MarkdownParserListener import MarkdownParserListener

class HtmlListener(MarkdownParserListener):
    def __init__(self):
        self.html = []
        self.inline_buffer = []

    # ========== HEADINGS ==========
    def exitHeading1(self, ctx):
        text = ctx.getText().replace("#", "").strip()
        self.html.append(f"<h1>{text}</h1>")

    def exitHeading2(self, ctx):
        text = ctx.getText().replace("##", "").strip()
        self.html.append(f"<h2>{text}</h2>")

    def exitHeading3(self, ctx):
        text = ctx.getText().replace("###", "").strip()
        self.html.append(f"<h3>{text}</h3>")

    # ========== PARAGRAPH ==========
    def exitParagraph(self, ctx):
        text = "".join(self.inline_buffer)
        self.html.append(f"<p>{text}</p>")

    # ========== INLINE ==========
    def exitText(self, ctx):
        self.inline_buffer.append(ctx.getText())

    def exitBoldText(self, ctx):
        text = ctx.getText().strip("**")
        self.inline_buffer.append(f"<strong>{text}</strong>")

    def exitItalicText(self, ctx):
        print(self.inline_buffer)
        text = ctx.getText()
        print (text)
        text = ctx.getText().strip("*")
        print (text)
        self.inline_buffer.clear()
        self.inline_buffer.append(f"<em>{text}</em>")

    def exitCodeSpan(self, ctx):
        text = ctx.getText().strip("`")
        self.inline_buffer.append(f"<code>{text}</code>")
