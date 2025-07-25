import random
from abc import ABC, abstractmethod
# abstract base class

class Character(ABC):
    def __init__(self, name, max_hp, hp, basic_power, special_power, move_speed, attack_range, block_strength):
        self.name = name 
        self.max_hp = max_hp
        self.hp = hp
        self.basic_power = basic_power
        self.special_power = special_power
        self.move_speed = move_speed
        self.attack_range = attack_range
        self.position = position
        self.is_blocking = False
        self.block_strength = block_strength
        self.is_alive = True


    def move(self, direction, spaces = None):
            if direction == "right":
                self.position += spaces
            elif direction == "left":
                self.position -= spaces 

    def take_damage():
        pass

    def block():
        pass 

    @abstractmethod
    def basic_attack(self, target):
        """Each character has an assigned basic attack."""
        pass
    
    @abstractmethod
    def special_attack(self, target):
        """Each character has an assigned special attack"""
        pass



# each character needs functions for basic, special attacks

class Tank(Character):
    def __init__(self):
        super().__init__(
            name="Tank",
            max_hp=150,
            basic_power=15,
            special_power=25,
            move_speed=1,
            attack_range=1,
            block_strength=20
        )

    def basic_attack(self, target):
        return super().basic_attack(target)

class Ranged(Character):
    def __init__(self):
        super().__init__(
            name="Ranged",
            max_hp=80,
            basic_power=20,
            special_power=25,
            move_speed=3,
            attack_range=4,
            block_strength_10
        )

class Balanced(Character):
    def __init__(self):
        super().__init__(
            name="Balanced",
            max_hp=100,
            basic_power=18,
            special_power=25,
            move_speed=2,
            attack_range=2,
            block_strength=15
        )
