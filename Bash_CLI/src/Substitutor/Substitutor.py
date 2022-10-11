from typing import List

from src.Controller import Controller
from src.Token import Token

class Substitutor(object):
    """Class for substitution environment variables."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def resolve_env_vars(self, list_tokens: List[Token]) -> str:
        """Substitute environment variables in the list of tokens."""

        result_string = ''
        for token in list_tokens:
            if token.data.startswith('$') and token.quotation != "'":
                env_var = token.data[1:]
                token.data = self.controller.env_vars.get(env_var, '')
            result_string += str(token)
        return result_string
