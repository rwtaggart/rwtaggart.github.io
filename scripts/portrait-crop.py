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


""" SRC IMAGES """
src_img_path = "./assets/images/bio_portrait.jpeg"
dst_img_path = "bio_portrait.256"

""" Utilities """
center = lambda size, offset=(0,0): (size[0]/2 + offset[0], size[1]/2 + offset[1])

def resize_ratio_w(im:Image, width:int) -> Image:
    # adjust image size and keep aspect ratio
    wpercent = (width/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    return im.resize((width, hsize), Image.LANCZOS)

""" Dimensions """
crop_offset = (0, 15)
size = (256, 256)
# TODO: Make this the size
# size = (1200, 630)

""" Load Src Image """
# src_img_path = "_sandbox/logo-1.orig.jpeg"
s_im = Image.open(src_img_path)
# r_im = s_im.resize(size, Image.LANCZOS)
r_im = resize_ratio_w(s_im, size[0])
c_im = r_im.crop((*crop_offset, size[0] + crop_offset[0], size[1] + crop_offset[1]))
c_im.save(f'_sandbox/{dst_img_path}.png')

""" Create Transparent Mask """
im_mask = Image.new('1', (size[0], size[1]), color=0)
md = ImageDraw.Draw(im_mask)
md.circle(center(size), size[0]//2, fill=1)
im_mask.save(f'_sandbox/{dst_img_path}.mask.png')

im = Image.new('RGBA', (size[0], size[1]), color=(0,0,0,0))
print('sizes: ', im.size, r_im.size, c_im.size, im_mask.size)
im.paste(c_im, mask=im_mask)


""" Save image """
im.save(f'_sandbox/{dst_img_path}.crop.png')
