WIDTH = 3
HEIGHT = 3
MINE_ICON = '*'
UNKNOWN_ICON = ' '
ORI_MINE_NUMBER = int(WIDTH * HEIGHT * 0.2)
FLAG = 'F'


class Config:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.ori_mine_number = ORI_MINE_NUMBER
        self.mine_icon = MINE_ICON
        self.unknown_icon = UNKNOWN_ICON
        self.flag = FLAG
