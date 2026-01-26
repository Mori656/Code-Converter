parser grammar LatexParser;

options { tokenVocab=LatexLexer; }

// entry point
expr : term+ ;

term
    : fraction
    | root
    | scriptable
    ;

fraction : FRAC LBRACE expr RBRACE LBRACE expr RBRACE ;

root : SQRT ( LBRACK expr RBRACK )? LBRACE expr RBRACE ;

scriptable : atom
           | atom superscript (subscript)?
           | atom subscript (superscript)?
           ;

subscript : UNDERSCORE atom ;
superscript : CARET atom ;

scriptOp
    : CARET
    | UNDERSCORE
    ;

atom
    : NUMBER
    | IDENT
    | COMMAND
    | LPAREN expr RPAREN
    | LBRACE expr RBRACE
    | operator
    | nbsp
    ;

nbsp : TILDE ;

operator
    : EXCLAMATION
    | ASTERISK
    | SLASH
    | PLUS
    | MINUS
    | LT
    | GT
    | EQUALS
    | DOT
    ;
