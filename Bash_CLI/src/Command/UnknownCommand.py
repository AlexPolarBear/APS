from src.Command import Command


class UnknownCommand(Command):
    """Class representing an unknown command.
    It is used when the user enters a command that is not recognized by the CLI.
    Its behaviour is fully defined by the Command class.
    """
    pass
