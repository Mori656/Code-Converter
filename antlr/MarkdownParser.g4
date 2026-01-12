parser grammar MarkdownParser;

// Import tokens from the lexer grammar
options { tokenVocab=MarkdownLexer; }

// The main entry point for the parser: a Markdown document is a sequence of blocks.
document : block* EOF ;

// A block is an element that usually occupies its own line(s), like a heading or paragraph.
block : heading1
      | heading2
      | heading3
      | heading4
      | heading5
      | heading6
      | codeBlock
      | latexBlock
      | unorderedList
      | orderedList
      | blockquote
      | paragraph
      | NEWLINE ;

// Rules for ATX Headings (e.g., # Heading)
heading1 : SPACE* HEADING1 inlineElement* NEWLINE ;
heading2 : SPACE* HEADING2 inlineElement* NEWLINE ;
heading3 : SPACE* HEADING3 inlineElement* NEWLINE ;
heading4 : SPACE* HEADING4 inlineElement* NEWLINE ;
heading5 : SPACE* HEADING5 inlineElement* NEWLINE ;
heading6 : SPACE* HEADING6 inlineElement* NEWLINE ;

// Rule for inline formatting elements
inlineElement : boldText
              | italicText
              | strikethroughText
              | link
              | image
              | codeSpan
              | text
              | SPACE ;

inlineElementNoItalic
    : boldText
    | strikethroughText
    | linkText
    | text
    ;

inlineElementNoBold
    : italicText
    | strikethroughText
    | linkText
    | text
    ;

inlineElementNoStrikethrough
    : boldText
    | italicText
    | linkText
    | text
    ;

inlineElementNoLink
    : boldText
    | italicText
    | strikethroughText
    | text
    ;

inlineListElement: boldText
              | italicText
              | strikethroughText
              | codeSpan
              | text
              | SPACE ;


// Rule for bold text (**text**)
boldText : BOLD inlineElementNoBold* BOLD ;

// Rule for italic text (*text*)
italicText : ITALIC inlineElementNoItalic* ITALIC ;

// Rule for strikethrough text (~~text~~)
strikethroughText: STRIKETHROUGH inlineElementNoStrikethrough* STRIKETHROUGH ;

// Rules for links
link     : linkText LINK_HREF_OPEN text LINK_HREF_CLOSE ;
linkText : LINK_OPEN inlineElementNoLink* LINK_CLOSE ;

image    : IMAGE link ;

// Rule for inline code (`code`)
codeSpan : BACKTICK text BACKTICK ;

// A paragraph is one or more lines of inline elements.
//paragraph : (inlineElement | NEWLINE)+ EOF_OR_BLANK_LINE ;
paragraph : ( inlineContentLine )+ ;

inlineContentLine : (inlineElement)+ NEWLINE ; // A line of text followed by a single NEWLINE

// Rule for a fenced code block
codeBlock : TRIPLE_BACKTICK CODE_BLOCK_CONTENT* CODE_BLOCK_END NEWLINE ;

// Rule for Latex mode
latexBlock : LATEX_START LATEX_CONTENT* LATEX_END NEWLINE ;

// Rule for lists
unorderedList
    : unorderedListItem+
    ;

orderedList
    : orderedListItem+
    ;

unorderedListItem
    : SPACE? UNORDERED_LIST_MARKER inlineListElement* NEWLINE
    ;

orderedListItem
    : SPACE? ORDERED_LIST_MARKER inlineListElement* NEWLINE
    ;

blockquote : BLOCKQUOTE (inlineElement)+ ;

// Text
text
    : TEXT
    ;
