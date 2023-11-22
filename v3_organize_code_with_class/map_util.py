import random
from print_util import generate_background_str


class Map:
    def __init__(self, width, height, unknown_icon, flag, mine_icon, ori_mine_number) -> None:
        self.width = width
        self.height = height
        self.unknown_icon = unknown_icon
        self.flag = flag
        self.mine_icon = mine_icon
        self.ori_mine_number = ori_mine_number
        self._init_ori_mine_state_map(self.ori_mine_number)
        self._init_unmasked_map()
        self._init_mask_map()

    def __str__(self) -> str:
        return generate_background_str(self.width, self.height, self.masked_map)

    @classmethod
    def from_config(cls, config):
        return cls(config.width, config.height, config.unknown_icon, config.flag, config.mine_icon, config.ori_mine_number)

    @property
    def masked_map(self):
        masked_map = [[self.unmasked_map[y][x] if self.mask_map[y][x]
                       else self.unknown_icon for x in range(self.width)] for y in range(self.height)]
        return masked_map

    @property
    def all_tiles_are_masked(self):
        return all(all(self.mask_map[y]) for y in range(self.height))

    @property
    def all_mines_are_flagged(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.mine_state_map[y][x] == 1 and self.mask_map[y][x] != self.flag:
                    return False
        return True

    def update_mask_map(self, user_input):
        x, y = user_input.x, user_input.y
        if user_input.flag_a_tile:
            self.mask_map[y][x] = self.flag
        else:
            self._update_mask_map_by_explore(x, y)

    def _init_ori_mine_state_map(self, ori_mine_number):
        mines = [1 for i in range(ori_mine_number)]
        blanks = [0 for i in range(self.width * self.height - ori_mine_number)]
        all_elements = mines + blanks
        random.shuffle(all_elements)
        ori_mine_map = [
            all_elements[i * self.width: (i+1)*self.width] for i in range(self.height)]
        self.mine_state_map = ori_mine_map

    def _init_unmasked_map(self):
        self.unmasked_map = [[_determine_unmasked_map_element(
            self.mine_state_map, x, y, self.width, self.height, self.mine_icon) for x in range(self.width)] for y in range(self.height)]

    def _init_mask_map(self):
        self.mask_map = [[False for x in range(
            self.width)] for y in range(self.height)]

    def _update_mask_map_by_explore(self, x, y):
        _update_mask_map_by_explore(x, y, self.mask_map, self.unmasked_map)


def _update_mask_map_by_explore(x, y, mask_map, unmasked_map):
    if not mask_map[y][x]:
        mask_map[y][x] = not mask_map[y][x]
        if unmasked_map[y][x] == '0':
            if x > 0:
                _update_mask_map_by_explore(x-1, y, mask_map, unmasked_map)
            if x < len(mask_map[0])-1:
                _update_mask_map_by_explore(x+1, y, mask_map, unmasked_map)
            if y > 0:
                _update_mask_map_by_explore(x, y-1, mask_map, unmasked_map)
            if y < len(mask_map)-1:
                _update_mask_map_by_explore(x, y+1, mask_map, unmasked_map)


def _determine_unmasked_map_element(mine_state_map, x, y, width, height, mine_icon):
    if mine_state_map[y][x] == 1:
        return mine_icon
    else:
        mine_number = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i < 0 or i >= width or j < 0 or j >= height:
                    continue
                if mine_state_map[j][i] == 1:
                    mine_number += 1
        return str(mine_number)
