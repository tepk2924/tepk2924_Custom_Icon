from PIL import Image
import numpy as np

image_path = input("Input the image directory : ")
image = np.array(Image.open(image_path).convert("RGBA"))
alpha = image[:, :, 3]
iszeromask = np.where(alpha == 0)
is255mask = np.where(alpha == 255)
print(f"Number of pixels w/ zero alpha value : {len(iszeromask[0])}")
print(f"Number of pixels w/ 255 alpha value : {len(is255mask[0])}")
print(f"Number of pixels w/ partial alpha value (1 - 254) : {alpha.shape[0]*alpha.shape[1] - len(iszeromask[0]) - len(is255mask[0])}")
