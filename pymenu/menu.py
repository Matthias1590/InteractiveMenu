from typing import Any, List
from .option import Option
from .helper_functions import Keys, clear, getkey
from consoledraw import Console
from termcolor import colored


class Menu:
    def __init__(self, title: str, options: List[Option]) -> None:
        self.title = title
        self.options = options
        self.console = Console()

    def show(self) -> Any:
        index, prevIndex = 0, -1
        while True:
            # Printing the title and options
            if index != prevIndex:
                clear()
                print(self.title)
                for i, option in enumerate(self.options):
                    option = str(option)
                    if i == index:
                        option = "> " + colored(f" {option} ", "red", "on_white", attrs=["dark", "bold"])
                    else:
                        option = "   " + option
                    print(option)
            
            prevIndex = index

            # Handling user input
            key = getkey()
            if key == Keys.ENTER:
                clear()
                return self.options[index].value
            elif key == Keys.UP and index > 0:
                index -= 1
            elif key == Keys.DOWN and index < len(self.options) - 1:
                index += 1
