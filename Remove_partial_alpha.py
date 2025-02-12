from PIL import Image
import numpy as np
import os

image_path = input("Input the image directory : ")
image_name = os.path.splitext(os.path.basename(image_path))[0]
extension = os.path.splitext(os.path.basename(image_path))[1]
image = np.array(Image.open(image_path).convert("RGBA"))
Achannelorigin = image[:, :, 3]
Achannel = image[:, :, 3]
Achannel = np.where(Achannel < 128, 0, Achannel)
Achannel = np.where(Achannel >= 128, 255, Achannel)
image[:, :, 3] = Achannel
image_pillow = Image.fromarray(image)
image_resize = image_pillow.resize((256, 256))
image_resize.save(os.path.join(os.path.dirname(__file__), image_name + "_Removed_partial_alpha" + extension))