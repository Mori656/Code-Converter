parser grammar LatexParser;

options { tokenVocab=LatexLexer; }

// Entry point
expr : relationExpr ;

// Level 5: relation / comparisons
relationExpr
    : additiveExpr (relationOp additiveExpr)*
    ;

relationOp
    : EQUALS
    | LT
    | GT
    | COMMAND        // constants used as infix operators, e.g. \approx, \leq
    ;

// Level 4: addition/subtraction
additiveExpr
    : multiplicativeExpr (addOp multiplicativeExpr)*
    ;

addOp : PLUS | MINUS ;

// Level 3: multiplication
multiplicativeExpr
    : postfixExpr (multOp postfixExpr)*
    ;

multOp : STAR | SLASH ;

// Level 2: postfix (sup/sub)
postfixExpr
    : primaryExpr (postfixOp primaryExpr)*
    ;

postfixOp : CARET | UNDERSCORE ;

// Level 1: primaries
primaryExpr
    : fracExpr
    | functionExpr
    | numberAtom
    | identAtom
    | commandAtom
    | group
    ;

fracExpr
    : COMMAND LBRACE expr RBRACE LBRACE expr RBRACE
    ;

functionExpr
    : FUNCTIONCMD primaryExpr+
    ;

group
    : LBRACE expr RBRACE
    | LPAREN expr RPAREN
    ;


//atom
//    : NUMBER
//    | IDENT
//    | COMMAND   // constants like \pi
//    ;

numberAtom  : NUMBER  ;
identAtom  :  IDENT   ;
commandAtom : COMMAND ;
