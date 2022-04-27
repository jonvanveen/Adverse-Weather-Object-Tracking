from PIL import Image
import os
import os.path
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', required=False,
  default='data',  help='input directory')
parser.add_argument('--outDir', required=False,
  default='illum',  help='output directory')
parser.add_argument('--lvl', required=False,
  default=20,  help='Noise level/standard deviation')
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

            np_img = np.asarray(img)
            #row,col,ch= np_img.shape
            #gauss = np.array(np_img.shape)
            #gauss = np.random.normal(0, opt.lvl, (row, col, ch))
            #gauss = gauss.reshape(row, col, ch)
            noisy = np.clip(np_img + opt.lvl,0,255)

            new_image = Image.fromarray(noisy.astype('uint8'),"RGB")


            if not os.path.exists(outDir):
                os.makedirs(outDir)

            outfile = os.path.join(outDir, fname)
            new_image.save(outfile)