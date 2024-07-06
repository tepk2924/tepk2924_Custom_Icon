from PIL import Image
import numpy as np
import os

image_path = input("Input the image directory : ")
image_name = os.path.splitext(os.path.basename(image_path))[0]
image = Image.open(image_path).convert("RGBA")
image_resize = image.resize((256, 256))
image_resize.save(os.path.join(os.path.dirname(__file__), image_name + ".ico"))