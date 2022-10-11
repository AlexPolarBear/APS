from src.Controller import Controller
from src.Lexer import Lexer


def test_parse_to_tokens_1():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('echo go')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'echo go '


def test_parse_to_tokens_2():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('x =       y')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'x = y '


def test_parse_to_tokens_3():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('pwd "home/user/home = ab" "s=t" -v ')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'pwd "home/user/home = ab""s=t"-v '


def test_parse_to_tokens_4():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('cat \'$x$y = $exit\'')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'cat \'$x$y = $exit\''


def test_parse_to_tokens_5():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('abc \'"raz, dva"\' " \' aaaa \' hhhhh \' " \' fffff')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'abc \'"raz, dva"\'" \' aaaa \' hhhhh \' "\' fffff\''

def test_parse_to_tokens_6():
    controller = Controller()
    lexer = Lexer(controller)
    
    tokens = lexer.parse_to_tokens('$x$y = 15')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == '$x$y = 15 '

def test_parse_to_tokens_7():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('x = ex | y = it|$x$y')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'x = ex |y = it |$x$y '

def test_parse_to_tokens_8():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('$x\'aboba$y\' "$x$y" \'"$r\' = 15')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == '$x \'aboba$y\'"$x$y"\'"$r\'= 15 '

def test_parse_to_tokens_9():
    controller = Controller()
    lexer = Lexer(controller)

    tokens = lexer.parse_to_tokens('wc | cat " | echo $___12" \' x=ex | $123 \' | pwd')
    final_str = ''
    for token in tokens:
        final_str += str(token)
    assert final_str == 'wc |cat " | echo $___12"\' x=ex | $123 \'|pwd '
