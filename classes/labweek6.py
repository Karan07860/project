class Pokemon:
    def __init__(self, name, type, health, level):
        self.name = name
        self.type = type
        self.health = health
        self.level = level
        
    def attack(self):
        print(f"\n{self.name} uses {self.type}attacks!")
        
    def dodge(self):
        print(f"\n{self.name} dodge {self.health} the attack!")
        
    def evolve(self, new_name):
        print(f"\n{self.name} is evolving into {new_name}!")
        self.name = new_name
        
    def level_up(self):
        level_up = 1
        print(f"\n{self.name} levels up to{self.level}!")
        