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
