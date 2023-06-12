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
    
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the numer of row/column of the array
                (depending on the axis value).
            axis: positive non null integer (0 or 1).
        Return:
        -----
            new_arr: thined numpy.ndarray.
            None (if conbination of parameters not valid).
        Raise:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        if not isinstance(n, int) or n <= 0:
            print("Invalid n argument", sys.stderr)
            return None
        if not isinstance(axis, int) or axis < 0 or axis > 1:
            print("Invalid axis argument", sys.stderr)
            return None
        if axis == 0 and n > array.shape[0]:
            print("Invalid combination of n and axis arguments", sys.stderr)
            return None
        if axis == 1 and n > array.shape[1]:
            print("Invalid combination of n and axis arguments", sys.stderr)
            return None
        new_arr = np.delete(array, np.s_[n - 1::n], axis)
        return new_arr
    
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -----
            new_arr: juxtaposed numpy.ndarray.
            None (if combination of parameters not valid).
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        if not isinstance(n, int) or n <= 0:
            print("Invalid n argument", sys.stderr)
            return None
        if not isinstance(axis, int) or axis < 0 or axis > 1:
            print("Invalid axis argument", sys.stderr)
            return None
        new_arr = np.concatenate([array]*n, axis)
        return new_arr
    
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetitions along each dimensions.
        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 positive non null integers.
        Return:
        -----
            new_arr: mosaic numpy.ndarray.
            None (if combination of parameters not valid).
        Raises:
        -----
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            print("Input is not a numpy array", sys.stderr)
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or not isinstance(dim[0], int) or not isinstance(dim[1], int):
            print("Invalid dim argument", sys.stderr)
            return None
        if dim[0] <= 0 or dim[1] <= 0:
            print("Invalid dim argument", sys.stderr)
            return None
        new_arr = np.tile(array, dim)
        return new_arr
    
if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    print(spb.crop(arr1, (3, 1), (1, 0)))
    
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    print(arr2)
    print(spb.thin(arr2, 3, 0))

    arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))

    arr4 = np.array([1, 2, 3, 4])
    print(spb.mosaic(arr4, (4, 1)))
    # Expected output:
    #   [[1, 2, 3, 4],
    #    [1, 2, 3, 4],
    #    [1, 2, 3, 4],
    #    [1, 2, 3, 4]]