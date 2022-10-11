import subprocess
from dataclasses import dataclass
from typing import List, Optional, Tuple

from src.Controller import Controller


@dataclass
class Command(object):
    """Base class for all commands.

    Attributes
    ----------
    name : str
        The name of the command.
    args : List[str]
        The list of arguments for the command.
    """
    name: Optional[str] = None
    args: Optional[List[str]] = None

    def __post_init__(self):
        """Check the correctness of the initialisation and fill in default values."""
        if self.name is None:
            raise ValueError('Command name is empty')
        if self.args is None:
            self.args = []

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Run the command in a subshell and return the output string, error string and return code.

        Parameters
        ----------
        stdin : str
            The input string for the command.
        controller : Controller
            The controller object which contains current execution context.

        Returns
        -------
        Tuple[str, str, int]
            The output string, error string and return code.
        """
        res = subprocess.run(
            self.name + ' ' + ' '.join(self.args),
            input=stdin,
            shell=True,
            text=True,
            capture_output=True,
        )

        return res.stdout, res.stderr, res.returncode
