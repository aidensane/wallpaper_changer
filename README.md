# Automatic Desktop Wallpaper Changer
This Python script automatically changes the desktop wallpaper of a Windows machine at regular intervals. The user can specify a list of images and the script will randomly select an image from the list and set it as the desktop wallpaper.

# Requirements
This script requires the ctypes module and runs on Windows machines only.

# Usage
1. Clone or download the script and the wallpaper images.
2. Edit the image_list variable in the script to add or remove images.
3. Run the script using python change_desktop.py.
4. The script will run indefinitely, changing the wallpaper every 10 seconds.
# Acknowledgements
The script uses the SystemParametersInfoW function from the ctypes module to change the desktop wallpaper
