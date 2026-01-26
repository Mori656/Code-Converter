from antlr4 import *
from antlr.MarkdownLexer import MarkdownLexer
from antlr.MarkdownParser import MarkdownParser
from antlr.HtmlVisitor import MarkdownToHtmlVisitor as HtmlVisitorMarkdown
from antlrLatex.LatexLexer import LatexLexer
from antlrLatex.LatexParser import LatexParser
from antlrLatex.HtmlVisitorLatex import LatexToHtmlVisitor as HtmlVisitorLatex

def test_markdown_parsing():
    input_stream = FileStream("testlatex.md", encoding="utf-8")
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

    visitor = HtmlVisitorMarkdown()
    print(tree.toStringTree(recog=parser))
    html = visitor.visit(tree)
    print(html)

def markdown_to_html(markdown: str) -> str:
    input_stream = InputStream(markdown)

    lexer = MarkdownLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = MarkdownParser(tokens)
    tree = parser.document()

    visitor = HtmlVisitorMarkdown()
    html = visitor.visit(tree)

    return html

def latex_to_html(latex: str) -> str:
    # input_stream = InputStream(latex)

    input_stream = FileStream("./antlr/test.md", encoding="utf-8")
    lexer = LatexLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    tokens.fill()

    for token in tokens.tokens:
        print(
            lexer.symbolicNames[token.type],
            repr(token.text)
        )

    parser = LatexParser(tokens)
    tree = parser.expr()

    visitor = HtmlVisitorLatex()
    print(tree.toStringTree(recog=parser))
    html = visitor.visit(tree)
    print(html)
    return html

if __name__ == "__main__":
    print("Running markdown parser ...")
    test_markdown_parsing()
    # print("Running LaTeX parser ...")
    # html = latex_to_html(r"\pi \approx \frac{22}{7}")
    # print(html)
