# Creating An Image

from PIL import Image

# Creating Image
img = Image.new("RGB", (100, 100), color="white")

# Saving Image
img.save("output6.png")
