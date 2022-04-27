from PIL import Image, ImageEnhance
import os
import os.path
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', required=False,
  default='data',  help='input directory')
parser.add_argument('--outDir', required=False,
  default='downsample',  help='output directory')
parser.add_argument('--lvl', required=False,
  default=2,  help='Contrast level')
parser.add_argument('--random', required=False,
  default=False,  help='Random noise level True/False')
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
            small = img.resize((round(img.height/opt.lvl),round(img.width/opt.lvl)),Image.BICUBIC)
            new_image = small.resize(img.size,Image.BICUBIC)


            if not os.path.exists(outDir):
                os.makedirs(outDir)

            outfile = os.path.join(outDir, fname)
            new_image.save(outfile)