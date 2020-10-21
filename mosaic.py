from PIL import Image

import io
import urllib.request

img_url = "https://mosaically.com/~/t/m/2020/10/20/f8323251-0595-4a92-b7de-fcaf12cfc96d/1/dz/output_files/"
num_vertical = 12
num_horizontal = 6
# 12: 0-2
# 13: 3-5
#
# (0-5, mod 3 + 12 = folder for output file)


fd = urllib.request.urlopen(img_url + "13/0_0.jpg")
image_file = io.BytesIO(fd.read())
im = Image.open(image_file)
orig_height = im.height
orig_width = im.width
print(orig_height, orig_width)
dst = Image.new('RGB', (orig_width * num_horizontal, orig_height * num_vertical))

for i in range(num_horizontal):
    folder = 13
    for j in range(num_vertical):
        the_url = img_url + "%d/%d_%d.jpg" % (folder, i, j)
        print(the_url)
        fd = urllib.request.urlopen(the_url)
        image_file = io.BytesIO(fd.read())
        im = Image.open(image_file)
        dst.paste(im, (orig_width * i, orig_height * j))
dst.save('pillow_concat_h.jpg')