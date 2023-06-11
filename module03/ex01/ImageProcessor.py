import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

class ImageProcessor:
    def load(self, path):
        try:
            img = Image.open(path)
            print(f"Loading image of size: {img.size[0]} x {img.size[1]} pixels.")
            # Normalize image arry to range [0, 1]
            return np.array(img, np.float32) / 255.0
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                print("Image file not found", sys.stderr)
            elif isinstance(e, Image.UnidentifiedImageError):
                print("Image file cannot be opened and identified", sys.stderr)
            else:
                print("Unknown error", sys.stderr)
                
    def display(self, array):
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return
        try:
            plt.imshow(array)
            plt.axis("off")
            plt.show()
        except Exception as e:
            print("Error displaying image", sys.stderr)
            print(e)
            return
            
if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("non_existing_file.png")
    print(arr)
    arr = imp.load("empty_file.png")
    print(arr)
    arr = imp.load("./resources/42AI.png")
    print(arr)
    imp.display(arr)
    imp.display("not_an_array")