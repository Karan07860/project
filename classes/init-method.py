class person():
    def __init__(self, name, gender, age):
        self.name = name,
        self.gender = gender,
        self.age = age,
        self.student = True,
        self.pets = ["spot", "stink"]
        self.age.counter = age + 1
        
    #method1: sleep
    def sleep(self):
        print("goodnight!")
        
    #method2: eat
    def eat(self):
        meal = input(f"what will{self.name} eat?:")
        print(f"\nYum! {self.name} has eaten {meal}!")
        
    #method3: work
    def work(self, employed):
        if employed == False:
            print(f"\nWork on your assessment!")
        else:
            print(f"\{self.name} will now go to work!")

#instances           
person_1 = person("Aayush", "Male", 20)
person_2 = person("Mrinalini", "Female", 21)

#calling methods

