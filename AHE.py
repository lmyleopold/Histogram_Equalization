import numpy as np
from HE import histogram_equalization

def adaptive_histogram_equalization(img_arr, level=256, window_size=32, affect_size=16):
    arr = img_arr.copy()
    m, n = img_arr.shape
    # Caculate the number of rows and columns
    rows = (m - window_size) // affect_size + 1
    cols = (n - window_size) // affect_size + 1
    
    for i in range(rows):
        for j in range(cols):
            off = (window_size - affect_size) // 2
            asi, aei = i * affect_size + off, (i + 1) * affect_size + off
            asj, aej = j * affect_size + off, (j + 1) * affect_size + off
            wsi, wei = i * affect_size, i * affect_size + window_size
            wsj, wej = j * affect_size, j * affect_size + window_size
            
            window_arr = img_arr[wsi : wei, wsj : wej]
            block_arr = histogram_equalization(window_arr, level)
            
            if i == 0:
                arr[wsi : asi, wsj : wej] = block_arr[0 : asi - wsi, :]
            elif i >= rows - 1:
                arr[aei : wei, wsj : wej] = block_arr[aei - wsi : wei - wsi, :]
            if j == 0:
                arr[wsi : wei, wsj : asj] = block_arr[:, 0 : asj - wsj]
            elif j >= cols - 1:
                arr[wsi : wei, aej : wej] = block_arr[: , aej - wsj : wej - wsj]
            arr[asi : aei, asj : aej] = block_arr[asi - wsi : aei - wsi, asj - wsj : aej - wsj]
                
    return arr
