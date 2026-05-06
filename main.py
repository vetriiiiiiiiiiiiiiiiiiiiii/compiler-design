#!/usr/bin/env python3

import argparse
import sys
import os
from lexer.lexer import lexer
from parser.parser import parser
from semantic.semantic_checker import SemanticChecker
from codegen.llvm_ir_generator import LLVMIRGenerator
import subprocess

def main():
    argparser = argparse.ArgumentParser(description='RoboScript Compiler')
    argparser.add_argument('input_file', help='Input .robo file')
    args = argparser.parse_args()

    if not args.input_file.endswith('.robo'):
        print("Error: Input file must have .robo extension")
        sys.exit(1)

    # Read input
    try:
        with open(args.input_file, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File {args.input_file} not found")
        sys.exit(1)

    print("Compiling RoboScript...")

    # Lexer
    print("Running lexer...")
    lexer.input(source)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    print(f"Tokens: {[str(t) for t in tokens]}")

    # Parser
    print("Running parser...")
    try:
        ast = parser.parse(source)
        print("AST built successfully")
    except Exception as e:
        print(f"Parse error: {e}")
        sys.exit(1)

    # Semantic analysis
    print("Running semantic analysis...")
    checker = SemanticChecker()
    errors = checker.check(ast)
    if errors:
        for error in errors:
            print(f"Semantic error: {error}")
        sys.exit(1)
    print("Semantic analysis passed")

    # Code generation
    print("Generating LLVM IR...")
    generator = LLVMIRGenerator()
    ir_code = generator.generate(ast)
    print("LLVM IR generated")

    # Save IR
    os.makedirs('output', exist_ok=True)
    with open('output/output.ll', 'w') as f:
        f.write(ir_code)
    print("Saved output/output.ll")

    # Run llc
    print("Running llc...")
    try:
        subprocess.run(['llc', 'output/output.ll', '-o', 'output/output.s'], check=True)
        print("Assembly generated: output/output.s")
    except subprocess.CalledProcessError as e:
        print(f"llc failed: {e}")
        sys.exit(1)

    # Run clang
    print("Running clang...")
    try:
        subprocess.run(['clang', 'output/output.s', 'runtime/runtime.c', '-o', 'output/executable'], check=True)
        print("Executable generated: output/executable")
    except subprocess.CalledProcessError as e:
        print(f"clang failed: {e}")
        sys.exit(1)

    print("Compilation successful!")

if __name__ == '__main__':
    main()