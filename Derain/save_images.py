import numpy as np
from SSIM_PIL import compare_ssim
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

n = 52
out_filename = '../PReNet-master/datasets'
in_filename = './facades/test_nature/'
filetype = '.jpg'

datafile = './result_all/test12_data/noise_metric_output.txt'
f = open(datafile,'w')

for i in range(n):
    print(i)

    x_true = Image.open(in_filename + str(i+1) + filetype)
    x_true = x_true.resize((1024,512))
    x_true.save('./facades/test_nature2/'+ str(i+1) + filetype)
    #x_true = x_true.resize((512,512))

    #Potentially convert to np.array
    if i == 0:
        plt.imshow(x_true)
        plt.show()



