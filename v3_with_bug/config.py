WIDTH = 5
HEIGHT = 5
MINE_ICON = '*'
UNKNOWN_ICON = ' '
ORI_MINE_NUMBER = 1
FLAG = 'F'


class Config:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.ori_mine_number = ORI_MINE_NUMBER
        self.mine_icon = MINE_ICON
        self.unknown_icon = UNKNOWN_ICON
        self.flag = FLAG
