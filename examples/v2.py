#example replace exception test
def func(values, index):
    if index >= len(values):   
        return 0
    return values[index]

#example preserve whole object
def temp_difference(min_temperature, max_temperature):
    return max_temperature - min_temperature

class TemperatureRange:
    def __init__(self, min_temperature, max_temperature):
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature

temp_range = TemperatureRange(min_temperature=20, max_temperature=30)
temperature_difference = temp_difference(temp_range)

#example for Replace Magic Number With Symbolic Constant	
GRAVITATIONAL_CONSTANT = 9.81
def potentialEnergy(mass, height):
   return mass * height * GRAVITATIONAL_CONSTANT

#example Encapsulated Collection
class DataProcessor:
     def __init__(self):
         self._data = [1, 2, 3, 4, 5]
     def get_data(self):
         return self._data.copy()  

#example Encapsulated field
class MyClass:
    def __init__(self):
       self._my_field = "a field"

    def get_my_field(self):
        return self._my_field

    def set_my_field(self,value):
        self._my_field = value
        
#example move method
class A:
    def method_A1(self):
        pass
class B:
    def method_B1(self):
        pass
    def method_B2(self):
        pass
    def method_A2(self):
        pass

#example Move field
class A:
    def __init__(self,a):
        self.a=a

class B:
    def __init__(self,b,c,d):
        self.b=b
        self.c=c
        self.d=d
        
#example Extract class
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B:
    def __init__(self,z):
        self.z=z

#example Inline class
class A:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def a_method(self):
        pass
#example pull up field
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B(A):
    def __init__(self,y):
        super().__init__(y)
class C(A):
    def __init__(self,y):
        super().__init__(y)

#example push down field
class A:
    def __init__(self,x):
        self.x=x
        
class B(A):
    def __init__(self,y):
        self.y=y
        
#example pull up method
class A:
    def method_x(self):
        pass
    def method_z(self):
        pass
class B(A):
    def method_y(self):
        pass

#example push down method
class A:
    def method_x(self):
        pass

class B(A):
    def method_y(self):
        pass
    def method_z(self):
        pass

#example pull up constructor body
class A(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

#example extract subclass
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    def get_details(self):
        return f"Job: {self.title}, \
            Salary: ${self.salary}"
class FullTimeJob(Job):
     def __init__(self, title, salary, benefits):
         super().__init__(title, salary)
         self.benefits = benefits
     def get_details(self):
         base_details = super().get_details()
         return f"{base_details}, \
             Benefits: {self.benefits}"
             
#example extract superclass
class C:
    def __init__(self) -> None:
        pass
class A(C):
    def __init__(self) -> None:
        pass
class B(C):
    def __init__(self) -> None:
        pass

#example collaplse hierarchy
class A:
    def __init__(self,x,y,z=None):
        self.x=x
        self.y=y
        self.z=z
    def a_method(self):
        return self.x+self.y +\
            self.z if self.z is not None else ""