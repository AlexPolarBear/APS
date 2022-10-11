from typing import List

from src.Parser import Parser
from src.Controller import Controller
from src.Token import Token
from src.Lexer import Lexer


def equals_token(list1: List[List[Token]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for idx in range(len(list1)):
        if len(list1[idx]) != len(list2[idx]):
            return False
        for index, token in enumerate(list1[idx]):
            if token.data != list2[idx][index]:
                return False
    return True

def test_parse_commands_1():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('cat aga    aboba|wc \'#x&y\''))
    assert equals_token(result, [['cat', 'aga', 'aboba'], ['wc', '#x&y']])

def test_parse_commands_2():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('echo go '))
    assert equals_token(result, [['echo', 'go']])

def test_parse_commands_3():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('pwd "home/user/home = ab" "s=t" -v '))
    assert equals_token(result, [['pwd', 'home/user/home = ab', 's=t', '-v']])

def test_parse_commands_4():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('cat \'$x$y = $exit\''))
    assert equals_token(result, [['cat', '$x$y = $exit']])

def test_parse_commands_5():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('abc \'"raz, dva"\' " \' aaaa \' hhhhh \' " \' fffff'))
    assert equals_token(result, [['abc', '"raz, dva"', ' \' aaaa \' hhhhh \' ', ' fffff']])

def test_parse_commands_6():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('x = ex | y = it|$x$y'))
    assert equals_token(result, [['x', '=', 'ex'], ['y', '=', 'it'], ['$x', '$y']])

def test_parse_commands_7():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('$x\'aboba$y\' "$x$y" \'"$r\' = 15'))
    assert equals_token(result, [['$x', 'aboba$y', '$x$y', '"$r', '=', '15']])

def test_parse_commands_8():
    controller = Controller()
    parser = Parser(controller)

    lexer = Lexer(controller)
    result = parser.parse_commands(lexer.parse_to_tokens('wc | cat " | echo $___12" \' x=ex | $123 \' | pwd'))
    assert equals_token(result, [['wc'], ['cat', ' | echo $___12', ' x=ex | $123 '], ['pwd']])
