lexer grammar LatexLexer;

BACKSLASH   : '\\' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
CARET       : '^' ;
UNDERSCORE  : '_' ;

PLUS        : '+' ;
MINUS       : '-' ;
STAR        : '*' ;
SLASH       : '/' ;
EQUALS      : '=' ;
LT          : '<' ;
GT          : '>' ;

FUNCTIONCMD : BACKSLASH ( 'sin' | 'cos' | 'tan' | 'log' | 'ln' | 'exp' );
COMMAND     : BACKSLASH [a-zA-Z]+ ;

NUMBER      : [0-9]+ ;
IDENT       : [a-zA-Z] ;

WS          : [ \t\r\n]+ -> skip ;
OTHER       : . ;
