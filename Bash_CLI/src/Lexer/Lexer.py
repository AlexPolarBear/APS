from typing import List
from itertools import chain

from src.Controller import Controller


class Lexer(object):
    def __init__(self, controller: Controller):
        self.controller = controller
    
    def _process_equation_and_space(self, arg_str: str) -> List[str]:
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
    
    def _process_double_quotation(self, arg_str: str) -> List[str]:
        tokens = arg_str.split('"')
        final_tokens = []
        for idx, s in enumerate(tokens):
            if idx % 2 == 0:
                final_tokens.extend(self._process_equation_and_space(s))
            else:
                new_s = '"' + s
                if idx != len(tokens) - 1:
                    new_s += '"'
                final_tokens.append(new_s)
        return list(filter(lambda s: len(s) > 0, final_tokens))

    def _process_single_quotation(self, arg_str: str) -> List[str]:
        open_single_quotation = False
        open_double_quotation = False
        current_str = ''
        tokens = []
        for symb in arg_str:
            if symb == "'":
                if open_single_quotation:
                    current_str += "'"
                    tokens.append(current_str)
                    open_single_quotation = False
                    current_str = ''
                elif open_double_quotation:
                    current_str += symb
                else:
                    tokens.extend(self._process_double_quotation(current_str))
                    open_single_quotation = True
                    current_str = "'"
            elif symb == '"':
                if open_double_quotation:
                    open_double_quotation = False
                elif not open_single_quotation:
                    open_double_quotation = True
                current_str += symb
            else:
                current_str += symb
        
        if open_single_quotation:
            tokens.append(current_str)
        else:
            tokens.extend(self._process_double_quotation(current_str))
        return list(filter(lambda s: len(s) > 0, tokens))

    def _process_pipe(self, arg_str: str) -> List[str]:
        return self._process_single_quotation(arg_str)

    def parse_to_tokens(self, arg_str: str) -> List[str]:
        return self._process_pipe(arg_str)
