import numpy as np
import sys
from ImageProcessor import ImageProcessor

class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -----
            array: numpy.ndarry corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        inverted_array = 1 - array
        inverted_array[..., 3:] = array[..., 3:]
        return inverted_array
    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -----
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function shold not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        new_array = array.copy()
        
        # Set the red and green channels to zero
        new_array[:, :, 0] = 0
        new_array[:, :, 1] = 0
        return new_array
    
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -----
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        new_array = array.copy()
        
        # Set the red and blue channels to zero
        new_array[:, :, 0] = 0
        new_array[:, :, 2] = 0
        return new_array
    
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -----
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        new_array = array.copy()
        
        # Set the green and blue channels to zero
        new_array[:, :, 1] = 0
        new_array[:, :, 2] = 0
        return new_array
        
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on shades of your image.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numoy.ndarray corresponding to the image.
        Return:
        -----
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        
        num_shades = 5
        shades = np.linspace(0, 1, num_shades)
        
        transformed_array = array.copy()
        
        for i in range(len(shades) - 1):
            lower_shade = shades[i]
            upper_shade = shades[i + 1]
            for channel in range(3):
                mask = (transformed_array[..., channel] > lower_shade) & (transformed_array[..., channel] <= upper_shade)
                transformed_array[..., channel][mask] = lower_shade
        return transformed_array
    
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RGB channels.
        For filter = 'weight'/'w': performs the weighted mean of RGB channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m', 'mean', 'w', 'weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                     corresponding to the weights of each RGB channels.
        Return:
        -----
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        grayscale_array = array.copy()
        if filter in ['m', 'mean']:
            grayscale_array[...,:3] = np.mean(array[...,:3], axis=2, keepdims=True)
        elif filter in ['w', 'weight']:
            if 'weights' not in kwargs:
                print("Missing weights argument", sys.stderr)
                return None
            weights = kwargs['weights']
            if len(weights) != 3:
                print("Weights argument must be a list of 3 floats", sys.stderr)
                return None
            if sum(weights) != 1:
                print("Sum of weights must be equal to 1", sys.stderr)
                return None
            grayscale_array[...,:3] = np.sum(array[...,:3] * weights, axis=2, keepdims=True) 
        else:
            print("Invalid filter argument", sys.stderr)
            return None
        return grayscale_array
    
if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("./assets/42AI.png")
    # arr = imp.load("./assets/elon_canaGAN.png")
    cf = ColorFilter()
    # print(arr)
    imp.display(cf.invert(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weight', weights=[0.2, 0.3, 0.5]))