import math

class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, num):
        self.value += num
        return self.value
    
    def subtract(self, num):
        self.value -= num
        return self.value
    
    def multiply(self, num):
        self.value *= num
        return self.value
    
    def divide(self, num):
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.value /= num
        return self.value
    
    def reset(self):
        self.value = 0
    
    def get_value(self):
        return self.value

def compute():
    calc = Calculator()
    numbers = [10, 5, 0, -3]
    
    for num in numbers:
        if num > 0:
            calc.add(num)
        elif num < 0:
            calc.subtract(abs(num))
        else:
            pass  
    
    try:
        result = calc.divide(2)
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        assert result is not None
    finally:
        print("Final result:", result)
    
    return result


square = lambda x: x * x


with open("output.txt", "w") as f:
    f.write("Square of 5: " + str(square(5)))


i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue  
    print("Odd number:", i)
    if i == 7:
        break 
    i += 1

global_var = 100

def outer():
    nonlocal_var = 50
    
    def inner():
        nonlocal nonlocal_var
        nonlocal_var += 10
        print("Inside inner function:", nonlocal_var)
    
    inner()
    print("Inside outer function:", nonlocal_var)

outer()


def generator_example():
    for i in range(3):
        yield i ** 2

gen = generator_example()
print("Generated values:", list(gen))


