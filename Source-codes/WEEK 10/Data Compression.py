import numpy as np
from PIL import Image

# Load the image
image = Image.open('lena.jpg')
pixel_map = np.array(image)

# Create a new image with the same size
img = Image.new(image.mode, image.size)
pixel_new = np.array(img)

# Loop through the original image
for i in range(image.size[0]):
    for j in range(image.size[1]):
        value = pixel_map[i, j]

        # Map the 8-bit value to a 3-bit value
        if 0 <= value <= 31:
            pixel_new[i, j] = 0
        elif 32 <= value <= 63:
            pixel_new[i, j] = 1
        elif 64 <= value <= 95:
            pixel_new[i, j] = 2
        elif 96 <= value <= 127:
            pixel_new[i, j] = 3
        elif 128 <= value <= 159:
            pixel_new[i, j] = 4
        elif 160 <= value <= 191:
            pixel_new[i, j] = 5
        else:
            pixel_new[i, j] = 6

# Save the new image
img.save('lena_compressed.jpg')

# Display the new image
img.show()