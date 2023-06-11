import numpy as np
"""
NumPy arrays are faster and more compact than Python lists. An array consumes less memory and is convenient to use.
NumPy uses much less memory to store data and it provides a mechanism of specifying the data types. 
"""
class NumPyCreator:
    def from_list(self, lst, dtype=None):
        if len(set(len(sublist) for sublist in lst)) != 1 or not all(isinstance(sublist, list) for sublist in lst):
            return None
        return np.array(lst, dtype)
    
    def from_tuple(self, tpl, dtype=None):
        if len(set(len(sublist) for sublist in tpl)) != 1 or not isinstance(tpl, tuple):
            return None
        return np.array(tpl, dtype)
    
    def from_iterable(self, itr, dtype=None):
        return np.array(itr, dtype)
    
    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype)
    
    def random(self, shape, dtype=None):
        return np.random.rand(*shape) if dtype is None else np.random.rand(*shape).astype(dtype)
    
    def identity(self, n, dtype=None):
        return np.identity(n, dtype)
    
    
if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    print(npc.from_list([[1,2,3],[6,4]]))
    print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
    print(npc.from_list(((1,2),(3,4))))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_tuple(["a","b","c"]))
    print(npc.from_iterable(range(5)))
    shape=(3,5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))