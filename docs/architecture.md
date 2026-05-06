# Compiler Architecture

## Overview

The RoboScript compiler follows a traditional multi-pass compiler architecture with clear separation of concerns.

## Components

### Lexer (`lexer/lexer.py`)
- Uses PLY lex for tokenization
- Recognizes keywords, identifiers, numbers, operators
- Handles comments and whitespace
- Provides error reporting for invalid characters

### Parser (`parser/parser.py`)
- Uses PLY yacc for syntax analysis
- Builds Abstract Syntax Tree (AST)
- Implements recursive descent parsing
- Reports syntax errors with line numbers

### AST (`ast_nodes/nodes.py`)
- Defines node classes for all language constructs
- Provides visitor pattern support
- Enables tree traversals for analysis and code generation

### Semantic Analyzer (`semantic/semantic_checker.py`)
- Implements symbol table for variable tracking
- Performs type checking (integers only)
- Detects undefined variables
- Validates semantic correctness

### Code Generator (`codegen/llvm_ir_generator.py`)
- Uses llvmlite for LLVM IR generation
- Translates AST to LLVM intermediate representation
- Handles control flow, arithmetic, and I/O operations
- Generates efficient, optimizable code

### Runtime (`runtime/runtime.c`)
- Provides C runtime support
- Links with generated assembly
- Includes necessary headers (stdio.h for printf)

## Pipeline Flow

1. Source code → Tokens
2. Tokens → AST
3. AST → Semantic validation
4. AST → LLVM IR
5. LLVM IR → Assembly (llc)
6. Assembly + Runtime → Executable (clang)