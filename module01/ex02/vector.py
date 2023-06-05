class Vector:
    def __init__(self, data):
        if isinstance(data, list) and len(data) == 1 and all(isinstance(f, float) for f in data[0]):
            # Initialize with a list of list of floats (row vector)
            self.values = data
            self.shape = (1, len(data[0]))
        elif isinstance(data, list) and all(isinstance(item, list) and len(item) == 1 and isinstance(item[0], float) for item in data):
            # Initialize with a list of lists of single float (column vector)
            self.values = data
            self.shape = (len(data), 1)
        elif isinstance(data, int):
            # Initialize with a size
            self.values = [[float(i)] for i in range(data)]
            self.shape = (data, 1)
        elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(item, int) for item in data):
            # Initialize with a range
            start, end = data
            if start > end:
                raise ValueError("Start value must be less than end value")
            self.values = [[float(i)] for i in range(start, end)]
            self.shape = (end - start, 1)
        else:
            raise ValueError("Invalid input")
    
    def __add__(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                if self.shape[0] == 1:
                    return Vector([list(self.values[0][i] + other.values[0][i] for i in range(self.shape[1]))])
                else:
                    new_values = []
                    for i in range(self.shape[0]):
                        new_values.append([self.values[i][0] + other.values[i][0]])
                    return Vector(new_values)
            else:
                raise ValueError("Cannot add vectors with different shapes")
        else:
            raise TypeError("Cannot add vector with non-vector")

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                if self.shape[0] == 1:
                    return Vector([list(self.values[0][i] - other.values[0][i] for i in range(self.shape[1]))])
                else:
                    new_values = []
                    for i in range(self.shape[0]):
                        new_values.append([self.values[i][0] - other.values[i][0]])
                    return Vector(new_values)
            else:
                raise ValueError("Cannot subtract vectors with different shapes")
        else:
            raise TypeError("Cannot subtract vector with non-vector")
        
    def __rsub__(self, other):
        return self - other
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            else:
                if self.shape[0] == 1:
                    return Vector([list(self.values[0][i] / other for i in range(self.shape[1]))])
                else:
                    new_values = []
                    for i in range(self.shape[0]):
                        new_values.append([self.values[i][0] / other])
                    return Vector(new_values)
        elif isinstance(other, Vector):
            raise NotImplementedError("Division of two Vectors is not defined here.")
        else:
            raise TypeError("Vector can be devided only by a scalar")

    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if self.shape[0] == 1:
                return Vector([list(self.values[0][i] * other for i in range(self.shape[1]))])
            else:
                new_values = []
                for i in range(self.shape[0]):
                    new_values.append([self.values[i][0] * other])
                return Vector(new_values)
        elif isinstance(other, Vector):
            raise NotImplementedError("Multiplication of two Vectors is not defined here.")
        else:
            raise TypeError("Vector can be multiplied only by a scalar")
        
    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return self.__str__()
    
    def dot(self, other):
        '''Dot product of two vectors'''
        if isinstance(other, Vector):
            if self.shape == other.shape:
                if self.shape[0] == 1:
                    return sum(self.values[0][i] * other.values[0][i] for i in range(self.shape[1]))
                else:
                    return sum(self.values[i][0] * other.values[i][0] for i in range(self.shape[0]))
            else:
                raise ValueError("Cannot dot vectors with different shapes")
        else:
            raise TypeError("Cannot dot product vector with non-vector")
        
    def T(self):
        '''Transpose of a vector'''
        # new_values = []
        if self.shape[0] == 1:
            new_values = [[i] for i in self.values[0]]
            # for i in range(self.shape[1]):
            #     new_values.append([self.values[0][i]])
            return Vector(new_values)
        else:
            new_list = []
            new_values = [[i[0] for i in self.values]]
            # for i in range(self.shape[0]):
            #     new_list.append(self.values[i][0])
            # new_values.append(new_list)
            return Vector(new_values)
