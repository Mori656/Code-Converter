lexer grammar LatexLexer;

BACKSLASH   : '\\' ;

LBRACE      : '{' ;
RBRACE      : '}' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACK      : '[' ;
RBRACK      : ']' ;

CARET       : '^' ;
UNDERSCORE  : '_' ;

EXCLAMATION : '!' ;
ASTERISK    : '*' ;
SLASH       : '/' ;
PLUS        : '+' ;
MINUS       : '-' ;
LT          : '<' ;
GT          : '>' ;
EQUALS      : '=' ;
DOT         : '.' ;

TILDE       : '~' ;

// Fraction commands
FRAC        : BACKSLASH 'frac' ;

// Function commands
//FUNCTION    : BACKSLASH ( 'sin' | 'cos' | 'tan' | 'log' | 'ln' | 'exp' ) ;

// Generic commands (constants, Greek letters, operators, etc.)
COMMAND     : BACKSLASH [a-zA-Z]+ ;

NUMBER      : [0-9]+ ;
IDENT       : [a-zA-Z] ;

WHITESPACE  : [ \t\r\n]+ -> skip ;
