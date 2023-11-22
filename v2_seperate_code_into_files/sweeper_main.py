from input_util import get_input
from map_util import all_mines_are_flagged, all_tiles_are_masked
from map_util import draw_the_unmasked_map
from map_util import generate_ori_mask_map, generate_ori_mine_state_map
from map_util import generated_masked_map, set_flag, update_mask_map
from print_util import print_all
from config import WIDTH, HEIGHT, ORI_MINE_NUMBER


def main():
    ori_mine_state_map = generate_ori_mine_state_map(
        WIDTH, HEIGHT, ORI_MINE_NUMBER)
    displayed_map = draw_the_unmasked_map(ori_mine_state_map)
    mask_map = generate_ori_mask_map(WIDTH, HEIGHT)
    masked_map = generated_masked_map(displayed_map, mask_map)
    flags_left = ORI_MINE_NUMBER
    print_all(WIDTH, HEIGHT, masked_map, ORI_MINE_NUMBER, flags_left)
    execute_game_loop(ori_mine_state_map, displayed_map, mask_map, flags_left)


def execute_game_loop(ori_mine_state_map, displayed_map, mask_map, flags_left):
    while True:
        x, y, flag_a_tile = get_input()
        if flag_a_tile:
            set_flag(mask_map, x, y)
            flags_left -= 1
        elif ori_mine_state_map[x][y] == 1:
            print("You lose!")
            break
        else:
            update_mask_map(mask_map, x, y, displayed_map)
        if all_mines_are_flagged(mask_map, ori_mine_state_map):
            print("You win!")
            break
        elif all_tiles_are_masked(mask_map):
            print("You lose!")
            break
        else:
            masked_map = generated_masked_map(displayed_map, mask_map)
            print_all(WIDTH, HEIGHT, masked_map, ORI_MINE_NUMBER, flags_left)


if __name__ == '__main__':
    main()
