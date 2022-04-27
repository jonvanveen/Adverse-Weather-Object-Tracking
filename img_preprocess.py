from PIL import Image
import os
import os.path
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', required=False,
  default='data',  help='')
parser.add_argument('--outDir', required=False,
  default='processed',  help='')
opt = parser.parse_args()

IMG_EXTENSIONS = [
  '.jpg', '.JPG', '.jpeg', '.JPEG',
  '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP', '',
]

def is_image_file(filename):
  return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

dir = opt.inDir
outDir = opt.outDir
if not os.path.isdir(dir):
    raise Exception('Check dataroot')
for root, _, fnames in sorted(os.walk(dir)):
    for fname in fnames:
        if is_image_file(fname):
            path = os.path.join(dir, fname)

            #load image
            img = Image.open(path).convert('RGB')

            new_image = Image.new('RGB', (2 * img.size[0], img.size[1]), (250, 250, 250))
            new_image.paste(img, (0, 0))
            new_image.paste(img, (img.size[0], 0))

            if not os.path.exists(outDir):
                os.makedirs(outDir)

            outfile = os.path.join(outDir, fname)
            new_image.save(outfile)