#!/usr/bin/env python3
"""
Lakbay Programming Language - Transpiler to C++
A compiled, object-oriented language

FILE: lakbay.py
"""

import re
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str
    line: int

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.tokens = []
        
    def tokenize(self) -> List[Token]:
        keywords = {
            'class', 'extends', 'func', 'return', 'if', 'else', 
            'while', 'for', 'new', 'this', 'public', 'private',
            'int', 'float', 'string', 'bool', 'void', 'array',
            'print', 'true', 'false'
        }
        
        while self.pos < len(self.code):
            # Skip whitespace
            if self.code[self.pos].isspace():
                if self.code[self.pos] == '\n':
                    self.line += 1
                self.pos += 1
                continue
            
            # Skip comments
            if self.pos < len(self.code) - 1 and self.code[self.pos:self.pos+2] == '//':
                while self.pos < len(self.code) and self.code[self.pos] != '\n':
                    self.pos += 1
                continue
            
            # Numbers
            if self.code[self.pos].isdigit():
                num = ''
                while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == '.'):
                    num += self.code[self.pos]
                    self.pos += 1
                self.tokens.append(Token('NUMBER', num, self.line))
                continue
            
            # Identifiers and keywords
            if self.code[self.pos].isalpha() or self.code[self.pos] == '_':
                ident = ''
                while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
                    ident += self.code[self.pos]
                    self.pos += 1
                token_type = 'KEYWORD' if ident in keywords else 'IDENTIFIER'
                self.tokens.append(Token(token_type, ident, self.line))
                continue
            
            # Strings
            if self.code[self.pos] == '"':
                self.pos += 1
                string = ''
                while self.pos < len(self.code) and self.code[self.pos] != '"':
                    if self.code[self.pos] == '\\' and self.pos + 1 < len(self.code):
                        self.pos += 1
                        escape_chars = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\', '"': '"'}
                        string += escape_chars.get(self.code[self.pos], self.code[self.pos])
                    else:
                        string += self.code[self.pos]
                    self.pos += 1
                self.pos += 1
                self.tokens.append(Token('STRING', string, self.line))
                continue
            
            # Operators and punctuation
            operators = {
                '==': 'EQ', '!=': 'NEQ', '<=': 'LEQ', '>=': 'GEQ',
                '&&': 'AND', '||': 'OR', '++': 'INC', '--': 'DEC'
            }
            
            two_char = self.code[self.pos:self.pos+2]
            if two_char in operators:
                self.tokens.append(Token(operators[two_char], two_char, self.line))
                self.pos += 2
                continue
            
            single_chars = {
                '+': 'PLUS', '-': 'MINUS', '*': 'MULT', '/': 'DIV',
                '=': 'ASSIGN', '<': 'LT', '>': 'GT', '!': 'NOT',
                '(': 'LPAREN', ')': 'RPAREN', '{': 'LBRACE', '}': 'RBRACE',
                '[': 'LBRACKET', ']': 'RBRACKET', ';': 'SEMI', ',': 'COMMA',
                '.': 'DOT', ':': 'COLON'
            }
            
            if self.code[self.pos] in single_chars:
                char = self.code[self.pos]
                self.tokens.append(Token(single_chars[char], char, self.line))
                self.pos += 1
                continue
            
            self.pos += 1
        
        return self.tokens

class Transpiler:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.output = []
        self.indent = 0
        self.classes = {}
        
    def current(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type: str, value: str = None) -> Token:
        token = self.current()
        if not token or token.type != token_type:
            raise Exception(f"Line {token.line if token else '?'}: Expected {token_type}, got {token.type if token else 'EOF'}")
        if value and token.value != value:
            raise Exception(f"Line {token.line}: Expected '{value}', got '{token.value}'")
        self.advance()
        return token
    
    def write(self, code: str):
        self.output.append('    ' * self.indent + code)
    
    def transpile(self) -> str:
        self.output = [
            '#include <iostream>',
            '#include <string>',
            '#include <vector>',
            'using namespace std;',
            ''
        ]
        
        while self.current():
            if self.current().type == 'KEYWORD' and self.current().value == 'class':
                self.transpile_class()
            else:
                self.advance()
        
        # Add main function
        self.output.append('\nint main() {')
        self.output.append('    cout << "Lakbay Program Running..." << endl;')
        self.output.append('    return 0;')
        self.output.append('}')
        
        return '\n'.join(self.output)
    
    def transpile_class(self):
        self.expect('KEYWORD', 'class')
        class_name = self.expect('IDENTIFIER').value
        
        parent = None
        if self.current() and self.current().type == 'KEYWORD' and self.current().value == 'extends':
            self.advance()
            parent = self.expect('IDENTIFIER').value
        
        self.expect('LBRACE')
        
        self.write(f'\nclass {class_name}' + (f' : public {parent}' if parent else '') + ' {')
        self.write('public:')
        self.indent += 1
        
        # Parse class body
        while self.current() and not (self.current().type == 'RBRACE'):
            if self.current().type == 'KEYWORD':
                if self.current().value in ['public', 'private']:
                    visibility = self.current().value
                    self.advance()
                    self.expect('COLON')
                    self.indent -= 1
                    self.write(f'{visibility}:')
                    self.indent += 1
                elif self.current().value == 'func':
                    self.transpile_method(class_name)
                else:
                    self.transpile_property()
            else:
                self.advance()
        
        self.indent -= 1
        self.write('};')
        self.expect('RBRACE')
    
    def transpile_property(self):
        type_name = self.expect('KEYWORD').value
        cpp_type = self.convert_type(type_name)
        var_name = self.expect('IDENTIFIER').value
        
        if self.current() and self.current().type == 'ASSIGN':
            self.advance()
            value = self.transpile_expression()
            self.write(f'{cpp_type} {var_name} = {value};')
        else:
            self.write(f'{cpp_type} {var_name};')
        
        self.expect('SEMI')
    
    def transpile_method(self, class_name: str):
        self.expect('KEYWORD', 'func')
        
        method_name = self.expect('IDENTIFIER').value
        is_constructor = (method_name == class_name)
        
        self.expect('LPAREN')
        params = []
        while self.current() and self.current().type != 'RPAREN':
            param_type = self.expect('KEYWORD').value
            param_name = self.expect('IDENTIFIER').value
            params.append(f'{self.convert_type(param_type)} {param_name}')
            if self.current() and self.current().type == 'COMMA':
                self.advance()
        self.expect('RPAREN')
        
        return_type = 'void'
        if not is_constructor and self.current() and self.current().type == 'COLON':
            self.advance()
            return_type = self.convert_type(self.expect('KEYWORD').value)
        
        param_str = ', '.join(params)
        
        if is_constructor:
            self.write(f'{class_name}({param_str}) {{')
        else:
            self.write(f'{return_type} {method_name}({param_str}) {{')
        
        self.expect('LBRACE')
        self.indent += 1
        
        self.transpile_block()
        
        self.indent -= 1
        self.write('}')
        self.expect('RBRACE')
    
    def transpile_block(self):
        while self.current() and self.current().type != 'RBRACE':
            self.transpile_statement()
    
    def transpile_statement(self):
        token = self.current()
        if not token:
            return
        
        if token.type == 'KEYWORD':
            if token.value == 'return':
                self.advance()
                if self.current() and self.current().type != 'SEMI':
                    expr = self.transpile_expression()
                    self.write(f'return {expr};')
                else:
                    self.write('return;')
                self.expect('SEMI')
            elif token.value == 'if':
                self.transpile_if()
            elif token.value == 'while':
                self.transpile_while()
            elif token.value == 'for':
                self.transpile_for()
            elif token.value == 'print':
                self.transpile_print()
            elif token.value in ['int', 'float', 'string', 'bool']:
                self.transpile_var_declaration()
        else:
            expr = self.transpile_expression()
            self.write(f'{expr};')
            self.expect('SEMI')
    
    def transpile_print(self):
        self.expect('KEYWORD', 'print')
        self.expect('LPAREN')
        args = []
        while self.current() and self.current().type != 'RPAREN':
            args.append(self.transpile_expression())
            if self.current() and self.current().type == 'COMMA':
                self.advance()
        self.expect('RPAREN')
        self.expect('SEMI')
        
        print_stmt = 'cout'
        for arg in args:
            print_stmt += f' << {arg}'
        print_stmt += ' << endl;'
        self.write(print_stmt)
    
    def transpile_if(self):
        self.expect('KEYWORD', 'if')
        self.expect('LPAREN')
        condition = self.transpile_expression()
        self.expect('RPAREN')
        self.expect('LBRACE')
        
        self.write(f'if ({condition}) {{')
        self.indent += 1
        self.transpile_block()
        self.indent -= 1
        self.write('}')
        self.expect('RBRACE')
        
        if self.current() and self.current().type == 'KEYWORD' and self.current().value == 'else':
            self.advance()
            self.expect('LBRACE')
            self.write('else {')
            self.indent += 1
            self.transpile_block()
            self.indent -= 1
            self.write('}')
            self.expect('RBRACE')
    
    def transpile_while(self):
        self.expect('KEYWORD', 'while')
        self.expect('LPAREN')
        condition = self.transpile_expression()
        self.expect('RPAREN')
        self.expect('LBRACE')
        
        self.write(f'while ({condition}) {{')
        self.indent += 1
        self.transpile_block()
        self.indent -= 1
        self.write('}')
        self.expect('RBRACE')
    
    def transpile_for(self):
        self.expect('KEYWORD', 'for')
        self.expect('LPAREN')
        init = self.transpile_expression()
        self.expect('SEMI')
        condition = self.transpile_expression()
        self.expect('SEMI')
        update = self.transpile_expression()
        self.expect('RPAREN')
        self.expect('LBRACE')
        
        self.write(f'for ({init}; {condition}; {update}) {{')
        self.indent += 1
        self.transpile_block()
        self.indent -= 1
        self.write('}')
        self.expect('RBRACE')
    
    def transpile_var_declaration(self):
        type_name = self.expect('KEYWORD').value
        cpp_type = self.convert_type(type_name)
        var_name = self.expect('IDENTIFIER').value
        
        if self.current() and self.current().type == 'ASSIGN':
            self.advance()
            value = self.transpile_expression()
            self.write(f'{cpp_type} {var_name} = {value};')
        else:
            self.write(f'{cpp_type} {var_name};')
        
        self.expect('SEMI')
    
    def transpile_expression(self) -> str:
        return self.transpile_logical_or()
    
    def transpile_logical_or(self) -> str:
        left = self.transpile_logical_and()
        while self.current() and self.current().type == 'OR':
            self.advance()
            right = self.transpile_logical_and()
            left = f'({left} || {right})'
        return left
    
    def transpile_logical_and(self) -> str:
        left = self.transpile_equality()
        while self.current() and self.current().type == 'AND':
            self.advance()
            right = self.transpile_equality()
            left = f'({left} && {right})'
        return left
    
    def transpile_equality(self) -> str:
        left = self.transpile_comparison()
        while self.current() and self.current().type in ['EQ', 'NEQ']:
            op = '==' if self.current().type == 'EQ' else '!='
            self.advance()
            right = self.transpile_comparison()
            left = f'({left} {op} {right})'
        return left
    
    def transpile_comparison(self) -> str:
        left = self.transpile_term()
        while self.current() and self.current().type in ['LT', 'GT', 'LEQ', 'GEQ']:
            op = {'LT': '<', 'GT': '>', 'LEQ': '<=', 'GEQ': '>='}[self.current().type]
            self.advance()
            right = self.transpile_term()
            left = f'({left} {op} {right})'
        return left
    
    def transpile_term(self) -> str:
        left = self.transpile_factor()
        while self.current() and self.current().type in ['PLUS', 'MINUS']:
            op = '+' if self.current().type == 'PLUS' else '-'
            self.advance()
            right = self.transpile_factor()
            left = f'({left} {op} {right})'
        return left
    
    def transpile_factor(self) -> str:
        left = self.transpile_unary()
        while self.current() and self.current().type in ['MULT', 'DIV']:
            op = '*' if self.current().type == 'MULT' else '/'
            self.advance()
            right = self.transpile_unary()
            left = f'({left} {op} {right})'
        return left
    
    def transpile_unary(self) -> str:
        if self.current() and self.current().type in ['MINUS', 'NOT']:
            op = '-' if self.current().type == 'MINUS' else '!'
            self.advance()
            return f'{op}{self.transpile_unary()}'
        return self.transpile_postfix()
    
    def transpile_postfix(self) -> str:
        expr = self.transpile_primary()
        
        while self.current():
            if self.current().type == 'DOT':
                self.advance()
                member = self.expect('IDENTIFIER').value
                if self.current() and self.current().type == 'LPAREN':
                    self.advance()
                    args = []
                    while self.current() and self.current().type != 'RPAREN':
                        args.append(self.transpile_expression())
                        if self.current() and self.current().type == 'COMMA':
                            self.advance()
                    self.expect('RPAREN')
                    expr = f'{expr}.{member}({", ".join(args)})'
                else:
                    expr = f'{expr}.{member}'
            elif self.current().type == 'LPAREN':
                self.advance()
                args = []
                while self.current() and self.current().type != 'RPAREN':
                    args.append(self.transpile_expression())
                    if self.current() and self.current().type == 'COMMA':
                        self.advance()
                self.expect('RPAREN')
                expr = f'{expr}({", ".join(args)})'
            elif self.current().type == 'LBRACKET':
                self.advance()
                index = self.transpile_expression()
                self.expect('RBRACKET')
                expr = f'{expr}[{index}]'
            elif self.current().type == 'ASSIGN':
                self.advance()
                value = self.transpile_expression()
                expr = f'{expr} = {value}'
            else:
                break
        
        return expr
    
    def transpile_primary(self) -> str:
        token = self.current()
        
        if token.type == 'NUMBER':
            self.advance()
            return token.value
        elif token.type == 'STRING':
            self.advance()
            return f'"{token.value}"'
        elif token.type == 'IDENTIFIER':
            self.advance()
            return token.value
        elif token.type == 'KEYWORD' and token.value == 'this':
            self.advance()
            return 'this'
        elif token.type == 'KEYWORD' and token.value == 'true':
            self.advance()
            return 'true'
        elif token.type == 'KEYWORD' and token.value == 'false':
            self.advance()
            return 'false'
        elif token.type == 'KEYWORD' and token.value == 'new':
            self.advance()
            class_name = self.expect('IDENTIFIER').value
            self.expect('LPAREN')
            args = []
            while self.current() and self.current().type != 'RPAREN':
                args.append(self.transpile_expression())
                if self.current() and self.current().type == 'COMMA':
                    self.advance()
            self.expect('RPAREN')
            return f'new {class_name}({", ".join(args)})'
        elif token.type == 'LPAREN':
            self.advance()
            expr = self.transpile_expression()
            self.expect('RPAREN')
            return f'({expr})'
        
        raise Exception(f'Line {token.line}: Unexpected token: {token.type} {token.value}')
    
    def convert_type(self, lakbay_type: str) -> str:
        type_map = {
            'int': 'int',
            'float': 'float',
            'string': 'string',
            'bool': 'bool',
            'void': 'void'
        }
        return type_map.get(lakbay_type, lakbay_type)

def compile_lakbay(source_code: str) -> str:
    """Main compilation function"""
    try:
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        transpiler = Transpiler(tokens)
        cpp_code = transpiler.transpile()
        
        return cpp_code
    except Exception as e:
        return f"ERROR: {str(e)}"