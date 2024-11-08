from enum import StrEnum, auto


class Locale(StrEnum):
    """
    Enumeration representing supported locales.
    """

    NP = auto()
    EN = auto()
    UK = auto()
    JA = auto()

    DEFAULT = EN
