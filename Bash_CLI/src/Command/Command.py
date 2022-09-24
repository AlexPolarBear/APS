import subprocess
from dataclasses import dataclass
from io import StringIO
from typing import List, Optional, Tuple

import src.Controller.Controller as Controller


@dataclass
class Command(object):
    name: Optional[str] = None
    args: Optional[List[str]] = None

    def __post_init__(self):
        if self.name is None:
            raise ValueError('Command name is empty')
        if self.args is None:
            self.args = []

    def run(self, stdin: str, controller: Controller.Controller) -> Tuple[str, str, int]:
        input_stream = StringIO(stdin)
        output_stream = StringIO()
        err_stream = StringIO()

        res = subprocess.call(
            self.name + ' ' + ' '.join(self.args),
            shell=True,
            stdin=input_stream,
            stdout=output_stream,
            stderr=err_stream,
        )

        return output_stream.getvalue(), err_stream.getvalue(), res
