import unittest
from parser.parser import parser
from ast_nodes.nodes import *

class TestParser(unittest.TestCase):
    def test_let_statement(self):
        result = parser.parse("LET x = 5")
        expected = ProgramNode([LetNode('x', NumberNode(5))])
        self.assertEqual(str(result), str(expected))  # Simple string comparison

    def test_print_statement(self):
        result = parser.parse("PRINT 10")
        expected = ProgramNode([PrintNode(NumberNode(10))])
        self.assertEqual(str(result), str(expected))

    def test_move_statement(self):
        result = parser.parse("MOVE FORWARD 5")
        expected = ProgramNode([MoveNode('FORWARD', NumberNode(5))])
        self.assertEqual(str(result), str(expected))

    def test_if_statement(self):
        result = parser.parse("IF 1 > 0 PRINT 1 END")
        expected = ProgramNode([IfNode(BinaryOpNode(NumberNode(1), '>', NumberNode(0)), [PrintNode(NumberNode(1))])])
        self.assertEqual(str(result), str(expected))

if __name__ == '__main__':
    unittest.main()