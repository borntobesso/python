import numpy as np
import sys

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height and width of the image)
        from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers
            position: tuple of 2 integers
        Return:
        -----
            new_arr: the cropped numpy.ndarray
            None (if combination of parameters not valid)
        Raise:
        -----
            This function shold not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or not isinstance(dim[0], int) or not isinstance(dim[1], int):
            print("Invalid dim argument", sys.stderr)
            return None
        if not isinstance(position, tuple) or len(position) != 2 or not isinstance(position[0], int) or not isinstance(position[1], int):
            print("Invalid position argument", sys.stderr)
            return None
        if position[0] < 0 or position[1] < 0:
            print("Invalid position argument", sys.stderr)
            return None
        if position[0] + dim[0] > array.shape[0] or position[1] + dim[1] > array.shape[1]:
            print("Invalid combination of dim and position arguments", sys.stderr)
            return None
        new_arr = array[position[0]:position[0]+dim[0], position[1]:position[1]+dim[1]]
        return new_arr