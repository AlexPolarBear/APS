from typing import List
from itertools import chain
import string

from src.Controller import Controller


class Lexer(object):
    """Class for creation an array of tokens from raw command line."""

    def __init__(self, controller: Controller):
        self.controller = controller
        self._variable_symbols = set(string.ascii_letters) | set(string.digits) | set('_')
    
    def _process_equation_and_space(self, arg_str: str) -> List[str]:
        """Split the string for the symbols " " and "="."""

        tokens = arg_str.split(' ')
        tokens = list(map(lambda s: s.split('='), tokens))
        for idx, arr in enumerate(tokens):
            new_arr = []
            for ind, s in enumerate(arr):
                if ind != 0:
                    new_arr.append('=')
                new_arr.append(s)
            tokens[idx] = new_arr
        
        tokens = chain.from_iterable(tokens)
        return list(filter(lambda s: len(s) > 0, tokens))

    def _process_environment_variables(self, arg_str: str) -> List[str]:
        """Find usage of environment variables and create tokens from it."""
        idx = 0
        tokens = []
        last_split = 0
        while idx < len(arg_str):
            if arg_str[idx] == '$':
                tokens.append(arg_str[last_split:idx])
                idx_var = idx + 1
                while idx_var < len(arg_str) and arg_str[idx_var] in self._variable_symbols:
                    idx_var += 1
                print(arg_str[idx:idx_var])
                tokens.append(arg_str[idx:idx_var])
                idx = idx_var
                last_split = idx_var
            else:
                idx += 1
        tokens.append(arg_str[last_split:])
        return list(filter(lambda s: len(s) > 0, tokens))
    
    def _process_double_quotation(self, arg_str: str) -> List[str]:
        """Split the string for the symbol "\"" and process each substring separately."""
        
        tokens = arg_str.split('"')
        final_tokens = []
        for idx, s in enumerate(tokens):
            if idx % 2 == 0:
                after_subst = self._process_environment_variables(s)
                for t in after_subst:
                    if not t.startswith('$'):
                        final_tokens.extend(self._process_equation_and_space(t))
                    else:
                        final_tokens.append(t)
            else:
                final_tokens.append('"')
                final_tokens.extend(self._process_environment_variables(s))
                if idx != len(tokens) - 1:
                    final_tokens.append('"')
        return list(filter(lambda s: len(s) > 0, final_tokens))

    def _process_single_quotation(self, arg_str: str) -> List[str]:
        """Split the string for the symbol "'" and process each substring separately."""

        open_single_quotation = False
        open_double_quotation = False
        tokens = []
        last_split = 0
        for idx, symb in enumerate(arg_str):
            if symb == "'":
                if open_single_quotation:
                    tokens.append(arg_str[last_split:(idx + 1)])
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
            tokens.append(arg_str[last_split:])
        else:
            tokens.extend(self._process_double_quotation(arg_str[last_split:]))
        return list(filter(lambda s: len(s) > 0, tokens))

    def _process_pipe(self, arg_str: str) -> List[str]:
        """Split the string for the symbol '|' and process each substring separately."""

        open_single_quotation = False
        open_double_quotation = False
        tokens = []
        last_split = 0
        for idx, symb in enumerate(arg_str):
            if symb == '|':
                if not open_single_quotation and not open_double_quotation:
                    tokens.extend(self._process_single_quotation(arg_str[last_split:idx]))
                    tokens.append('|')
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
        return list(filter(lambda s: len(s) > 0, tokens))

    def parse_to_tokens(self, arg_str: str) -> List[str]:
        """Generate array of tokens from raw command line."""

        return self._process_pipe(arg_str)
