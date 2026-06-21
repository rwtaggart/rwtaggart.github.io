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
# b_size = (int(256 * 1.3), int(256 * 1.3))

""" Load Src Image """
# src_img_path = "_sandbox/logo-1.orig.jpeg"
src_img_path = "_sandbox/IMG_6988.jpg"
s_im = Image.open(src_img_path)
r_im = s_im.resize(size, Image.LANCZOS)
r_im.save('_sandbox/logo-1.256.png')

""" Create Transparent Mask """
im_mask = Image.new('1', (size[0], size[1]), color=0)
md = ImageDraw.Draw(im_mask)
md.circle(center(size), size[0]//2 - 7, fill=1)
im_mask.save('_sandbox/logo-mask.png')

im = Image.new('RGBA', (size[0], size[1]), color=(0,0,0,0))
print('sizes: ', im.size, r_im.size, im_mask.size)
im.paste(r_im, mask=im_mask)

# """ Generate Image """
# im = Image.new('RGBA', (size[0], size[1]), color=(0,0,0,0))
# cx, cy = c = center(size)

# draw = ImageDraw.Draw(im)

# # BACKGROUND
# draw.circle(c, size[0]//2, fill=dark, outline=blue, width=10)

# # MID-LAYER
# # draw.circle(c, size[0]//3, fill=None, outline="white", width=5)

# # FOREGROUND
# draw.circle(shift(c, r=size[0]//3, angle= -60), 15, fill=blue)
# draw.circle(shift(c, r=size[0]//3, angle=  45), 15, fill=blue)
# draw.circle(shift(c, r=size[0]//3, angle=-160), 15, fill=blue)

# draw.circle(c, 20, fill="white")


""" Save image """
im.save('_sandbox/logo-2.png')
im.save('_sandbox/favicon-2.png')
im.save('_sandbox/favicon-2.ico', format='ICO', sizes=[(256,256),(64,64),(32,32),(16,16)])
