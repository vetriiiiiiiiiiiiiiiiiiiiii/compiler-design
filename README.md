# RoboScript Compiler

A complete end-to-end compiler for the RoboScript domain-specific language (DSL), built from scratch using Python, PLY, and LLVM.

## Overview

RoboScript is a DSL designed for controlling robots and automation systems. This compiler translates RoboScript source code into native executables through a multi-stage pipeline: lexical analysis, parsing, AST construction, semantic analysis, LLVM IR generation, and backend compilation.

## Features

- **Full Compiler Pipeline**: Lexer → Parser → AST → Semantic Analysis → LLVM IR → Assembly → Executable
- **Modular Architecture**: Clean separation of concerns with dedicated modules for each compilation stage
- **Error Handling**: Comprehensive error reporting with line numbers and colored output
- **Optimization**: Constant folding and basic optimizations
- **Extensible**: Easy to add new language features
- **Production-Ready**: Well-documented, tested, and suitable for academic and professional use

## RoboScript Language Syntax

### Variables and Arithmetic
```
LET variable = expression
```

### Movement Commands
```
MOVE FORWARD expression
MOVE BACKWARD expression
TURN LEFT expression
TURN RIGHT expression
```

### Control Flow
```
IF condition
    statements
END
```

### Output
```
PRINT expression
```

### Expressions
- Arithmetic: `+`, `-`, `*`, `/`
- Comparisons: `>`, `<`
- Variables and numbers

### Example Program
```
LET speed = 10
MOVE FORWARD speed
TURN LEFT 90
IF speed > 5
    PRINT speed
END
```

## Compiler Architecture

```
RoboScript Source
       ↓
     Lexer
       ↓
     Parser
       ↓
       AST
       ↓
Semantic Analysis
       ↓
    LLVM IR
       ↓
   llc Backend
       ↓
    Assembly
       ↓
     clang
       ↓
 Native Executable
```

## Installation

### Prerequisites
- Python 3.11+
- LLVM toolchain (llc, clang)
- Git

### Setup
```bash
git clone https://github.com/vetriiiiiiiiiiiiiiiiiiiiii/compiler-design.git
cd compiler-design
pip install -r requirements.txt
```

## Usage

### Compiling a RoboScript Program
```bash
python main.py examples/example1.robo
```

This will:
1. Compile the RoboScript source
2. Generate LLVM IR (`output/output.ll`)
3. Generate assembly (`output/output.s`)
4. Create native executable (`output/executable`)

### Running the Executable
```bash
./output/executable
```

## Project Structure

```
compiler-design/
├── lexer/                 # Lexical analysis
│   ├── __init__.py
│   └── lexer.py
├── parser/                # Syntax analysis and AST construction
│   ├── __init__.py
│   └── parser.py
├── ast_nodes/             # Abstract Syntax Tree node definitions
│   ├── __init__.py
│   └── nodes.py
├── semantic/              # Semantic analysis and type checking
│   ├── __init__.py
│   └── semantic_checker.py
├── codegen/               # LLVM IR code generation
│   ├── __init__.py
│   └── llvm_ir_generator.py
├── runtime/               # Runtime support (C code)
│   └── runtime.c
├── examples/              # Sample RoboScript programs
│   ├── example1.robo
│   ├── example2.robo
│   └── example3.robo
├── output/                # Generated files (IR, assembly, executable)
├── docs/                  # Documentation
│   ├── architecture.md
│   ├── grammar.md
│   ├── llvm_pipeline.md
│   └── screenshots/
├── tests/                 # Unit tests
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_codegen.py
├── .github/workflows/     # CI/CD pipeline
│   └── ci.yml
├── requirements.txt       # Python dependencies
├── main.py                # Compiler driver
├── README.md
├── LICENSE
└── .gitignore
```

## LLVM Pipeline Explanation

1. **Source Code**: RoboScript programs are written in a simple, robot-control focused syntax
2. **Lexer**: Breaks source into tokens using PLY (Python Lex-Yacc)
3. **Parser**: Builds Abstract Syntax Tree using PLY yacc
4. **Semantic Analysis**: Checks for undefined variables, type consistency
5. **LLVM IR Generation**: Translates AST to LLVM Intermediate Representation using llvmlite
6. **Backend Compilation**: 
   - `llc` converts LLVM IR to target-specific assembly
   - `clang` links assembly with runtime and produces executable

## Example Programs

### Example 1: Basic Movement and Conditional
```
LET speed = 10
MOVE FORWARD speed
TURN LEFT 90
IF speed > 5
    PRINT speed
END
```

### Example 2: Arithmetic Operations
```
LET a = 5
LET b = a + 3
PRINT b
MOVE BACKWARD 2
```

### Example 3: Comparison and Control Flow
```
LET x = 10
LET y = 20
IF x < y
    PRINT x
    TURN RIGHT 45
END
PRINT y
```

## Build Instructions

### Manual Build
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Build example
python main.py examples/example1.robo

# Run executable
./output/executable
```

### CI/CD
The project includes GitHub Actions for automated testing and building.

## Running Instructions

1. Write your RoboScript program in a `.robo` file
2. Run: `python main.py your_program.robo`
3. Execute: `./output/executable`

## Screenshots

*Compiler output showing successful compilation*

*Generated LLVM IR for example program*

*Execution output of compiled program*

## Future Improvements

- [ ] Add more data types (floats, strings)
- [ ] Implement loops (WHILE, FOR)
- [ ] Add functions and procedures
- [ ] Enhance error messages with suggestions
- [ ] Add debugging support
- [ ] Optimize generated code
- [ ] Support for robot hardware integration

## Contribution Guide

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Academic/Portfolio Notes

This compiler demonstrates:
- Compiler construction principles
- Language design
- LLVM toolchain usage
- Python software engineering
- Test-driven development
- Documentation best practices

Suitable for computer science courses, compiler design projects, and software engineering portfolios.