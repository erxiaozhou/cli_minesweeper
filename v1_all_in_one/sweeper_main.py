import random
import os


WIDTH = 5
HEIGHT = 3
MINE_ICON = '*'
UNKNOWN_ICON = ' '
ORI_MINE_NUMBER = int(WIDTH * HEIGHT * 0.2)
FLAG = 'F'


def main():
    ori_mine_state_map = generate_ori_mine_state_map(
        WIDTH, HEIGHT, ORI_MINE_NUMBER)
    unmasked_map = draw_the_unmasked_map(ori_mine_state_map)
    mask_map = generate_ori_mask_map(WIDTH, HEIGHT)
    masked_map = generated_masked_map(unmasked_map, mask_map)
    flags_left = ORI_MINE_NUMBER
    print_all(WIDTH, HEIGHT, masked_map, ORI_MINE_NUMBER, flags_left)
    while True:
        x, y, flag_a_tile = get_input()
        if flag_a_tile:
            set_flag(mask_map, x, y)
            flags_left -= 1
        elif ori_mine_state_map[y][x] == 1:
            print("You lose!")
            break
        else:
            update_mask_map(mask_map, x, y, unmasked_map)
        if all_mines_are_flagged(mask_map, ori_mine_state_map):
            print("You win!")
            break
        elif all_tiles_are_masked(mask_map):
            print("You lose!")
            break
        else:
            masked_map = generated_masked_map(unmasked_map, mask_map)
            print_all(WIDTH, HEIGHT, masked_map, ORI_MINE_NUMBER, flags_left)


def print_all(width, height, to_display_map, mines_num, flags_left):
    # os.system('cls' )
    background_str = generate_background_str(width, height, to_display_map)
    info_text = generate_info_text(mines_num, flags_left)
    ui = f'{info_text}\n{background_str}'
    print(ui)


def generate_a_bar_str(width):
    return '--'*width


def generate_a_line_content(content_line):
    content_line = [''] + content_line + ['']
    return '|'.join(content_line)


def generate_background_str(width, height, unmasked_map):
    background_lines = []
    for y in range(height):
        background_lines.append(generate_a_bar_str(width))
        background_lines.append(generate_a_line_content(unmasked_map[y]))
    background_lines.append(generate_a_bar_str(width))
    background_str = '\n'.join(background_lines)
    return background_str


def generate_info_text(mines_num, flags_left):
    return "Mine Number: {}\nFlags Left: {}".format(mines_num, flags_left)


def generate_ori_mine_state_map(width, height, ori_mine_number):
    mines = [1 for i in range(ori_mine_number)]
    blanks = [0 for i in range(width * height - ori_mine_number)]
    all_elements = mines + blanks
    random.shuffle(all_elements)
    ori_mine_map = [
        all_elements[i * width: (i+1)*width] for i in range(height)]
    return ori_mine_map


def detect_mine_number(mine_state_map, x, y):
    if mine_state_map[y][x] == 1:
        return MINE_ICON
    else:
        mine_number = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i < 0 or i >= WIDTH or j < 0 or j >= HEIGHT:
                    continue
                if mine_state_map[j][i] == 1:
                    mine_number += 1
        return str(mine_number)


def draw_the_unmasked_map(mine_state_map):
    unmasked_map = [[detect_mine_number(
        mine_state_map, i, j) for i in range(WIDTH)] for j in range(HEIGHT)]
    return unmasked_map


def generated_masked_map(unmasked_map, mask_map):
    masked_map = [[_determine_one_masked_tile(i, j, mask_map, unmasked_map) for i in range(WIDTH)] for j in range(HEIGHT)]
    return masked_map


def _determine_one_masked_tile(x, y, mask_map, unmasked_map):
    if not mask_map[y][x]:
        return UNKNOWN_ICON
    elif mask_map[y][x] == FLAG:
        return FLAG
    else:
        return unmasked_map[y][x]


def generate_ori_mask_map(WIDTH, HEIGHT):
    return [[False for i in range(WIDTH)] for j in range(HEIGHT)]


def all_mines_are_flagged(mask_map, ori_mine_state_map):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if ori_mine_state_map[y][x] == 1 and mask_map[y][x] != FLAG:
                return False
    return True


def all_tiles_are_masked(mask_map):
    return all(all(mask_map[x]) for x in range(HEIGHT))


def update_mask_map(mask_map, x, y, unmasked_map):
    if not mask_map[y][x]:
        mask_map[y][x] = not mask_map[y][x]
        if unmasked_map[y][x] == '0':
            if x > 0:
                update_mask_map(mask_map, x-1, y, unmasked_map)
            if x < WIDTH-1:
                update_mask_map(mask_map, x+1, y, unmasked_map)
            if y > 0:
                update_mask_map(mask_map, x, y-1, unmasked_map)
            if y < HEIGHT-1:
                update_mask_map(mask_map, x, y+1, unmasked_map)


def set_flag(mask_map, x, y):
    mask_map[y][x] = FLAG


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
    if inputs[0] not in [str(_) for _ in range(WIDTH)] or inputs[1] not in [str(_) for _ in range(HEIGHT)]:
        is_valid = False
    if len(inputs) == 3:
        if inputs[2] != 'F':
            is_valid = False
    return is_valid


if __name__ == '__main__':
    main()
