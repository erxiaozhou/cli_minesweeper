from config import HEIGHT, WIDTH


class UserInput:
    def __init__(self, x, y, flag_a_tile):
        self.x = x
        self.y = y
        self.flag_a_tile = flag_a_tile

    @classmethod
    def get_input_from_cli(cls):
        prompt = 'Please input the coordinate (e.g., 0 0 / 1 3):, Input F to flag the coordinate (e.g., 0 0 F / 1 3 F)'
        inputs = input(prompt).split()
        if not _is_valid_input(inputs):
            print("Invalid input! Please input again!")
            return cls.get_input_from_cli()
        else:
            x, y = int(inputs[0]), int(inputs[1])
            flag_a_tile = len(inputs) == 3
            return cls(x, y, flag_a_tile)


def _is_valid_input(inputs):
    is_valid = True
    if inputs[0] not in [str(_) for _ in range(WIDTH)]:
        is_valid = False
    if inputs[1] not in [str(_) for _ in range(HEIGHT)]:
        is_valid = False
    if len(inputs) == 3:
        if inputs[2] != 'F':
            is_valid = False
    return is_valid
