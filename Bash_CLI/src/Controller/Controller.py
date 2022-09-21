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
        # TODO
        while True:
            ui = UI(self)
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
