import unittest
from lexer.lexer import lexer

class TestLexer(unittest.TestCase):
    def test_keywords(self):
        lexer.input("LET MOVE FORWARD PRINT IF END")
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
        expected = [
            ('LET', 'LET'),
            ('MOVE', 'MOVE'),
            ('FORWARD', 'FORWARD'),
            ('PRINT', 'PRINT'),
            ('IF', 'IF'),
            ('END', 'END')
        ]
        self.assertEqual(tokens, expected)

    def test_numbers(self):
        lexer.input("42 123")
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
        expected = [('NUMBER', 42), ('NUMBER', 123)]
        self.assertEqual(tokens, expected)

    def test_identifiers(self):
        lexer.input("speed x y")
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
        expected = [('ID', 'speed'), ('ID', 'x'), ('ID', 'y')]
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()