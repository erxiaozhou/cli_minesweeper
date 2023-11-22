import random
import os


# Constant variables
WIDTH = 5
HEIGHT = 3
MINE_ICON = '*'
UNKNOWN_ICON = ' '
ORI_MINE_NUMBER = int(WIDTH * HEIGHT * 0.2)
FLAG = 'F'


def main():
    ori_mine_state_board = generate_ori_mine_state_board(
        WIDTH, HEIGHT, ORI_MINE_NUMBER)
    unmasked_board = get_the_unmasked_board(ori_mine_state_board)
    mask_board = generate_ori_mask_board(WIDTH, HEIGHT)
    masked_board = generate_masked_board(unmasked_board, mask_board)
    flags_left = ORI_MINE_NUMBER
    print_all(WIDTH, HEIGHT, masked_board, ORI_MINE_NUMBER, flags_left)
    while True:
        x, y, flag_a_tile = get_input()
        if flag_a_tile:
            set_flag(mask_board, x, y)
            flags_left -= 1
        elif ori_mine_state_board[y][x] == 1:
            print("You lose!")
            break
        else:
            update_mask_board(mask_board, x, y, unmasked_board)
        if all_mines_are_flagged(mask_board, ori_mine_state_board):
            print("You win!")
            break
        elif all_tiles_are_covered(mask_board):
            print("You lose!")
            break
        else:
            masked_board = generate_masked_board(unmasked_board, mask_board)
            print_all(WIDTH, HEIGHT, masked_board, ORI_MINE_NUMBER, flags_left)


def print_all(width, height, to_display_board, mines_num, flags_left):
    # print the  board and the text info
    # os.system('cls' )
    background_str = generate_background_str(width, height, to_display_board)
    info_text = generate_info_text(mines_num, flags_left)
    ui = f'{info_text}\n{background_str}'
    print(ui)


def generate_a_bar_str(width):
    return '--'*width


def generate_a_line_content(content_line):
    content_line = [''] + content_line + ['']
    return '|'.join(content_line)


def generate_background_str(width, height, unmasked_board):
    # generate the string ploting the board
    background_lines = []
    for y in range(height):
        background_lines.append(generate_a_bar_str(width))
        background_lines.append(generate_a_line_content(unmasked_board[y]))
    background_lines.append(generate_a_bar_str(width))
    background_str = '\n'.join(background_lines)
    return background_str


def generate_info_text(mines_num, flags_left):
    # generate the text message
    return "Mine Number: {}\nFlags Left: {}".format(mines_num, flags_left)


def generate_ori_mine_state_board(width, height, ori_mine_number):
    # determine where are the mines
    mines = [1 for i in range(ori_mine_number)]
    blanks = [0 for i in range(width * height - ori_mine_number)]
    all_elements = mines + blanks
    random.shuffle(all_elements)
    ori_mine_board = [
        all_elements[i * width: (i+1)*width] for i in range(height)]
    return ori_mine_board


def detect_mine_number(mine_state_board, x, y):
    # determine the number of mines around a tile
    if mine_state_board[y][x] == 1:
        return MINE_ICON
    else:
        mine_number = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i < 0 or i >= WIDTH or j < 0 or j >= HEIGHT:
                    continue
                if mine_state_board[j][i] == 1:
                    mine_number += 1
        return str(mine_number)


def get_the_unmasked_board(mine_state_board):
    # initialize the unmasked board
    unmasked_board = [[detect_mine_number(
        mine_state_board, i, j) for i in range(WIDTH)] for j in range(HEIGHT)]
    return unmasked_board


def generate_masked_board(unmasked_board, mask_board):
    # geneate the board to display
    masked_board = [[_determine_one_masked_tile(i, j, mask_board, unmasked_board) for i in range(WIDTH)] for j in range(HEIGHT)]
    return masked_board


def _determine_one_masked_tile(x, y, mask_board, unmasked_board):
    # determine how to desplay a tile
    if not mask_board[y][x]:
        return UNKNOWN_ICON
    elif mask_board[y][x] == FLAG:
        return FLAG
    else:
        return unmasked_board[y][x]


def generate_ori_mask_board(WIDTH, HEIGHT):
    # initialize the mask board
    return [[False for i in range(WIDTH)] for j in range(HEIGHT)]


def all_mines_are_flagged(mask_board, ori_mine_state_board):
    # whether all mines are flagged
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if ori_mine_state_board[y][x] == 1 and mask_board[y][x] != FLAG:
                return False
    return True


def all_tiles_are_covered(mask_board):
    # whether all tiles are covered
    return all(all(mask_board[x]) for x in range(HEIGHT))


def update_mask_board(mask_board, x, y, unmasked_board):
    if not mask_board[y][x]:
        mask_board[y][x] = not mask_board[y][x]
        if unmasked_board[y][x] == '0':
            if x > 0:
                update_mask_board(mask_board, x-1, y, unmasked_board)
            if x < WIDTH-1:
                update_mask_board(mask_board, x+1, y, unmasked_board)
            if y > 0:
                update_mask_board(mask_board, x, y-1, unmasked_board)
            if y < HEIGHT-1:
                update_mask_board(mask_board, x, y+1, unmasked_board)


def set_flag(mask_board, x, y):
    mask_board[y][x] = FLAG


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
