from antlr4 import *
from MarkdownLexer import MarkdownLexer
from MarkdownParser import MarkdownParser
from HtmlVisitor import MarkdownToHtmlVisitor as HtmlVisitor

def test_markdown_parsing():
    input_stream = FileStream("test.md", encoding="utf-8")
    lexer = MarkdownLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = MarkdownParser(tokens)
    tree = parser.document()

    tokens.fill()

    for token in tokens.tokens:
        print(
            lexer.symbolicNames[token.type],
            repr(token.text)
        )

    visitor = HtmlVisitor()
    print(tree.toStringTree(recog=parser))
    html = visitor.visit(tree)
    print(html)

def markdown_to_html(markdown: str) -> str:
    input_stream = InputStream(markdown)

    lexer = MarkdownLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = MarkdownParser(tokens)
    tree = parser.document()

    visitor = MarkdownToHtmlVisitor()
    html = visitor.visit(tree)

    return html

if __name__ == "__main__":
    print("Running markdown parser ...")
    test_markdown_parsing()