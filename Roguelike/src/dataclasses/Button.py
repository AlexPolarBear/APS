from dataclasses import dataclass


@dataclass
class Button(object):
    """Contain a key name which was pressed by user."""
    key: str
