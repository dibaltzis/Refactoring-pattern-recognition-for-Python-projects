#example replace exception test
def func(values, index):
    try:
        return values[index]
    except IndexError:
        return 0

#example preserve whole object
def temp_difference(min_temperature, max_temperature):
    return max_temperature - min_temperature

min_temp = 20
max_temp = 30
temperature_difference = temp_difference(min_temp, max_temp)

#example for Replace Magic Number With Symbolic Constant	
def potentialEnergy(mass, height):
    return mass * height * 9.81

#example Encapsulated Collection
class DataProcessor:
     def __init__(self):
         self.data = [1, 2, 3, 4, 5]

#example Encapsulated field
class MyClass:
   def __init__(self):
       self.my_field = "a field"
       
#example move method
class A:
    def method_A1(self):
        pass
    def method_A2(self):
        pass
class B:
    def method_B1(self):
        pass
    def method_B2(self):
        pass

#example Move field
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class B:
    def __init__(self,c,d):
        self.c=c
        self.d=d

#example Extract class
class A:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

#example Inline class
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B:
    def __init__(self,z):
        self.z=z
    def a_method(self):
        pass

#example pull up field
class A:
    def __init__(self,x):
        self.x=x
        
class B(A):
    def __init__(self,y):
        self.y=y
class C(A):
    def __init__(self,y):
        self.y=y

#example push down field
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B(A):
    def __init__(self,y):
        super().__init__(y)

#example pull up method
class A:
    def method_x(self):
        pass

class B(A):
    def method_y(self):
        pass
    def method_z(self):
        pass

#example push down method
class A:
    def method_x(self):
        pass
    def method_z(self):
        pass
class B(A):
    def method_y(self):
        pass
#example pull up constructor body
class A(B):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
#example extract subclass
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    def get_details(self):
        return f"Job: {self.title}, \
            Salary: ${self.salary}"

#example extract superclass




class A:
    def __init__(self) -> None:
        pass
class B:
    def __init__(self) -> None:
        pass

#example collaplse hierarchy
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def a_method(self):
        return self.x+self.y
class B(A):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def a_method(self):
        base = super().a_method()
        return base + self.z
