from typing import List

from src.Controller import Controller
from src.Token import Token


class Parser(object):
    """Class for splitting the list of tokens into separate commands."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def parse_commands(self, list_tokens: List[Token]) -> List[List[Token]]:
        """Split list_tokens into separate commands."""

        merge_double_quotation = []
        open_double_quotation = False
        inside_quotation = ''
        for token in list_tokens:
            if token.data == '"':
                if open_double_quotation:
                    merge_double_quotation.append(Token(inside_quotation, '', '"'))
                    inside_quotation = ''
                open_double_quotation = not open_double_quotation
            else:
                if open_double_quotation:
                    inside_quotation += str(token)
                else:
                    merge_double_quotation.append(token)
        
        list_commands = []
        last_command = []
        for token in merge_double_quotation:
            if token.data == '|' and token.quotation == '':
                if len(last_command) > 0:
                    list_commands.append(last_command)
                last_command = []
            else:
                last_command.append(token)
        if len(last_command) > 0:
            list_commands.append(last_command)
        
        return list_commands
