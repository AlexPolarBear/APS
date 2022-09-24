from src.UI.UI import UI


class ExceptionHandler(object):
    def __init__(self, ui: UI):
        self.ui = ui

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.ui.print_result(exc_val)
            return True
