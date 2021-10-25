from typing import Optional, Any


class Option:
    def __init__(self, text: str, value: Optional[Any] = None) -> None:
        self.__text = text
        self.__value = value

    @property
    def value(self) -> Optional[Any]:
        return self.__value

    def __repr__(self) -> str:
        return self.__text
