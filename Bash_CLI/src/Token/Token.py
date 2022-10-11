from dataclasses import dataclass

@dataclass
class Token(object):
    """
    Class, that store data-string and some useful information about it:
    separator, that follows data-string, and quotation, that wraps data-string.
    """
    _data: str
    _separator_after_str: str
    _quotation: str
    
    def __str__(self) -> str:
        return self._quotation + self._data + self._quotation + self._separator_after_str
    
    def __len__(self) -> bool:
        """Check that data-string is empty."""
        return len(self._data)

    @property
    def data(self) -> str:
        """Return the data-string."""
        return self._data

    @data.setter
    def data(self, data: str):
        """Set the data-string."""
        self._data = data
    
    @property
    def separator(self) -> str:
        """Return separator after data-string."""
        return self._separator_after_str

    @separator.setter
    def separator(self, sep: str):
        """Set separator after data-string."""
        self._separator_after_str = sep

    @property
    def quotation(self) -> str:
        """Return string quotation."""
        return self._quotation