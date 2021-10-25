# PyMenu
An easy-to-use python package to create interactive menus in the terminal.

# Installation
This package is pip installable.
```
pip install interactivemenu
```

# Demo
```python
from interactivemenu import Menu, Option

menu = Menu(
    "Are you sure you want to quit?",
    [
        Option("Yes", True),
        Option("No", False)
    ]
)

if menu.show():
    exit()
else:
    ... # Do stuff
```
