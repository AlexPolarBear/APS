from src.Controller import Controller


class Substitutor(object):
    def __init__(self, controller: Controller):
        self.controller = controller

    def resolve_env_vars(self, list_tokens):
        return ' '.join(list_tokens)
