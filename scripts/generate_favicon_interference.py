#!/usr/bin/env python3
"""
Favicon.ico Generator
Created by Claude AI.

Generate a favicon for "Rich's Corner" using the Platonic Interference concept:
Three overlapping rotated ellipses representing the convergence of engineering,
business operations, and artificial intelligence. Each ellipse is colored and
semi-transparent, creating constructive interference zones where they overlap.
"""

from PIL import Image, ImageDraw
import math
import numpy as np

# Image settings (256x256 is standard for favicon)
width, height = 256, 256
center = (width // 2, height // 2)

# Create image with transparent background
img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Color scheme: Navy + Teal + Amber
# Layered back-to-front with opacity gradient to evoke 3D projection
# Back layer faded, front layer bold — like depth of field
ellipse_specs = [
    {'outline': (210, 110, 0, 230),  'fill': (210, 110, 0, 90),  'angle': 130, 'width': 4},  # Amber — back
    {'outline': (0, 140, 130, 120),  'fill': (0, 140, 130, 38),  'angle': 70,  'width': 6},  # Teal — middle
    {'outline': (0, 33, 106, 255),   'fill': (0, 33, 106, 110),  'angle': 10, 'width': 8},  # Navy — front
]

# Ellipse parameters
major_radius = 90
minor_radius = 36

# White circular background card
bg_radius = 102
bg_bbox = [
    center[0] - bg_radius, center[1] - bg_radius,
    center[0] + bg_radius, center[1] + bg_radius
]
draw.ellipse(bg_bbox, fill=(255, 255, 255, 255))

def ellipse_points(cx, cy, rx, ry, angle_deg, steps=180):
    """Generate polygon points for a rotated ellipse."""
    a = math.radians(angle_deg)
    pts = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        # Parametric ellipse equation
        x = rx * math.cos(t)
        y = ry * math.sin(t)
        # Rotate by angle_deg and translate to center
        rotated_x = cx + x * math.cos(a) - y * math.sin(a)
        rotated_y = cy + x * math.sin(a) + y * math.cos(a)
        pts.append((rotated_x, rotated_y))
    return pts

# === PRECOMPUTE LIGHTING GRADIENT ===
# Increased contrast and steeper gradient for more obvious effect
light_angle_rad = math.radians(-45)
light_dir_x = math.cos(light_angle_rad)
light_dir_y = math.sin(light_angle_rad)
ambient = 0.25
diffuse_strength = 0.75

y_coords, x_coords = np.mgrid[0:height, 0:width]
projection = (x_coords - center[0]) * light_dir_x + (y_coords - center[1]) * light_dir_y

# Gradient parameters: width (transition zone size) and offset (shift toward light)
# Constraint: offset + width = bg_radius ensures top-right of card is at full brightness
gradient_width = bg_radius * 0.8    # transition window ~82px
gradient_offset = bg_radius * 0.2   # offset toward upper-right, saturation at card edge
projection = np.clip((projection - gradient_offset) / gradient_width, -1, 1)
lighting = ambient + diffuse_strength * (projection + 1) / 2

def apply_lighting(layer):
    """Apply precomputed lighting gradient to an RGBA layer."""
    arr = np.array(layer).astype(np.float64)
    mask = arr[:, :, 3] > 0
    for c in range(3):
        arr[:, :, c] = np.where(mask, np.clip(arr[:, :, c] * lighting, 0, 255), arr[:, :, c])
    return Image.fromarray(arr.astype(np.uint8), 'RGBA')

# Draw white card with lighting
card_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
ImageDraw.Draw(card_layer).ellipse(bg_bbox, fill=(255, 255, 255, 255))
img = Image.alpha_composite(img, apply_lighting(card_layer))

# Draw three overlapping rotated ellipses (back to front)
for spec in ellipse_specs:
    angle = spec['angle']
    pts = ellipse_points(center[0], center[1], major_radius, minor_radius, angle)

    # Draw filled ellipse on isolated layer, apply lighting, composite
    fill_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(fill_layer).polygon(pts, fill=spec['fill'])
    img = Image.alpha_composite(img, apply_lighting(fill_layer))

    # Draw outline directly on img (unlit, stays crisp)
    ImageDraw.Draw(img).line(pts + [pts[0]], fill=spec['outline'], width=spec['width'])

# Draw small white circle at center (specular highlight / vanishing point) — unlit
# center_r = 12
# ImageDraw.Draw(img).ellipse(
#     [center[0] - center_r, center[1] - center_r, center[0] + center_r, center[1] + center_r],
#     fill=(255, 255, 255, 255)
# )

# Save the image
img.save('favicon.png')
img.save('favicon.ico', format='ICO', sizes=[(256,256),(64,64),(32,32),(16,16)])

print("✓ Generated favicon.png (256x256 pixels)")
print("✓ Generated favicon.ico (with full alpha transparency)")
print("\nDesign: Platonic Interference")
print("Three overlapping ellipses (Navy, Teal, Amber) representing the convergence of")
print("engineering, business operations, and artificial intelligence.")
