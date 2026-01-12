lexer grammar MarkdownLexer;

// Default Mode Rules

HEADING6 : '######' SPACESKIP ;
HEADING5 : '#####' SPACESKIP ;
HEADING4 : '####' SPACESKIP ;
HEADING3 : '###' SPACESKIP ;
HEADING2 : '##' SPACESKIP ;
HEADING1 : '#' SPACESKIP ;

BOLD          : '**' ;
UNORDERED_LIST_MARKER   : '*' ' ' ;
ORDERED_LIST_MARKER     : '1.' ' ' ;
ITALIC        : '*' ;
BACKTICK      : '`' ;
BLOCKQUOTE    : '>' ; 
STRIKETHROUGH : '~~' ;
NEWLINE       : '\r'? '\n' ;
SPACE         : [ \t]+ ;
SPACESKIP     : [ \t]+ -> skip ;
LINK_OPEN       : '[' ;
LINK_CLOSE      : ']' ;
LINK_HREF_OPEN  : '(' ;
LINK_HREF_CLOSE : ')' ;
IMAGE           : '!' ;

TEXT    : ~[#\r\n`*1>~[\]()!]+ ;


// The token that starts the new mode (must be last among tokens starting with the same characters)
TRIPLE_BACKTICK : '```' NEWLINE -> pushMode(CodeBlockMode) ;

// New Lexer Mode for Fenced Code Block Content
mode CodeBlockMode;

// Only tokenized when in CodeBlockMode
CODE_BLOCK_CONTENT : ~[`]+  ; 

// This token switches the lexer back to the default mode
CODE_BLOCK_END : '```' -> popMode ;
