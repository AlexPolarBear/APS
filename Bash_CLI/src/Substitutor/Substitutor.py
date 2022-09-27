from src.Controller import Controller


class Substitutor(object):
    """Class for substitution environment variables."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def resolve_env_vars(self, list_tokens):
        """Substitute environment variables in the list of tokens."""
        
        return ' '.join(list_tokens)
