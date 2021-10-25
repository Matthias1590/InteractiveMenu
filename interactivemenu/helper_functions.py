import os


class Keys:
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"
    ENTER = "enter"


if os.name == "nt":
    from msvcrt import getch

    def clear() -> None:
        os.system("cls")

    def getkey() -> Keys:
        key = getch()
        if key in [b"\x00", b"\xe0"]:
            return {
                "H": Keys.UP,
                "M": Keys.RIGHT,
                "P": Keys.DOWN,
                "K": Keys.LEFT,
            }[getch().decode()]
        return {
            "\r": Keys.ENTER,
        }.get(key.decode(), key.decode())
else:
    import keyboard

    def clear() -> None:
        os.system("clear")

    def getkey() -> Keys:
        return keyboard.read_key() # TODO: Test this function
