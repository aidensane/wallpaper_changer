import ctypes
import time

image_list = [
    "wallpapers\image_1.png",
    "wallpapers\image_2.png",
    "wallpapers\image_3.jpg",
    "wallpapers\image_4.jpg",
    "wallpapers\image_5.jpg"
]

while True:
    for image in image_list:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
        time.sleep(10)
        print("Wallpaper changed successfully!")
