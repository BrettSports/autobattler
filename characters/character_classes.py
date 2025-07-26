import random
from abc import ABC, abstractmethod
# abstract base class

#TODO: I realized way too late after not reviewing main.py that this code uses integers for position
    #whilst main.py uses 
#TODO: We have range checking function, how do we make range matter? Here or in main.py?
#TODO: Redundancy of text- should messages like "{character} has died" be returned from functions here or on main.py?
#TODO: Random module discussion - elements of random- which ones will be handled in which functions
    # Have not yet integrated randomness into attacks
#TODO: Integrate healing
#TODO: Flesh out/individualize basic attacks, integrate randomness on this end or on main.py?
#TODO: Individualize special attacks
#TODO: Could have a function that returns characters stats/attributes for character select/creation screen
#TODO: Helper functions needed for main.py? Discussion for Saturday

#TODO: syntax issues, noted in output. Too tired to figure them out yet.
#TODO: I copy-pasted a testing section suggested by AI, not sure how to use it yet
    # currently is commented out at the bottom of the file

#TODO: Nice to have- refine character stats
#TODO: Nice to have- Add more characters
#TODO: Nice to have- rename characters



class Character(ABC):
    def __init__(self, name, max_hp, hp, basic_power, special_power, move_speed, attack_range, block_strength):
        self.name = name 
        self.max_hp = max_hp
        self.hp = hp
        self.basic_power = basic_power
        self.special_power = special_power
        self.move_speed = move_speed
        self.attack_range = attack_range
        self.position = 0
        self.is_blocking = False
        self.block_strength = block_strength
        self.is_alive = True


    def move(self, direction, spaces = None):
            """Move character on battlefield (0-11)"""
            if spaces is None:
                spaces = self.move_speed
            if direction == "right":
                self.position += min(11, self.position + spaces)
            elif direction == "left":
                self.position -= max(0, self.position - spaces)
            return f"{self.name} moved to position {self.position}"

    def take_damage(self, damage):
        "Apply damage, considering blocking, determine if still alive"
        actual_damage = damage
        if self.is_blocking:
            actual_damage = max(1, damage - self.block_strength)  
            self.is_blocking = False 
            damage_message = f" (blocked {damage - actual_damage} damage)"
        else:
            damage_message = ""
        self.hp = max(0, self.hp - actual_damage)
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            return f"{self.name} takes {actual_damage} damage {damage_message} and has died."
        return f"{self.name} takes {actual_damage} damage{damage_message}! {self.name} has HP remaining: {self.hp}/{self.max_hp}"
        
    def get_distance_to(self, target):
        """Calculate distance to another character for attacks"""
        return abs(self.position - target.position)
    
    def is_in_range(self, target):
        """Check if target is close enough for an attack"""
        return self.get_distance_to(target) <= self.attack_range
    
    #TODO: This seems important. Figure it out later.
    def heal(self, amount):
        """Heal character by increasing HP"""
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        healed = self.hp - old_hp
        return f"{self.name} heals for {healed} HP! HP: {self.hp}/{self.max_hp}"

    def block(self):
        "Put character in blocking state"
        self.is_blocking = True
        return f"{self.name} goes into block mode! (Block strength: {self.block_strength})"

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
            hp=150,
            basic_power=15,
            special_power=25,
            move_speed=1,
            attack_range=1,
            block_strength=20
        )
        self.position = position
        # can put special abilities here later

    #TODO basic_attack and special attack
    def basic_attack(self, target):
        target.take_damage(self.basic_power)

    def special_attack(self, target): #TBD
        target.take_damage(self.special_power)

class Ranged(Character):
    def __init__(self):
        super().__init__(
            name="Ranged",
            max_hp=80,
            hp=80,
            basic_power=20,
            special_power=25,
            move_speed=3,
            attack_range=4,
            block_strength=10
        )
        self.position = position
        # can put special abilities here later

    #TODO basic_attack and special attack
    def basic_attack(self, target):
        target.take_damage(self.basic_power)

    def special_attack(self, target): 
        target.take_damage(self.special_power)

class Balanced(Character):
    def __init__(self):
        super().__init__(
            name="Balanced",
            max_hp=100,
            hp=80,
            basic_power=18,
            special_power=25,
            move_speed=2,
            attack_range=2,
            block_strength=15
        )
        self.position = position
    
    #TODO basic_attack and special attack
    def basic_attack(self, target):
        target.take_damage(self.basic_power)

    def special_attack(self, target): #TBD
        target.take_damage(self.special_power)



# # Testing section suggested by AI [uncomment entire section when ready to test]
# if __name__ == "__main__":
#     print("=== CHARACTER CREATION TEST ===")
#     tank = create_character('tank', 2)
#     ranged = create_character('ranged', 8)
#     balanced = create_character('balanced', 5)
    
#     print(tank)
#     print(ranged)
#     print(balanced)
    
#     print("\n=== COMBAT TEST ===")
#     print(f"Distance between Tank and Ranged: {tank.get_distance_to(ranged)}")
#     print(ranged.basic_attack(tank))
#     print(tank.move("right", 2))
#     print(tank.special_attack(ranged))
#     print(balanced.basic_attack(ranged))
#     print(balanced.basic_attack(ranged))
#     print(balanced.basic_attack(ranged))  # Should trigger combo
    
#     print("\n=== FINAL STATUS ===")
#     print(tank)
#     print(ranged)
#     print(balanced)