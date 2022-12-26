import re
import sys
from io import StringIO

from src import GameClient
from src.GameClient.InputProvider import StrSequenceInputProvider
from src.Model import Model

reference_output = """############################################################
@ . . . . . █ █ █ . █ . . . █ . █ . █ . █ █ █ . █ . █ . . .
. . . █ . . █ █ . █ . . █ . . . █ . . █ █ █ . . █ . █ █ █ █
█ . . . █ . █ . █ . . █ . █ . . . . █ . █ █ . █ █ █ █ . █ .
█ . . █ █ . . . █ █ . █ █ . . . . █ █ █ . . . . █ █ . . █ █
. . █ . █ █ . █ . █ . █ . █ . █ . █ █ . . . █ . . . . . . .
. █ █ . . . █ . █ █ . . █ █ . █ . . █ . . █ █ █ █ █ . . . .
. █ █ . . . . █ █ . █ . █ . . . █ . . . █ . . █ . █ . █ █ .
. █ █ . . █ . . █ . . . █ █ . █ . █ █ . █ █ . █ █ . █ . . .
. █ █ . █ █ . . . . █ █ █ █ █ . . . . . . █ █ . . . . . . .
. . . . . █ █ . █ █ █ . . █ █ █ █ █ █ █ . █ █ █ . . . █ . .
============================================================
HP: 10 AP: 1 XP: 0 Level: 1                                 
############################################################
"""

reference_output_backpack = """############################################################
                           Backpack
 
 
 
 
 
 
 
 
 
 
Press space to activate/deactivate item
############################################################
"""


def test_game_client_map_print():
    model = Model.from_save('test_map.txt')
    input_provider = StrSequenceInputProvider([])

    string_io = StringIO()
    prev_io, sys.stdout = sys.stdout, string_io
    GameClient(model, input_provider)
    sys.stdout = prev_io

    for ref_line, output_line in zip(reference_output.splitlines(), string_io.getvalue().splitlines()):
        for ref_symbol, output_symbol in zip(ref_line, output_line):
            if ref_symbol in {'@', '#', ' ', '█', 'H', 'P', 'X', '1', '0', 'L', 'e', 'v', 'e', 'l'}:
                assert ref_symbol == output_symbol


def test_game_client_hero_move():
    successful_start = False
    input_provider = StrSequenceInputProvider(['right'])
    while not successful_start:
        model = Model.from_save('test_map.txt')
        string_io = StringIO()
        prev_io, sys.stdout = sys.stdout, string_io
        game_client = GameClient(model, input_provider)
        sys.stdout = prev_io

        if string_io.getvalue().splitlines()[1][2] == '.':
            successful_start = True

    try:
        string_io = StringIO()
        prev_io, sys.stdout = sys.stdout, string_io
        game_client.play()
        sys.stdout = prev_io
    except SystemExit:
        pass

    assert string_io.getvalue().splitlines()[1][2] == '@'


def test_game_client_backpack():
    input_provider = StrSequenceInputProvider(['tab'])
    model = Model()
    string_io = StringIO()
    prev_io, sys.stdout = sys.stdout, string_io
    game_client = GameClient(model, input_provider)
    sys.stdout = prev_io

    try:
        string_io = StringIO()
        prev_io, sys.stdout = sys.stdout, string_io
        game_client.play()
    except SystemExit:
        pass
    sys.stdout = prev_io

    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result = ansi_escape.sub('', string_io.getvalue())

    assert len(result.splitlines()) == len(reference_output_backpack.splitlines())

    for ref_line, output_line in zip(reference_output_backpack.splitlines(), result.splitlines()):
        assert ref_line.strip() == output_line.strip()
