from src.Controller.Controller import Controller


class UI(object):
    def __init__(self, controller: Controller):
        self.controller = controller

    def read_input(self):
        return input('>>> ')

    def print_result(self, result: str):
        print(result)
