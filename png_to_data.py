import os
import numpy as np
import h5py
from PIL import Image

# Path to your images directory
image_dir = '/Users/luchuqiao/Desktop/ECE176/project/ECE176_project/img_align_celeba'

# Path for the output HDF5 file
output_file = 'data.h5'

# Initialize a list to store the images
images = []

# Load images
for i in range(1, 3001):  # Assuming image filenames are in the format 000001.jpg to 003000.jpg
    filename = f'{i:06d}.jpg'
    filepath = os.path.join(image_dir, filename)
    with Image.open(filepath) as img:
        img_array = np.array(img)
        images.append(img_array)

# Convert the list of images to a NumPy array
images_np = np.array(images)

# Create an HDF5 file and dataset
with h5py.File(output_file, 'w') as h5f:
    h5f.create_dataset('images', data=images_np)

print(f"Saved {len(images)} images to {output_file}")
