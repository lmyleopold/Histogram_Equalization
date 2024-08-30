import numpy as np

def contrast_limited_ahe(img_arr, level=256, blocks=8, threshold=10.0):
    m, n = img_arr.shape
    block_m = m // blocks
    block_n = n // blocks
    
    # Initialize the list to store the CDFs for each block
    maps = []
    for i in range(blocks):
        row_maps = []
        for j in range(blocks):
            si, ei = i * block_m, (i + 1) * block_m
            sj, ej = j * block_n, (j + 1) * block_n
            block_img_arr = img_arr[si : ei, sj : ej]
            hists = np.histogram(block_img_arr.flatten(), level, [0, level])[0]
            
            # Clip the histogram and distribute clipped pixels
            clip_limit = threshold * np.mean(hists)
            excess_pixels = np.sum(hists[hists > clip_limit] - clip_limit)
            hists[hists > clip_limit] = clip_limit
            hists += int(excess_pixels / level)
            
            cdf = hists.cumsum()
            cdf = np.ma.masked_equal(cdf, 0)
            cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
            cdf = np.ma.filled(cdf, 0).astype('uint8')
            
            row_maps.append(cdf)
        maps.append(row_maps)
    
    arr = np.zeros_like(img_arr)
    for i in range(m):
        for j in range(n):
            r = i // block_m
            c = j // block_n
            
            # Ensure we don't go out of bounds
            if r >= blocks - 1:
                r = blocks - 2
            if c >= blocks - 1:
                c = blocks - 2

            x1 = (i % block_m) / block_m
            y1 = (j % block_n) / block_n
            
            # Retrieve the CDFs for the four surrounding blocks
            cdf_lu = maps[r][c]
            cdf_ru = maps[r][c + 1]
            cdf_lb = maps[r + 1][c]
            cdf_rb = maps[r + 1][c + 1]

            # Perform bilinear interpolation to get the new pixel value
            new_value = (1 - x1) * ((1 - y1) * cdf_lu[img_arr[i, j]] + y1 * cdf_lb[img_arr[i, j]]) + \
                        x1 * ((1 - y1) * cdf_ru[img_arr[i, j]] + y1 * cdf_rb[img_arr[i, j]])
            
            arr[i, j] = new_value
    
    return arr.astype('uint8')
