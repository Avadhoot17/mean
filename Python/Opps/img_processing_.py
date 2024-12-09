import numpy as np

# Example RGB image: 3x3 pixels
# Each pixel has 3 values for Red, Green, and Blue
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],  # Row 1
    [[125, 125, 125], [255, 255, 255], [0, 0, 0]],  # Row 2
    [[100, 50, 200], [30, 180, 75], [200, 200, 50]]  # Row 3
])

# 1. Convert RGB image to Grayscale
# Grayscale formula: 0.2989 * Red + 0.5870 * Green + 0.1140 * Blue
grayscale_image = (0.2989 * rgb_image[:, :, 0] +
                   0.5870 * rgb_image[:, :, 1] +
                   0.1140 * rgb_image[:, :, 2]).astype(int)

print("Grayscale Image:")
print(grayscale_image)

# 2. Apply threshold to create a binary image
threshold = 128
binary_image = (grayscale_image > threshold).astype(int)  # 1 for white, 0 for black

print("\nBinary Image (Threshold 128):")
print(binary_image)