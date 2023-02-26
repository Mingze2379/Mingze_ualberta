import numpy as np
import matplotlib.pyplot as plt
import random
import math
from os import listdir
from PIL import Image

P_ba = 0.3 # b
P_ca = 0.2 # r
P_aa = 0.5 # 1-b-r

P_cb = 0 #
P_ab = 0.3 # b
P_bb = 0.7 # 1-b

P_bc = 0
P_ac = 0.2 # r
P_cc = 0.8 # 1-r
# Suppose r = 0.2, b = 0.3

def get_next_state(cur_s):
    if cur_s == 'a':
        if random.uniform(0, 1) > (P_ca + P_ba):# > r + b = 0.5
            return 'a'
        elif random.uniform(0, 1) < P_ca: # < r = 0.2
            return 'c'
        else:
            return 'b'

    elif cur_s == 'b':
        if random.uniform(0, 1) > P_ab: # > b = 0.3
            return 'b'
        else:
            return 'a'

    elif cur_s == 'c':
        if random.uniform(0, 1) > P_ac: # < r = 0.2
            return 'c'
        else:
            return 'a'
def r_loops():
    sequence = []
    start = random.randint(1, 3)
    if start == 1:
        sequence.append('a')
    elif start == 2:
        sequence.append('b')
    else:
        sequence.append('c')
    for i in range(50):
        next_state = get_next_state(sequence[i])
        sequence.append(next_state)
    return sequence
def main():
    im_list = []
    sequence = r_loops()
    for i in sequence:
        if i == 'a':
            im_list.append(Image.open('a.jpg'))
        elif i == 'b':
            im_list.append(Image.open('b.jpg'))
        else:
            im_list.append(Image.open('c.jpg'))
    ims = []
    for i in im_list:
        new_img = i.resize((130, 171), Image.BILINEAR)
        ims.append(new_img)
    width, height = ims[0].size
    result = Image.new(ims[0].mode, (width * len(ims), height))

    for i, im in enumerate(ims):
        result.paste(im, box=(i * width, 0))
    rgb_im = result.convert('RGB')
    rgb_im.save("result.jpg")

#     lists = d.items()
#     x, y = zip(*lists) # unpack a list of pairs into two tuples
#     plt.plot(x, y)
#     plt.title(label = '% R-loops over Probability p4')
#     plt.xlabel(xlabel = 'Probability of p4')
#     plt.ylabel(ylabel = '% R-loops')
#     plt.show()

if __name__ == "__main__":
    main()
