"""
URL QR Code Generator
https://github.com/lincolnloop/python-qrcode
"""
import argparse
import qrcode
from PIL import Image

# parser = argparse.ArgumentParser(description=__doc__)
# parser.add_argument('-u', '--url', required=True, help='URL text to encode')
# parser.add_argument('-u', '--url', required=True, help='URL text to encode')
# parser.add_argument('-f', '--file', required=True, help='output image file path')
# args = parser.parse_args()

# taking url or text
url = 'https://www.linkedin.com/in/rich-taggart/'
print(f'Generating QR code for URL:\n  "{url}"')


QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
# QRcolor = '#3A60ED'

# adding color to QR code
QRimg = QRcode.make_image(fill_color="black", back_color="white").convert('RGB')

# Apply custom image
img_path = './qr_imgs/linkedin_logo_white.png'
overlay_img = Image.open(img_path)
# overlay_img_background = Image.new(mode=overlay_img.mode, size=(overlay_img.size[0] + 10, overlay_img.size[1] + 10), color='white')
# padding_xy = (
#   (overlay_img_background.size[0] - overlay_img.size[0]) // 2,
#   (overlay_img_background.size[1] - overlay_img.size[1]) // 2,
# )
# overlay_img_padding = Image.new(mode=overlay_img.mode, size=overlay_img.size, color='white')
# overlay_img_background.paste(overlay_img, padding_xy)

# new_width = 150  # px
# width_pct = new_width / float(overlay_img.size[0])
# new_height = int(float(overlay_img.size[1]) * float(width_pct))
# overlay_img = overlay_img.resize((new_width, new_height), Image.ANTIALIAS)

overlay_xy = (
  (QRimg.size[0] - overlay_img.size[0]) // 2,
  (QRimg.size[1] - overlay_img.size[1]) // 2,
)
QRimg.paste(overlay_img, overlay_xy)

# save the QR code generated
file = './qr_imgs/qr_linkedin.png'
QRimg.save(file)

print(f'QR code generated: \n  "{file}"')
