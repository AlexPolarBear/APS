from src.GameClient.InputProvider import StrSequenceInputProvider
from src.dataclasses import Button


def test_str_sequence_input_provider_get_user_button_1():
    input_provider = StrSequenceInputProvider(['a', 'b', 'c'])
    assert input_provider.get_user_button() == Button('a')
    assert input_provider.get_user_button() == Button('b')
    assert input_provider.get_user_button() == Button('c')


def test_str_sequence_input_provider_get_user_button_2():
    input_provider = StrSequenceInputProvider([])
    assert input_provider.get_user_button() == Button('esc')
    assert input_provider.get_user_button() == Button('esc')


def test_str_sequence_input_provider_get_user_button_3():
    input_provider = StrSequenceInputProvider(['space', 'shift', 'w', 'a', 'up'])
    assert input_provider.get_user_button() == Button('space')
    assert input_provider.get_user_button() == Button('shift')
    assert input_provider.get_user_button() == Button('w')
    assert input_provider.get_user_button() == Button('a')
    assert input_provider.get_user_button() == Button('up')
    assert input_provider.get_user_button() == Button('esc')
