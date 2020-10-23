import numpy as np
import cv2
import sys
from PIL import Image
import os
import functools

print = functools.partial(print, flush=True)

print("Welcome to ASCIILive.py")
print("Made by: CaydendW")
print("Note: You may have to resize terminal window to get best effect.")
print("Note: This does not work for Linux.")
print("Note: Press control+c in the terminanl or q in the window to exit. (crtl+c) (q)")

try:
    new_width = int(input("How big do you want the image?: "))
except:
    print(new_width + " is not a valid int")
    exit()

theme = str(input("Press d for dark mode and l for light mode (This depends on your terminal background): "))
pos = input("Please put w for windows or l for linux: ").lower()

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
elif theme=="l":
    chars = ["B","S","#","&","@","$","%","*","!",":"," "]
else:
    print(theme + " is not a valid option")
    exit()

if pos=="w":
    lspsa="cls"
elif pos=="l":
    lspsa="clear"
else:
    print(pos + " is not a valid option")
    exit()

try:
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, 1)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            os.system(lspsa)
            cap.release()
            cv2.destroyAllWindows()
            exit()

        img = Image.fromarray(gray)

        os.system(lspsa)
        
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

except KeyboardInterrupt:
    cap.release()
    os.system(lspsa)
    cv2.destroyAllWindows()
    exit()
