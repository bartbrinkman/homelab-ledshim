# import random
# import time

# import ledshim

# ledshim.set_clear_on_exit()
# ledshim.set_brightness(0.4)

# while True:
#     for i in range(ledshim.NUM_PIXELS):
#         ledshim.set_pixel(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#     ledshim.show()
#     time.sleep(0.05)



# try:
#     import numpy as np
# except ImportError:
#     exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

# import time
# import colorsys
# import ledshim

# ledshim.set_clear_on_exit()


# def make_gaussian(fwhm):
#     x = np.arange(0, ledshim.NUM_PIXELS, 1, float)
#     y = x[:, np.newaxis]
#     x0, y0 = 3.5, (ledshim.NUM_PIXELS / 2) - 0.5
#     fwhm = fwhm
#     gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
#     return gauss


# while True:
#     for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
#         fwhm = 15.0 / z
#         gauss = make_gaussian(fwhm)
#         start = time.time()
#         y = 4
#         for x in range(ledshim.NUM_PIXELS):
#             h = 0.5
#             s = 1.0
#             v = gauss[x, y]
#             rgb = colorsys.hsv_to_rgb(h, s, v)
#             r, g, b = [int(255.0 * i) for i in rgb]
#             ledshim.set_pixel(x, r, g, b)
#         ledshim.show()
#         end = time.time()
#         t = end - start
#         if t < 0.04:
#             time.sleep(0.04 - t)



import time
import ledshim

ledshim.set_clear_on_exit()

REDS = [0] * ledshim.NUM_PIXELS * 2
SCAN = [1, 2, 4, 8, 16, 32, 64, 128, 255]
REDS[ledshim.NUM_PIXELS - len(SCAN):ledshim.NUM_PIXELS + len(SCAN)] = SCAN + SCAN[::-1]

start_time = time.time()

while True:
    # Sine wave, spends a little longer at min/max
    # delta = (time.time() - start_time) * 8
    # offset = int(round(((math.sin(delta) + 1) / 2) * (ledshim.NUM_PIXELS - 1)))

    # Triangle wave, a snappy ping-pong effect
    delta = (time.time() - start_time) * ledshim.NUM_PIXELS * 2
    offset = int(abs((delta % len(REDS)) - ledshim.NUM_PIXELS))

    for i in range(ledshim.NUM_PIXELS):
        ledshim.set_pixel(i, REDS[offset + i], 0, 0)

    ledshim.show()

    time.sleep(0.05)