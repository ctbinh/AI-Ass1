import numpy as np
from PIL import Image

RED = (255, 0, 0)
GREEN = (39, 164, 24)
BLUE = (24, 72, 232)
YELLOW = (232, 231, 24)
PINK = (232, 24, 219)
BROWN = (114, 80, 70)
ORANGE = (218, 109, 7)
COLOR1 = (226, 242, 15)
COLOR2 = (86, 236, 188)
COLOR3 = (86, 210, 236)
COLOR4 = (104, 86, 236)
COLOR5 = (187, 9, 124)
COLOR6 = (157, 244, 24)
NOCOLOR = (247, 247, 247)
COLORS = [NOCOLOR ,RED, GREEN, BLUE, YELLOW, PINK, BROWN, ORANGE, COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6]

def createImg(step, tube_size, step_idx):
    width, height = 1500, 500
    # create blank image
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # draw background
    img[:] = (173, 173, 173)
    for color in range(tube_size):
        for tube_idx in range(len(step)):
            # select random window colours
            if(color >= len(step[tube_idx].items)):
                window_colour = COLORS[0]
            else:
                window_colour = COLORS[step[tube_idx].items[color]]
            # draw windows
            img[
                int(height*0.2 + 42*(tube_size - color) + 20):int(height*0.2 + 42*(tube_size - color) + 40 + 20),
                int(width*0.01 + 65*tube_idx): int(width*0.01 + 65*tube_idx + 50)
                ] = window_colour
    idx = str(step_idx) if len(str(step_idx)) == 2 else '0'+ str(step_idx)
    Image.fromarray(img).save("./images/" + idx + '.png')
