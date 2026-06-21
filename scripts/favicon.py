#!/usr/bin/env python3
"""
favicon.ico
Generate the favicon.ico file and site logo

Use Pillow.Image to generate the graphic.
https://pillow.readthedocs.io/en/stable/reference
"""

from math import pow, sin, cos, degrees as deg, radians as rad
import math

from PIL import Image, ImageDraw


""" Palette """
dark = "#0e0e0e"
blue = "#0056c7"


""" Utilities """
cir_x = lambda r, angle=0, rot=0: r*cos(rad(angle + rot))
cir_y = lambda r, angle=0, rot=0: r*sin(rad(angle + rot))
shift = lambda c, r, angle=0, rot=0: (c[0] + cir_x(r, angle, rot), c[1] + cir_y(r, angle, rot))
c_pad = lambda c, pad=0: (c[0] - pad, c[1] - pad, c[0] + pad, c[1] + pad)
n_deg = lambda n: 360/n

center = lambda size, offset=(0,0): (size[0]/2 + offset[0], size[1]/2 + offset[1])



""" Dimensions """
size = (256, 256)


""" Generate Image """
im = Image.new('RGBA', (size[0], size[1]), color=(0,0,0,0))
cx, cy = c = center(size)

draw = ImageDraw.Draw(im)

# BACKGROUND
draw.circle(c, size[0]//2, fill=dark, outline=blue, width=10)

# MID-LAYER
# draw.circle(c, size[0]//3, fill=None, outline="white", width=5)

# FOREGROUND
draw.circle(shift(c, r=size[0]//3, angle= -60), 15, fill=blue)
draw.circle(shift(c, r=size[0]//3, angle=  45), 15, fill=blue)
draw.circle(shift(c, r=size[0]//3, angle=-160), 15, fill=blue)

draw.circle(c, 20, fill="white")


""" Save image """
im.save('_sandbox/logo.png')
im.save('_sandbox/favicon.png')
im.save('_sandbox/favicon.ico', format='ICO', sizes=[(256,256),(64,64),(32,32),(16,16)])
