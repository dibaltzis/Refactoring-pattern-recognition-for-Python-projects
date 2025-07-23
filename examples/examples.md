# Refactors Examples

## Refactor replace exception test
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
def func(values, index):
try:
    return values[index]
except IndexError:
    return 0
```
</td>
<td>

```python
def func(values, index):
    if index >= len(values):   
        return 0
    return values[index]
```

</td>
</tr>
</table>

## Refactor preserve whole object
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
def temp_difference(min_temperature, max_temperature):
    return max_temperature - min_temperature

min_temp = 20
max_temp = 30
temperature_difference = temp_difference(min_temp, max_temp)
```
</td>
<td>

```python
def temp_difference(min_temperature, max_temperature):
    return max_temperature - min_temperature

class TemperatureRange:
    def __init__(self, min_temperature, max_temperature):
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature

temp_range = TemperatureRange(min_temperature=20, max_temperature=30)
temperature_difference = temp_difference(temp_range)
```

</td>
</tr>
</table>

## Refactor Replace Magic Number With Symbolic Constant
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
def potentialEnergy(mass, height):
    return mass * height * 9.81
```
</td>
<td>

```python
GRAVITATIONAL_CONSTANT = 9.81
def potentialEnergy(mass, height):
   return mass * height * GRAVITATIONAL_CONSTANT
```

</td>
</tr>
</table>

## Refactor Encapsulated Collection
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class DataProcessor:
     def __init__(self):
         self.data = [1, 2, 3, 4, 5]
```
</td>
<td>

```python
class DataProcessor:
     def __init__(self):
         self._data = [1, 2, 3, 4, 5]
     def get_data(self):
         return self._data.copy()
```

</td>
</tr>
</table>

## Refactor Encapsulated field
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class MyClass:
   def __init__(self):
       self.my_field = "a field"
```
</td>
<td>

```python
class MyClass:
    def __init__(self):
       self._my_field = "a field"

    def get_my_field(self):
        return self._my_field

    def set_my_field(self,value):
        self._my_field = value
```

</td>
</tr>
</table>


## Refactor move method
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
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

```
</td>
<td>

```python
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
```

</td>
</tr>
</table>

## Refactor move field
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class B:
    def __init__(self,c,d):
        self.c=c
        self.d=d
```
</td>
<td>

```python
class A:
    def __init__(self,a):
        self.a=a

class B:
    def __init__(self,b,c,d):
        self.b=b
        self.c=c
        self.d=d
```

</td>
</tr>
</table>

## Refactor Extract class
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
```
</td>
<td>

```python
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B:
    def __init__(self,z):
        self.z=z
```

</td>
</tr>
</table>


## Refactor Inline class
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B:
    def __init__(self,z):
        self.z=z
    def a_method(self):
        pass
```
</td>
<td>

```python
class A:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def a_method(self):
        pass
```

</td>
</tr>
</table>

## Refactor pull up field
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self,x):
        self.x=x
        
class B(A):
    def __init__(self,y):
        self.y=y
class C(A):
    def __init__(self,y):
        self.y=y
```
</td>
<td>

```python
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
```

</td>
</tr>
</table>


## Refactor push down field
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B(A):
    def __init__(self,y):
        super().__init__(y)
```
</td>
<td>

```python
class A:
    def __init__(self,x):
        self.x=x
        
class B(A):
    def __init__(self,y):
        self.y=y
```

</td>
</tr>
</table>

## Refactor pull up method
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def method_x(self):
        pass

class B(A):
    def method_y(self):
        pass
    def method_z(self):
        pass
```
</td>
<td>

```python
class A:
    def method_x(self):
        pass
    def method_z(self):
        pass
class B(A):
    def method_y(self):
        pass
```

</td>
</tr>
</table>

## Refactor push down method
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def method_x(self):
        pass
    def method_z(self):
        pass
class B(A):
    def method_y(self):
        pass

```
</td>
<td>

```python
class A:
    def method_x(self):
        pass

class B(A):
    def method_y(self):
        pass
    def method_z(self):
        pass
```

</td>
</tr>
</table>

## Refactor pull up constructor body
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A(B):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

```
</td>
<td>

```python
class A(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
```

</td>
</tr>
</table>

## Refactor extract subclass
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    def get_details(self):
        return f"Job: {self.title}, \
            Salary: ${self.salary}
```
</td>
<td>

```python
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
```

</td>
</tr>
</table>

## Refactor extract superclass
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
class A:
    def __init__(self) -> None:
        pass
class B:
    def __init__(self) -> None:
        pass
```
</td>
<td>

```python
class C:
    def __init__(self) -> None:
        pass
class A(C):
    def __init__(self) -> None:
        pass
class B(C):
    def __init__(self) -> None:
        pass

```

</td>
</tr>
</table>

## Refactor collaplse hierarchy
<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>

```python
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
```
</td>
<td>

```python
class A:
    def __init__(self,x,y,z=None):
        self.x=x
        self.y=y
        self.z=z
    def a_method(self):
        return self.x+self.y +\
            self.z if self.z is not None else ""
```

</td>
</tr>
</table>