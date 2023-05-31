class Vector:
    def __init__(self, data):
        if isinstance(data, list) and len(data) == 1 and all(isinstance(item, float) for item in data[0]):
            # Initialize with a list of floats within a list
            self.values = [float(val) for val in data[0]]
        elif isinstance(data, list) and all(isinstance(f, float) for f in data):
            # Initialize with a list of floats
            self.values = [[float(val)] for val in data]
        elif isinstance(data, list) and all(isinstance(item, list) and len(item) == 1 and isinstance(item[0], float) for item in data):
            # Initialize with a list of lists of floats
            self.values = [[float(val[0])] for val in data]
        elif isinstance(data, int):
            # Initialize with a size
            self.values = [[float(i)] for i in range(data)]
        elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(item, int) for item in data):
            # Initialize with a range
            start, end = data
            if start > end:
                raise ValueError("Start value must be less than end value")
            self.values = [[float(i)] for i in range(start, end)]
        else:
            raise ValueError("Invalid input")
    
    def __str__(self):
        return str(self.values)
