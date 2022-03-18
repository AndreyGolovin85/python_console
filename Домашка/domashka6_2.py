colors_dict = {
    1: "░", 2: "▒", 3: "▓",
}


def draw_carpet(w: int, h: int):
    """
    Рисуем ковер в псевдографике.
    :param w:
    :param h:
    :return:
    """
    for x in range(h):
        if w < 6 or h < 3:
            print(colors_dict[3] + (colors_dict[1] * (w - 2)) + colors_dict[3])
        else:
            if x == 0:
                print(colors_dict[3] + (colors_dict[1] * (w - 2)) + colors_dict[3])
            elif x == h - 1:
                print(colors_dict[3] + (colors_dict[1] * (w - 2)) + colors_dict[3])
            else:
                print(colors_dict[3] + colors_dict[1] + colors_dict[2] * (w - 4) + colors_dict[1] + colors_dict[3])


draw_carpet(3, 8)
