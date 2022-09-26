class Controller(object):
    """Class that contains the execution context and controls the flow of the program.

    Attributes
    ----------
    env_vars : dict
        Dictionary that contains the environment variables.
    """

    def __init__(self):
        self.env_vars = {}

    def run(self):
        """Run the CLI loop."""
        from src.CommandFactory import CommandFactory
        from src.Controller import ExceptionHandler
        from src.Interpreter import Interpreter
        from src.Lexer import Lexer
        from src.Parser import Parser
        from src.Substitutor import Substitutor
        from src.UI import UI

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
