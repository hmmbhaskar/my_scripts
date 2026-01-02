# Pillow library for image processing. 
from PIL import Image

images = [Image.open(f) for f in ["1.jpg","2.jpg","3.jpg", "4.jpg"]]
images[0].save("output.pdf", save_all=True, append_images=images[1:])
