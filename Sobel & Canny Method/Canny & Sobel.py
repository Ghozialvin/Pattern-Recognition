# -*- coding: utf-8 -*-
"""Tugas Pengpol1_Ghozi Alvin Karim_121450123.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GZZgiAjQa87-XaXKkg4diTYPcxvCTIFD

# Tugas Pengenalan Pola
---
> Nama :Ghozi Alvin Karim \
> Nim : 121450123 \
> Kelas : Pengenalan Pola (RA)
---

## Algoritma Sobel
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_edge_detector(image_path):
    # Read the image using OpenCV -Computer Vision
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")

    # Apply Sobel operator
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate gradient magnitude
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Apply a threshold to identify edges
    threshold = 50
    edges = magnitude > threshold

    return edges

# Example usage
image_path = '/content/drive/MyDrive/S7/data1.jpg'
try:
    edge_image = sobel_edge_detector(image_path)

    # Display the original and edge-detected images
    original_image = cv2.imread(image_path)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Plotting the images using matplotlib
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(original_image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    # Edge-detected Image
    plt.subplot(1, 2, 2)
    plt.imshow(edge_image, cmap='gray')
    plt.title('Edge-detected Image (Sobel)')
    plt.axis('off')

    # Display the images
    plt.show()

except ValueError as e:
    print(e)

"""## Algoritma Canny"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_edge_detector(image_path, low_threshold=50, high_threshold=150):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")

    # Apply Canny edge detector
    edges = cv2.Canny(image, low_threshold, high_threshold)

    return edges

# Example usage
image_path = '/content/drive/MyDrive/S7/data1.jpg'
try:
    edge_image = canny_edge_detector(image_path)

    # Display the original and edge-detected images
    original_image = cv2.imread(image_path)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Plotting the images using matplotlib
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(original_image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    # Edge-detected Image
    plt.subplot(1, 2, 2)
    plt.imshow(edge_image, cmap='gray')
    plt.title('Edge-detected Image (Canny)')
    plt.axis('off')

    # Display the images
    plt.show()

except ValueError as e:
    print(e)