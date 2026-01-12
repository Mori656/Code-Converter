from antlr4 import *
from MarkdownLexer import MarkdownLexer
from MarkdownParser import MarkdownParser
from HtmlVisitor import MarkdownToHtmlVisitor as HtmlVisitor

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

print("\nGenerated HTML:\n")
print(html)
