# Simple inheritance

## Basic class

###class Animal:
 #   def __init__(self, name):
##        self.name = name

 #   def speak(self):
        #print(f"{self.name} makes a sound.")
## Derived class
##class Dog(Animal):
 #   def speak(self):
       # print(f"{self.name} barks.")

## create an instance of Animal
#animal =Animal("Generic Animal")

#animal.speak()

## Create an instance of Dog class
#dog = Dog("Buddy")
#dog.speak()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed} dog")


animal = Animal("Tommy")
animal.speak()

dog = Dog("Buddy", "Bulldog")
dog.speak()
