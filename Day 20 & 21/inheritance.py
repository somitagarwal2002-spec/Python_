class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale & Exhale")

class Fish(Animal): # calling the other class
    def __init__(self):
        super().__init__() #inheriting all the functions and object of the "Animal" class

    def swim(self):
        print("Can walk under water")

    def breathe(self):
        super().breathe() # modifying to the function that already exist in the parent class jaise
                          # hum isme particular "fish" class ke liye kuch aur add krna ho to
        print("I can breathe under water")

f = Fish()
f.swim()
f.breathe()

