parser grammar LatexParser;

options { tokenVocab=LatexLexer; }

// entry point
expr : term+ ;

term
    : fraction
    | scriptable
    ;

fraction
    : FRAC LBRACE expr RBRACE LBRACE expr RBRACE
    ;

scriptable
    : atom (scriptOp atom)? (scriptOp atom)? ;

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
