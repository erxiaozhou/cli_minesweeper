from config import HEIGHT, WIDTH


def get_input():
    prompt = 'lease input the coordinate (e.g., 0 0 / 1 3):, Input F to flag the coordinate (e.g., 0 0 F / 1 3 F)'
    inputs = input(prompt).split()
    if not is_valid_input(inputs):
        print("Invalid input! Please input again!")
        return get_input()
    else:
        x, y = int(inputs[0]), int(inputs[1])
        flag_a_tile = len(inputs) == 3
        return x, y, flag_a_tile


def is_valid_input(inputs):
    is_valid = True
    if inputs[0] not in [str(_) for _ in range(HEIGHT)]:
        is_valid = False
    if inputs[1] not in [str(_) for _ in range(WIDTH)]:
        is_valid = False
    if len(inputs) == 3:
        if inputs[2] != 'F':
            is_valid = False
    return is_valid
