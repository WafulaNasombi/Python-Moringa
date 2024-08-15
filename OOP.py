class MyClass:
    def __init__(self, name): # instance method- they  are called on objects
        self.name = name #instance variable. The self keyword is used to access the attributes and methods of the class in python.

    def say_hello(self):
        print(f"Hello, {self.name}!")

# Creating objects of the class
obj1 = MyClass("John")
obj2 = MyClass("Alice")

# Calling the method on the objects
obj1.say_hello()
obj2.say_hello()

# Output
"""
Hello John!
Hello Alice!
"""

# or 

class Person():
    
    def introduce(self):
        return f'Hi, my name is {self.name}. It is a pleasure to meet you!'
    
    def say_hello(self):
        return 'Hi, how are you?'
        
    def eat_breakfast(self):
        self.hungry = False
        return 'Yum that was delish!'
        
gail = Person()
gail.name = 'Gail'
the_snail = Person()
the_snail.name = 'the Snail'
print('1. ', gail.introduce())
print('2. ', the_snail.introduce())

# Output
"""
1.  Hi, my name is Gail. It is a pleasure to meet you!
2.  Hi, my name is the Snail. It is a pleasure to meet you!
"""
#METHOD
def say_hello_and_weather(instance_obj, weather_pattern):
    return f"Hi, my name is {instance_obj.name}! What wildly {weather_pattern} weather we're having, right?!"

say_hello_and_weather(the_snail, 'overcast')
# Output
"""
"Hi, my name is the Snail! What wildly overcast weather we're having, right?!"
"""

# passing the method to our class
class Person():

    def say_hello_and_weather(self, weather_pattern):
        # we are using self instead of instance_obj because we know self represents the instance object
        return f"Hi, my name is {self.name}! What wildly {weather_pattern} weather we're having, right?!"

the_snail = Person()
the_snail.name = 'the Snail'
print('1. ', the_snail.say_hello_and_weather('humid'))
# notice that we are ONLY passing in the weather pattern argument
# instance methods **implicitly** pass in the instance object as the **first** argument


#example 2
class Person():

    def happy_birthday(self):
        self.age += 1
        return f"Happy Birthday to {self.name} (aka ME)! Can't believe I'm {self.age}?!"

#creating an instance object
the_snail = Person()
#setting the instance object's attributes
the_snail.name = 'the Snail'
the_snail.age = 29
print('1. ', the_snail.age)
print('2. ', the_snail.happy_birthday())
print('3. ', the_snail.age)

# Output
"""
1.  29
2.  Happy Birthday to the Snail (aka ME)! Can't believe I'm 30?!
3. 30
"""

#conditions in classes
class Person:
    #define method for hungry and not hungry 
    def eat_breakfast(self):
        #if hungry is true
        if(self.hungry):
            self.relieve_hunger()
            return 'Yum that was delish!'
        #if hungry is false
        else:
            return 'I am not hungry, thanks!'
        
    def relieve_hunger(self):
        #if hungry is true
        print("Hunger is being relieved")
        self.hungry = False

#instanciate the class
gail = Person()
gail.name = 'Gail'
gail.hungry = True
print('1. ', gail.hungry)
print('2. ', gail.eat_breakfast())
print('3. ', gail.hungry)
print('4. ', gail.eat_breakfast())


# Output
"""
1.  True
Hunger is being relieved
2.  Yum that was delish!
3.  False
4. I am not hungry, thanks!
"""