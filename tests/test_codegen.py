import unittest
from parser.parser import parser
from codegen.llvm_ir_generator import LLVMIRGenerator

class TestCodegen(unittest.TestCase):
    def test_simple_program(self):
        ast = parser.parse("LET x = 5 PRINT x")
        generator = LLVMIRGenerator()
        ir = generator.generate(ast)
        self.assertIn("main", ir)
        self.assertIn("printf", ir)
        self.assertIn("%d", ir)

    def test_arithmetic(self):
        ast = parser.parse("LET a = 2 LET b = a + 3 PRINT b")
        generator = LLVMIRGenerator()
        ir = generator.generate(ast)
        self.assertIn("add", ir)

    def test_conditional(self):
        ast = parser.parse("IF 1 > 0 PRINT 1 END")
        generator = LLVMIRGenerator()
        ir = generator.generate(ast)
        self.assertIn("br", ir)  # branch instruction

if __name__ == '__main__':
    unittest.main()