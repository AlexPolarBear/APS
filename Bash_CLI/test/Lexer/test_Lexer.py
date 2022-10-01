from src.Controller import Controller
from src.Lexer import Lexer


def test_parse_to_tokens_1():
    controller = Controller()
    lexer = Lexer(controller)

    assert lexer.parse_to_tokens('echo go') == ['echo', 'go']


def test_parse_to_tokens_2():
    controller = Controller()
    lexer = Lexer(controller)

    assert lexer.parse_to_tokens('x =       y') == ['x', '=', 'y']


def test_parse_to_tokens_3():
    controller = Controller()
    lexer = Lexer(controller)

    assert lexer.parse_to_tokens('pwd "home/user/home = ab" "s=t" -v ') == \
           ['pwd', '"', 'home/user/home = ab', '"', '"', 's=t', '"', '-v']


def test_parse_to_tokens_4():
    controller = Controller()
    lexer = Lexer(controller)

    assert lexer.parse_to_tokens('cat \'$x$y = $exit\'') == ['cat', "'$x$y = $exit'"]


def test_parse_to_tokens_5():
    controller = Controller()
    lexer = Lexer(controller)

    assert lexer.parse_to_tokens('abc \'"raz, dva"\' " \' aaaa \' hhhhh \' " \' fffff') == \
           ['abc', '\'"raz, dva"\'', '"', " ' aaaa ' hhhhh ' ", '"', "' fffff"]

def test_parse_to_tokens_6():
    controller = Controller()
    lexer = Lexer(Controller)

    assert lexer.parse_to_tokens('$x$y = 15') == ['$x', '$y', '=', '15']

def test_parse_to_tokens_7():
    controller = Controller()
    lexer = Lexer(Controller)

    assert lexer.parse_to_tokens('x = ex | y = it|$x$y') == ['x', '=', 'ex', '|', 'y', '=', 'it', '|', '$x', '$y']

def test_parse_to_tokens_8():
    controller = Controller()
    lexer = Lexer(Controller)

    assert lexer.parse_to_tokens('$x\'aboba$y\' "$x$y" \'"$r\' = 15') == \
        ['$x', '\'aboba$y\'', '"', '$x', '$y', '"', '\'"$r\'', '=', '15']

def test_parse_to_tokens_9():
    controller = Controller()
    lexer = Lexer(Controller)

    assert lexer.parse_to_tokens('wc | cat " | echo $___12" \' x=ex | $123 \' | pwd') == \
        ['wc', '|', 'cat', '"', ' | echo ', '$___12', '"', '\' x=ex | $123 \'', '|', 'pwd']
