import cv2
import numpy as np
from PIL import Image
from os import system, name
from time import sleep
import numpy as np
import math

DENSITY = r"Ñ@#W$9876543210?!abc;:+=-,._            "

def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def get_item(lst,i):
    return(lst[i//len(lst[0])][i%len(lst[0])])

def cv2_to_pil(img): #Since you want to be able to use Pillow (PIL)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def pil_to_cv2(img):
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

cam = cv2.VideoCapture(0)
while True:
    clear_screen()
    ret_val, img = cam.read()

    c = cv2.waitKey(1)
    if c == 27:
        break

    img = cv2.flip(img, 1)
    pil_img = cv2_to_pil(img)

    height = 40
    width = 150
    pil_img = pil_img.resize((width, height))

    data = list(pil_img.getdata())
    arr = np.array(data)
    arr = arr.reshape(height, width, 3)

    for y in range(height):
        #print("\t\t\t", end = "")
        for x in range(width):
            r, g, b = arr[y][x]
            avg = (r + g + b) / 3
            char_idx = math.floor((avg - 0) / (254 - 0) * ((len(DENSITY) - 1) - 0) + 0)
            print(DENSITY[char_idx], end= "")
        print()


    sleep(0.1)


cam.release()
cv2.destroyAllWindows()
