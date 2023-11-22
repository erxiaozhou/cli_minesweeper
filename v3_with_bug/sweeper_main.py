from input_util import UserInput
from map_util import Map
from print_util import generate_info_text
from config import Config


class Game:
    def __init__(self, config) -> None:
        pass
        self.map = Map.from_config(config)
        self.flags_left = config.ori_mine_number
        self.ori_mine_number = config.ori_mine_number

    def play(self):
        self.display_state()
        while True:
            user_input = UserInput.get_input_from_cli()
            if self.game_failed(user_input):
                print("You lose!")
                break
            self.map.update_mask_map(user_input)
            if user_input.flag_a_tile:
                self.flags_left -= 1
            if self.game_succeed():
                print("You win!")
                break
            elif self.tiles_are_all_masked():
                print("You lose!")
                break
            else:
                self.display_state()

    def display_state(self):
        info_txt = generate_info_text(self.ori_mine_number, self.flags_left)
        ui = f'{info_txt}\n{self.map}'
        print(ui)

    def game_failed(self, user_input):
        return (not user_input.flag_a_tile) and bool(self.map.mine_state_map[user_input.y][user_input.x])

    def game_succeed(self):
        return self.map.all_mines_are_flagged

    def tiles_are_all_masked(self):
        return self.map.all_tiles_are_masked


if __name__ == '__main__':
    Game(Config()).play()
