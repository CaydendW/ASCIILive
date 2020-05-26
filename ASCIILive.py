import numpy as np
import cv2
import sys
from PIL import Image
import os
import time as time
import functools

print = functools.partial(print, flush=True)

print("Welcome to ASCIILive.py")
print("Made by: Cayden de Wit")
print("Note: You may have to resize terminal window to get best effect.")
print("Note: This does not work for Linux.")
print("Note: Press control+c in the terminanl or q in the window to exit. (crtl+c) (q)")
new_width = int(input("How big do you want the image?: "))
theme = str(input("Press d for dark mode and leave blank for light.: "))

chars = []
cap = cv2.VideoCapture(0)

def disable_stdout_buffering():
    fileno = sys.stdout.fileno()
    temp_fd = os.dup(fileno)
    sys.stdout.close()
    os.dup2(temp_fd, fileno)
    os.close(temp_fd)
    sys.stdout = os.fdopen(fileno, "w")

if theme=="d":
    chars = [" ",":","!","*","%","$","@","&","#","S","B"]
else:
    chars = ["B","S","#","&","@","$","%","*","!",":"," "]

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    try:
        a = "B"
    except KeyboardInterrupt:
        break

    cv2.imwrite(r"D:\Users\cayde\Documents\Code\Resources\Python.jpg",gray)
    image_path = r"D:\Users\cayde\Documents\Code\Resources\Python.jpg"
    img = Image.open(image_path)

    os.system('cls')
    
    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    disable_stdout_buffering()
    print(ascii_image)

    try:
        a = "B"
    except KeyboardInterrupt:
        break

os.system('cls')
cap.release()
cv2.destroyAllWindows()
time.sleep(1)
os.system('cls')