"""Using the python's object oriented programming scheeme (OOPS) kindly complete the following tasks which is given as below:-

1)Create a python class called circle with constructor which will take a list as an argument for the task.
    The list is [10,501,22,37,1000,999,87,351]
2)Create proper member variables inside the task if required and use them when necessary. For example for this task
create a class private variable name pi = 3.141
3)From the given list create two class method Area and Perimeter which will be going to calculate the Area and Perimeter.
4)Kindly visit the below and convert the UML diagram into a python class and its methods.
    https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md
"""

#Create a class named circle
class circle:
    #create required member variable
    pi = 3.141

    #Constructor which takes a list as argument
    def __init__(self,radius):
        self.radius = radius

    #Method to calculate perimeter
    def perimeter(self):
        result = []
        for i in self.radius:
            result.append(2 * circle.pi * i)
        return result
    
    #method to calculate area
    def area(self):
        result = []
        for i in self.radius:
            result.append(circle.pi * pow(i,2))
        return result
    
#main code
given_list = [10,501,22,37,1000,999,87,351]
#given_list= int(given_list)
cir = circle(given_list)
print("Given list of radius of circle is : ", given_list)
print("Area of cirlce is : ",cir.area())
print("Perimeter of circle is : ",cir.perimeter())