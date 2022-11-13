from dataclasses import dataclass

from src.dataclasses import Button


@dataclass
class Command(object):
    button: Button
