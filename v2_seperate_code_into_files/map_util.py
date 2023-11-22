from config import WIDTH, HEIGHT, UNKNOWN_ICON, FLAG, MMINE_ICON
import random


def generate_ori_mine_state_map(width, height, ori_mine_number):
    mines = [1 for i in range(ori_mine_number)]
    blanks = [0 for i in range(width * height - ori_mine_number)]
    all_elements = mines + blanks
    random.shuffle(all_elements)
    ori_mine_map = [
        all_elements[i * width: (i+1)*width] for i in range(height)]
    return ori_mine_map


def detect_mine_number(mine_state_map, x, y):
    if mine_state_map[x][y] == 1:
        return MMINE_ICON
    else:
        mine_number = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i < 0 or i >= HEIGHT or j < 0 or j >= WIDTH:
                    continue
                if mine_state_map[i][j] == 1:
                    mine_number += 1
        return str(mine_number)


def draw_the_unmasked_map(mine_state_map):
    displayed_map = [[detect_mine_number(
        mine_state_map, x, y) for x in range(WIDTH)] for y in range(HEIGHT)]
    return displayed_map


def generated_masked_map(displayed_map, mask_map):
    masked_map = [[displayed_map[x][y] if mask_map[x][y]
                   else UNKNOWN_ICON for x in range(WIDTH)] for y in range(HEIGHT)]
    return masked_map


def generate_ori_mask_map(WIDTH, HEIGHT):
    return [[False for x in range(WIDTH)] for y in range(HEIGHT)]


def all_mines_are_flagged(mask_map, ori_mine_state_map):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            if ori_mine_state_map[x][y] == 1 and mask_map[x][y] != FLAG:
                return False
    return True


def all_tiles_are_masked(mask_map):
    return all(all(mask_map[x]) for x in range(HEIGHT))


def update_mask_map(mask_map, x, y, displayed_map):
    if not mask_map[x][y]:
        mask_map[x][y] = not mask_map[x][y]
        if displayed_map[x][y] == '0':
            if x > 0:
                update_mask_map(mask_map, x-1, y, displayed_map)
            if x < HEIGHT-1:
                update_mask_map(mask_map, x+1, y, displayed_map)
            if y > 0:
                update_mask_map(mask_map, x, y-1, displayed_map)
            if y < WIDTH-1:
                update_mask_map(mask_map, x, y+1, displayed_map)


def set_flag(mask_map, x, y):
    mask_map[x][y] = FLAG
