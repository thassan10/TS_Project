from PIL import Image

# Testing - can open preset images
img = Image.open("geek.jpg")
# Need to save as thumbnail to keep aspect ratio
# If size is larger though, have to use resize - thumbnail won't work
img.thumbnail((400,400))
img.save('new_img.jpg')
#img.show()

# Can use simpy to move to another window but then have to use opencv to get a np array as input

# CAN'T IMPORT CV2 FOR SOME REASON
#import os
#import time
#from multiprocessing import Process
#import cv2

#def f(display):
#    os.environ['DISPLAY'] = display
#    print(os.environ['DISPLAY'])
#    a = cv2.imread('avatar.png')
#    cv2.imshow('window on %s'%display, a)
#    cv2.waitKey(1000)
#    time.sleep(10)

#Process(target=f, args=(':0.0',)).start()
#Process(target=f, args=(':0.1',)).start()

# slmpy doesn't work on Mac lol
# Think this is most promising - want to test on lab comp
import slmpy
import numpy as np
import time

slm = slmpy.SLMdisplay()
# slm = slmpy.SLMdisplay(monitor = x) - To specify monitor with x being monitor
slm = slmpy.SLMdisplay(isImageLock = False)
resX, resY = slm.getSize()
testIMG = np.zeros([resY,resX]).astype('uint8')
t0 = time.time()
for i in range(100):
  slm.updateArray(testIMG)
print(time.time() - t0)
slm.close()