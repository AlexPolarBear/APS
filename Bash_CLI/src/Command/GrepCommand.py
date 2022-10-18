import argparse
import io
import sys
from typing import Optional, List, Tuple, Sequence

from src.Command import Command
from src.Controller import Controller
from src.Token import Token
import re


class GrepCommand(Command):
    """Class representing the grep command.
    Grep is a small command for finding matching patterns.
    """
    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('grep', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of grep command."""
        try:
            args = self._parse_args()
        except Exception as exc:
            return '', str(exc), -1

        pattern = args.pattern
        whole_word = args.w
        ignore_case = args.i
        lines_after = args.A

        string_to_print = ''
        lines_to_print = 0

        regex = re.compile(fr'\b{pattern}\b' if whole_word else pattern, re.IGNORECASE if ignore_case else 0)

        for line in stdin.splitlines():
            if regex.search(line):
                lines_to_print = 1 + lines_after

            if lines_to_print > 0:
                string_to_print += line + '\n'
                lines_to_print -= 1

        return string_to_print[:-1], '', 0

    def _parse_args(self) -> argparse.Namespace:
        """Check if the arguments are valid."""
        str_args = list(map(str.strip, map(str, self.args)))

        parser = argparse.ArgumentParser(prog='grep', description='Find matching patterns.')
        parser.add_argument('pattern', type=str, help='The pattern to search for.')
        parser.add_argument('-w', action='store_true', help='Search for the whole word.')
        parser.add_argument('-i', action='store_true', help='File to search in.')
        parser.add_argument('-A', type=int, default=0, help='Print the number of lines after match.')

        fake_stdout = io.StringIO()
        current_stdout = sys.stdout
        sys.stdout = fake_stdout
        try:
            args = parser.parse_args(str_args)
        except SystemExit:
            raise RuntimeError(fake_stdout.getvalue())
        finally:
            sys.stdout = current_stdout

        return args
