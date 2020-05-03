import matplotlib.pyplot as plt
import matplotlib.image as img
import os
from PIL import Image
import time
import subprocess

mypath = "img"

# p = subprocess.Popen("imgs\\transport.png", shell=True)
# name = input("Input:")
# p.kill()


for filename in os.listdir(mypath):
    path = mypath + "\\\\" + filename
    print(path)
    p = subprocess.Popen(path, shell=True)
    name = input("Input:")
    p.kill()
    # im = Image.open(path)
    # plt.imshow(im)
    # plt.show()
    # plt.close()
    # plt.clf() #will make the plot window empty
    # im.close()
