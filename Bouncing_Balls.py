import math

def bouncing_ball(h, bounce, window):
    if window >= h or h <= 0 or not 0 < bounce < 1:
        return -1

    return 1 + int(math.log(window / h, bounce)) * 2




print(bouncing_ball(30, 0.66, 1.5))