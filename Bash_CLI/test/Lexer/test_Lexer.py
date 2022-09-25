import src.Lexer.Lexer as Lexer
import src.Controller.Controller as Controller


def test_parse_to_tokens_1():
    controller = Controller.Controller()
    lexer = Lexer.Lexer(controller)

    assert lexer.parse_to_tokens('echo go') == ['echo', 'go']

def test_parse_to_tokens_2():
    controller = Controller.Controller()
    lexer = Lexer.Lexer(controller)

    assert lexer.parse_to_tokens('x =       y') == ['x', '=', 'y']

def test_parse_to_tokens_3():
    controller = Controller.Controller()
    lexer = Lexer.Lexer(controller)

    assert lexer.parse_to_tokens('pwd "home/user/home = ab" "s=t" -v ') == \
        ['pwd', '"home/user/home = ab"', '"s=t"', '-v']

def test_parse_to_tokens_4():
    controller = Controller.Controller()
    lexer = Lexer.Lexer(controller)

    assert lexer.parse_to_tokens('cat \'$x$y = $exit\'') == ['cat', "'$x$y = $exit'"]

def test_parse_to_tokens_5():
    controller = Controller.Controller()
    lexer = Lexer.Lexer(controller)

    assert lexer.parse_to_tokens('abc \'"raz, dva"\' " \' aaaa \' hhhhh \' " \' fffff') == \
                ['abc', '\'"raz, dva"\'', "\" ' aaaa ' hhhhh ' \"", "' fffff"]
