import os
import subprocess

image_path = "/Users/nupurkapur/Documents/Histogram_Equalization/images/sample_images_input/"


for filename in os.listdir(image_path):
     input_path = image_path + filename
     command = f"python main.py --input {input_path} --method CLAHE --plot"
     subprocess.run(command, shell=True)