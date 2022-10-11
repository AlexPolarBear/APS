from typing import List, Optional, Tuple
import os

from src.Command import Command
from src.Controller import Controller


class WcCommand(Command):
    """Class representing the wc command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__('wc', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of wc command."""
        try:
            if len(self.args) > 0:
                with open(self.args[0], 'r') as input_file:
                    lines_in_file = 0
                    words_in_file = 0
                    bytes_in_file = os.path.getsize(self.args[0])
                    for line in input_file:
                        lines_in_file += 1
                        words_in_file += len(line.split())
            else:
                bytes_in_file = len(stdin.encode('utf-8'))
                lines = stdin.split('\n')
                lines_in_file = len(lines)
                words_in_file = 0
                for line in lines:
                    words_in_file += len(line.split())
        except Exception as exc:
            return '', str(exc), -1
        return '{0}  {1}  {2}'.format(lines_in_file, words_in_file, bytes_in_file), '', 0
