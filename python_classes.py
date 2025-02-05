# #learning classes in python
# class Dog:
#     sound = "bark!" #class attribute

# #create an object from the class
# dog1 = Dog()

# print(Dog.sound)
# print(dog1.sound)

class Dog:
    species = "Canine" #class attribute

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute

    def introduction(self):
        print("My dog's name is " + self.name + " and it's age is " + str(self.age))

#Explanation
'''class Dog: Defines a class named Dog
   species: A class attribute shared by all instances of the class
   __init__ method: Initializes the name and age attributes when a new object is crdated
'''
# dog1 = Dog("Rex", 5)
# print(dog1.age)
# print(dog1.species)

dog1 = Dog("Rex", 3)
dog2 = Dog("Skeleton", 5)

dog2.introduction()


