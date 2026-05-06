# RoboScript Grammar

## EBNF Grammar

```
program ::= statements

statements ::= statement statements | statement

statement ::= let_stmt | print_stmt | move_stmt | turn_stmt | if_stmt

let_stmt ::= "LET" ID "=" expr

print_stmt ::= "PRINT" expr

move_stmt ::= "MOVE" direction expr

turn_stmt ::= "TURN" direction expr

direction ::= "FORWARD" | "BACKWARD" | "LEFT" | "RIGHT"

if_stmt ::= "IF" condition statements "END"

condition ::= expr relop expr

relop ::= ">" | "<"

expr ::= expr "+" term | expr "-" term | term

term ::= term "*" factor | term "/" factor | factor

factor ::= NUMBER | ID | "(" expr ")"

ID ::= [a-zA-Z_][a-zA-Z0-9_]*

NUMBER ::= [0-9]+
```

## Operator Precedence

1. `*`, `/` (highest)
2. `+`, `-`
3. `>`, `<` (lowest)

## Notes

- All statements end implicitly
- Blocks are delimited by IF ... END
- Expressions are right-associative for arithmetic
- No function calls or complex expressions