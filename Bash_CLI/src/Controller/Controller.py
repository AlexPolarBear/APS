import src.CommandFactory.CommandFactory as CommandFactory
import src.Controller.ExceptionHandler.ExceptionHandler as ExceptionHandler
import src.Interpreter.Interpreter as Interpreter
import src.Lexer.Lexer as Lexer
import src.Parser.Parser as Parser
import src.Substitutor.Substitutor as Substitutor
import src.UI.UI as UI


class Controller(object):
    def __init__(self):
        self.env_vars = {}

    def run(self):
        __traceback_hide__ = True
        ui = UI(self)

        while True:
            with ExceptionHandler.ExceptionHandler(ui):
                input_string = ui.read_input()

                lexer = Lexer.Lexer(self)
                tokens = lexer.parse_to_tokens(input_string)

                substitutor = Substitutor.Substitutor(self)
                input_after_substitution = substitutor.resolve_env_var(tokens)

                final_tokens = lexer.parse_to_tokens(input_after_substitution)

                parser = Parser.Parser(self)
                str_commands = parser.parse_commands(final_tokens)

                command_factory = CommandFactory.CommandFactory(self)
                commands = command_factory.generate_commands(str_commands)

                interpreter = Interpreter.Interpreter(self)
                result = interpreter.run_commands(commands)

                ui.print_result(result)
