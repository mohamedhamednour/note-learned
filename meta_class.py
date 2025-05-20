def say_hello(self):
    print(self.x)

MyClass = type(
    "MyClass",       
    (),              
    {
        "x": 5,              
        "say_hello": say_hello 
    }
)


obj = MyClass()
obj.say_hello()  