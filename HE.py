import numpy as np

### equalize the distribution of histogram to enhance contrast
### @params img_arr : numpy.array uint8 type, 2-dim
### @params level : the level of gray scale
### @return arr : the equalized image array
def histogram_equalization(img_arr, level = 256):
    # get the shape of image
    rows, cols = img_arr.shape
    # get the histogram of image
    hist, bins = np.histogram(img_arr.flatten(), level, [0, level])
    # get the cumulative distribution of histogram
    cdf = hist.cumsum()
     # Normalize the CDF to be in the range [0, L-1]
    cdf_normalized = (cdf - cdf.min()) * (level - 1) / (cdf.max() - cdf.min())
    # Use the normalized CDF to map the pixel values
    arr = cdf_normalized[img_arr]
    arr = arr.astype('uint8')  # Ensure the image is in the uint8 format
    # Reshape the array back to the original image shape
    arr = arr.reshape(rows, cols)
    return arr