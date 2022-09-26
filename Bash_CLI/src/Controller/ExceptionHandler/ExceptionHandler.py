import sys
import traceback

from src.UI import UI


class ExceptionHandler(object):
    """Context manager for handling exceptions.
    If the exception raises it prints the exception message to the UI
    and returns True to indicate that the exception was handled.
    """
    def __init__(self, ui: UI):
        self.ui = ui

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in (KeyboardInterrupt, SystemExit):
            sys.exit(0)

        if exc_type is not None:
            self.ui.print_result(exc_val)
            traceback.print_exc(exc_val)
            return True
