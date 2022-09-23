from src.CommandFactory.CommandFactory import CommandFactory
from src.Interpreter.Interpreter import Interpreter
from src.Lexer.Lexer import Lexer
from src.Parser.Parser import Parser
from src.Substitutor.Substitutor import Substitutor
from src.UI.UI import UI


class Controller(object):
    def __init__(self):
        self.env_vars = {}

    def run(self):
        __traceback_hide__ = True
        ui = UI(self)

        while True:
            with ExceptionHandler(ui):
                input_string = ui.read_input()

                lexer = Lexer(self)
                tokens = lexer.parse_to_tokens(input_string)

                substitutor = Substitutor(self)
                input_after_substitution = substitutor.resolve_env_var(tokens)

                final_tokens = lexer.parse_to_tokens(input_after_substitution)

                parser = Parser(self)
                str_commands = parser.parse_commands(final_tokens)

                command_factory = CommandFactory(self)
                commands = command_factory.generate_commands(str_commands)

                interpreter = Interpreter(self)
                result = interpreter.run_commands(commands)

                ui.print_result(result)


class ExceptionHandler(object):
    def __init__(self, ui: UI):
        self.ui = ui

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.ui.print_result(exc_val)
            return True