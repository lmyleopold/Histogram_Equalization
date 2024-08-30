import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def load_image(filepath):
    img = Image.open(filepath)
    return np.array(img.convert('L'))

def save_image(img_arr, filepath):
    # Convert the image array to an 8-bit format (mode 'L') before saving
    img = Image.fromarray(img_arr)
    # Check the image mode and convert it if necessary
    if img.mode in ('F', 'I'):
        img = img.convert('L')  # Convert to 8-bit grayscale mode
    img.save(filepath)


def plot_histograms(original_img_arr, result_img_arr, level=256):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the original image's histogram
    axs[0].set_title("Original Image Histogram")
    hist, bins = np.histogram(original_img_arr.flatten(), level, [0, level])
    cdf = hist.cumsum()
    cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())  # Normalize CDF
    axs[0].hist(original_img_arr.flatten(), level, [0, level], color='r')
    axs[0].plot(cdf, color='b', linewidth=2)
    axs[0].set_xlim([0, level])
    axs[0].legend(('CDF', 'Histogram'), loc='upper left')

    # Plot the result image's histogram
    axs[1].set_title("Result Image Histogram")
    hist, bins = np.histogram(result_img_arr.flatten(), level, [0, level])
    cdf = hist.cumsum()
    cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())  # Normalize CDF
    axs[1].hist(result_img_arr.flatten(), level, [0, level], color='r')
    axs[1].plot(cdf, color='b', linewidth=2)
    axs[1].set_xlim([0, level])
    axs[1].legend(('CDF', 'Histogram'), loc='upper left')

    plt.show()


def plot_images(original_img_arr, result_img_arr):
    plt.figure(figsize=(12, 6))
    # Plot original image
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_img_arr, cmap='gray')
    plt.axis('off')
    # Plot result image
    plt.subplot(1, 2, 2)
    plt.title("Processed Image")
    plt.imshow(result_img_arr, cmap='gray')
    plt.axis('off')

    plt.show()
