import argparse
import os
from utils import load_image, save_image, plot_histograms, plot_images
from HE import histogram_equalization
from AHE import adaptive_histogram_equalization
from CLAHE import contrast_limited_ahe

def main():
    parser = argparse.ArgumentParser(description="Histogram Equalization Tool")
    parser.add_argument('--input', required=True, help="Path to input image")
    parser.add_argument('--output', required=False, help="Path to save the output image")
    parser.add_argument('--method', required=True, choices=['HE', 'AHE', 'CLAHE'], help="Histogram Equalization Method")
    parser.add_argument('--plot', action='store_true', help="Plot the histogram and image")
    
    args = parser.parse_args()
    
    # Load image
    img_arr = load_image(args.input)
    
    # Process image
    if args.method == 'HE':
        result_img_arr = histogram_equalization(img_arr=img_arr)
    elif args.method == 'AHE':
        result_img_arr = adaptive_histogram_equalization(img_arr=img_arr, window_size=160)
    elif args.method == 'CLAHE':
        result_img_arr = contrast_limited_ahe(img_arr=img_arr, blocks=4, threshold=4)
    
    # Save image
    # Get the input file name and extension
    input_filename = os.path.basename(args.input)
    input_name, input_ext = os.path.splitext(input_filename)
    # Generate the output file name based on the method
    if args.method == 'HE':
        suffix = "_he"
    elif args.method == 'AHE':
        suffix = "_ahe"
    elif args.method == 'CLAHE':
        suffix = "_clahe"
    # Set the default output file name if not provided
    if not args.output:
        args.output = f"images/sample_images_output/{input_name}{suffix}{input_ext}"
    save_image(result_img_arr, args.output)
    
    # Plot if needed

    histogram_filename = f"images/histogram_output/{input_name}{suffix}_Histogram{input_ext}"
    if args.plot:
        plot_histograms(original_img_arr=img_arr, result_img_arr=result_img_arr, filename=histogram_filename)
        plot_images(original_img_arr=img_arr, result_img_arr=result_img_arr)

if __name__ == "__main__":
    main()
