from typing import List
import string

from src.Controller import Controller
from src.Token import Token


class Lexer(object):
    """Class for creation an array of tokens from raw command line."""

    def __init__(self, controller: Controller):
        self.controller = controller
        self._variable_symbols = set(string.ascii_letters) | set(string.digits) | set('_')
    
    def _process_equation_and_space(self, arg_str: str) -> List[Token]:
        """Split the string for the symbols " " and "="."""

        tokens = arg_str.split(' ')
        tokens = list(map(lambda s: s.split('='), tokens))
        final_tokens = []
        for arr in tokens:
            for ind, s in enumerate(arr):
                if ind != 0:
                    final_tokens.append(Token('=', ' ', ''))
                final_tokens.append(Token(s, ' ', ''))
        
        return list(filter(lambda token: token, final_tokens))

    def _process_environment_variables(self, arg_str: str) -> List[Token]:
        """Find usage of environment variables and create tokens from it."""
        idx = 0
        tokens = []
        last_split = 0
        while idx < len(arg_str):
            if arg_str[idx] == '$':
                tokens.append(Token(arg_str[last_split:idx], '', ''))
                idx_var = idx + 1
                while idx_var < len(arg_str) and arg_str[idx_var] in self._variable_symbols:
                    idx_var += 1
                tokens.append(Token(arg_str[idx:idx_var], '', ''))
                idx = idx_var
                last_split = idx_var
            else:
                idx += 1
        tokens.append(Token(arg_str[last_split:], '', ''))
        return list(filter(lambda token: token, tokens))
    
    def _process_double_quotation(self, arg_str: str) -> List[Token]:
        """Split the string for the symbol "\"" and process each substring separately."""
        
        tokens = arg_str.split('"')
        final_tokens = []
        for idx, s in enumerate(tokens):
            if idx % 2 == 0:
                split_space_equation = self._process_equation_and_space(s)
                for token in split_space_equation:
                    split_env = self._process_environment_variables(token.data)
                    if len(split_env) > 0:
                        split_env[-1].separator = ' '
                    final_tokens.extend(split_env)
            else:
                final_tokens.append(Token('"', '', ''))
                final_tokens.extend(self._process_environment_variables(s))
                final_tokens.append(Token('"', '', ''))
                
        return list(filter(lambda token: token, final_tokens))

    def _process_single_quotation(self, arg_str: str) -> List[Token]:
        """Split the string for the symbol "'" and process each substring separately."""

        open_single_quotation = False
        open_double_quotation = False
        tokens = []
        last_split = 0
        for idx, symb in enumerate(arg_str):
            if symb == "'":
                if open_single_quotation:
                    tokens.append(Token(arg_str[(last_split + 1):idx], '', "'"))
                    open_single_quotation = False
                    last_split = idx + 1
                elif not open_double_quotation:
                    tokens.extend(self._process_double_quotation(arg_str[last_split:idx]))
                    open_single_quotation = True
                    last_split = idx
            elif symb == '"':
                if open_double_quotation:
                    open_double_quotation = False
                elif not open_single_quotation:
                    open_double_quotation = True
        
        if open_single_quotation:
            tokens.append(Token(arg_str[(last_split + 1):], '', "'"))
        else:
            tokens.extend(self._process_double_quotation(arg_str[last_split:]))
        return list(filter(lambda token: token, tokens))

    def _process_pipe(self, arg_str: str) -> List[Token]:
        """Split the string for the symbol '|' and process each substring separately."""

        open_single_quotation = False
        open_double_quotation = False
        tokens = []
        last_split = 0
        for idx, symb in enumerate(arg_str):
            if symb == '|':
                if not open_single_quotation and not open_double_quotation:
                    tokens.extend(self._process_single_quotation(arg_str[last_split:idx]))
                    tokens.append(Token('|', '', ''))
                    last_split = idx + 1
            if symb == '"':
                if open_double_quotation:
                    open_double_quotation = False
                elif not open_single_quotation:
                    open_double_quotation = True
            if symb == "'":
                if open_single_quotation:
                    open_single_quotation = False
                elif not open_double_quotation:
                    open_single_quotation = True

        tokens.extend(self._process_single_quotation(arg_str[last_split:]))
        return tokens

    def parse_to_tokens(self, arg_str: str) -> List[Token]:
        """Generate array of tokens from raw command line."""

        return self._process_pipe(arg_str)
