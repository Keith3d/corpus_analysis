class Person():
    name = ""
    age = 0

    def speak(self):
        print("Hi my name is " + self.name)


pete = Person()
pete.name = "Pete"
pete.age = 30

amanda = Person()
amanda.name = "Amanda"
amanda.age = 50

pete.speak()
amanda.speak()
