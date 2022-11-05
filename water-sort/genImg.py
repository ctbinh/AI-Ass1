import numpy as np
from PIL import Image

RED = (255, 0, 0)
GREEN = (39, 164, 24)
BLUE = (24, 72, 232)
YELLOW = (232, 231, 24)
PINK = (232, 24, 219)
BROWN = (114, 80, 70)
ORANGE = (218, 109, 7)
COLOR1 = (21, 90, 42)
COLOR2 = (86, 236, 188)
COLOR3 = (86, 210, 236)
COLOR4 = (104, 86, 236)
COLOR5 = (187, 9, 124)
COLOR6 = (157, 244, 24)
COLOR7 = (0, 0, 0)
NOCOLOR = (247, 247, 247)
COLORS = [NOCOLOR, RED, GREEN, BLUE, YELLOW, PINK, BROWN, ORANGE,
          COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, RED, GREEN, BLUE, YELLOW, PINK, BROWN, ORANGE,
          COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, RED, GREEN, BLUE, YELLOW, PINK, BROWN, ORANGE,
          COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7]


def getImgName():
    print('2'*5)


def createImg(step, tube_size, step_idx, total_img):
    width, height = 1500, 500
    # create blank image
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # draw background
    img[:] = (173, 173, 173)
    for color in range(tube_size):
        for tube_idx in range(len(step)):
            if(color >= len(step[tube_idx].items)):
                window_colour = COLORS[0]
            else:
                window_colour = COLORS[step[tube_idx].items[color]]
            # draw windows
            img[
                int(height*0.01 + 42*(tube_size - color)):int(height*0.01 + 42*(tube_size - color) + 40),
                int(width*0.01 + 65*tube_idx): int(width*0.01 + 65*tube_idx + 50)
            ] = window_colour
    idx = str(step_idx) if len(str(step_idx)) == len(str(total_img)
                                                     ) else '0'*(len(str(total_img))-len(str(step_idx))) + str(step_idx)
    Image.fromarray(img).save("./images/" + idx + '.png')
