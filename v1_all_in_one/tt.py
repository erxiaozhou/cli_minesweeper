def print_all(width, height, to_display_map, mines_num, flags_left):
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


width = 5
height = 5
to_display_map = [[' '] * width] * height
mines_num = 5
flags_left = 5

print_all(width, height, to_display_map, mines_num, flags_left)
