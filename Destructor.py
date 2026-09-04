class Student: 
    def __init__(self, name, age):       # Constructor
        self.name = name 
        self.age = age 
 
    def display(self): 
        print("Name:", self.name) 
        print("Age:", self.age) 
 
    def __del__(self):                   # Destructor
        print("Student object destroyed") 
 
 
s = Student("Pratik", 21)                 # Object created here
s.display() 
 
del s                                    # Object destroyed here