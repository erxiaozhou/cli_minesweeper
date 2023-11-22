def print_all(width, height, displayed_map, mines_num, flags_left):
    background_str = generate_background_str(width, height, displayed_map)
    info_text = generate_info_text(mines_num, flags_left)
    ui = f'{info_text}\n{background_str}'
    print(ui)


def generate_a_bar_str(width):
    return '--'*width


def generate_a_line_content(content_line):
    content_line = [''] + content_line + ['']
    return '|'.join(content_line)


def generate_background_str(width, height, displayed_map):
    background_lines = []
    for y in range(height):
        background_lines.append(generate_a_bar_str(width))
        background_lines.append(generate_a_line_content(displayed_map[y]))
    background_lines.append(generate_a_bar_str(width))
    background_str = '\n'.join(background_lines)
    return background_str


def generate_info_text(mines_num, flags_left):
    return "Mines Number: {}\n Flags Left: {}".format(mines_num, flags_left)
