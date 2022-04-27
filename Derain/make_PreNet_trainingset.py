import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

def get_output(index,i):
    try:
        x = Image.open('../PReNet-master/datasets/train/Rain12600/rainy_image/' + str(index+1) + '.jpg')  # f'{i+1:03d}'+'.png')
        x_clear = Image.open('../PReNet-master/datasets/train/Rain12600/ground_truth/' + str(index+1)+'_'+str(i) + '.png')  # f'{i+1:03d}'+'.png')
    except(FileExistsError):
        return get_output(index + 1,i)
    except(FileNotFoundError):
        return get_output(index + 1,i)
    return x,x_clear,index

index = 0
img = 1
for i in range(900):
    #for j in range(14):
        print([index, img])
        j = random.randint(1,14)
        #x, x_clear, img = get_output(img,j)
        x = Image.open('../PReNet-master/datasets/train/Rain12600/rainy_image/' + str(i+1)+ '_' + str(j) + '.jpg')  # f'{i+1:03d}'+'.png')
        x_clear = Image.open('../PReNet-master/datasets/train/Rain12600/ground_truth/' + str(i+1)  + '.jpg')
        img += 1
        # plt.imshow(x)
        # plt.show()

        y = x.resize((512, 512))
        y_clear = x_clear.resize((512, 512))

        new_image = Image.new('RGB', (2 * y.size[0], y.size[1]), (250, 250, 250))
        new_image.paste(y, (0, 0))
        new_image.paste(y_clear, (y.size[0], 0))

        # plt.imshow(new_image)
        # plt.show()
        new_image.save('./facades/PReNet-training/Rain_Medium/' + str(index) + '.jpg')
        index += 1
