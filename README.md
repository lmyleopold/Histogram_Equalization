# Histogram Equalization and Enhancement Techniques

## Project Overview

This project focuses on the implementation and analysis of various histogram equalization techniques to improve image contrast. The primary objectives include implementing the basic Histogram Equalization (HE) algorithm, exploring its pros and cons, and developing and evaluating advanced versions like Adaptive Histogram Equalization (AHE) and Contrast-Limited Adaptive Histogram Equalization (CLAHE).

## Project Structure

- **images/**: Contains the original and processed images.
  - `input/`: Original sample images.
  - `output/`: Images processed by HE, AHE, and CLAHE.
- **results/**: Stores histograms and CDF plots generated during the analysis.
- **report/**: Contains the final project report and any additional documentation.
  - `project_report.pdf`: The main report discussing the implementation, results, and analysis.

## Getting Started

### Prerequisites

To run the code provided in this project, you need to have the following installed:

- Python 3.x
- NumPy
- Matplotlib

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lmyleopold/Histogram_Equalization.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd Histogram_Equalization
   ```

### Usage

The project includes a command-line tool for applying different histogram equalization techniques to images. You can specify the input image, choose the desired method, and optionally plot the original and processed images along with their histograms.

#### Command Structure

```bash
python main.py --input <input_image_path> --method <HE|AHE|CLAHE> [--output <output_image_path>] [--plot]
```

#### Arguments

- `--input`: **(Required)** Path to the input image.
- `--method`: **(Required)** Histogram Equalization method to use. Choose from:
  - `HE`: Basic Histogram Equalization.
  - `AHE`: Adaptive Histogram Equalization.
  - `CLAHE`: Contrast-Limited Adaptive Histogram Equalization.
- `--output`: **(Optional)** Path to save the processed image. If not specified, the output image will be saved in the `images/output/` directory with a suffix indicating the method used.
- `--plot`: **(Optional)** Flag to plot the original and processed images along with their histograms.

#### Example Commands

1. **Basic Histogram Equalization (HE)**:
   ```bash
   python main.py --input images/sample.jpg --method HE --plot
   ```

2. **Adaptive Histogram Equalization (AHE)**:
   ```bash
   python main.py --input images/sample.jpg --method AHE --output images/output/sample_ahe.jpg
   ```

3. **Contrast-Limited Adaptive Histogram Equalization (CLAHE)**:
   ```bash
   python main.py --input images/sample.jpg --method CLAHE --plot
   ```

#### Output

- The processed image will be saved in the specified output path or, by default, in the `images/output/` directory with a suffix (`_he`, `_ahe`, `_clahe`) added to the original file name.
- If the `--plot` option is used, a window will open showing the original and processed images side by side, along with their corresponding histograms.

## Project Workflow

1. **Algorithm Implementation**: 
   - Implement basic and advanced histogram equalization techniques.
   - Optimize the algorithms for efficiency and readability.
2. **Image Processing**:
   - Apply the implemented algorithms to the provided sample images.
   - Generate and analyze histograms and CDFs to evaluate the effectiveness of each method.
3. **Result Analysis**:
   - Assess the pros and cons of each technique based on the processed images.
   - Identify scenarios where the basic HE algorithm fails and how advanced techniques address these issues.
4. **Report Writing**:
   - Compile the findings into a comprehensive report, including the implementation details, results, and discussions.

## Results and Analysis

The processed images and their corresponding histograms and CDFs demonstrate the effectiveness of the various histogram equalization techniques. The basic HE algorithm significantly improves the contrast in images with low dynamic range but may cause loss of detail in already high-contrast images. AHE and CLAHE address some of these issues by focusing on local contrast enhancement and mitigating noise amplification.

For a detailed discussion of the results, please refer to the [project report](report/project_report.pdf).
