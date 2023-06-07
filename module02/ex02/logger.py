'''decorators wrap a function, modifying its behavior.
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
'''

import functools
import time
import os
from random import randint

def log(func):
    @functools.wraps(func)
    def wrapper_log(*args, **kwargs):
        f = open("machine.log", "a")
        str = f"({os.environ.get('USER')})Running:"
        name = func.__name__.replace("_", " ").title()
        str += f" {name:19}"
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        str += f"[ exec-time = {run_time:.3f} ms ]\n"
        f.write(str)
        f.close()
        return value
    return wrapper_log
    
class CoffeeMachine():
    
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
         return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        
    machine.make_coffee()
    machine.add_water(70)
            