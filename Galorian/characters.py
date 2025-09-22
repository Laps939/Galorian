import random

class Player:
    def __init__(self, name, character_class_id, race, level, hit_points=0, max_hit_points=0, mp=0, max_mp=0, stamina=0,
                 max_stamina=0, weapon=None, armor=None, gold=0, items=[], experience=0):
        self.name = name
        self.character_class_id = character_class_id
        self.race = race
        self.level = level
        self.hit_points = hit_points
        self.max_hit_points = max_hit_points
        self.mp = mp
        self.max_mp = max_mp
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.weapon = weapon
        self.armor = armor
        self.gold = gold
        self.items = items
        self.experience = experience

def heal (self, amount):
    healed_amount = min(amount, self.max_hit_points - self.hit_poits)
    self.hit_points += healed_amount
    return healed_amount

def restore_resources(self):
    self.hit_points = self.max_hit_points
    self.mp = self.max_mp
    self.stamina = self.max_samina
    
    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage and has {self.hit_points} health remaining.")

    def level_up(self):
        level_threshold = 20
        if self.experience >= level_threshold:
            self.level += 1
            self.experience -= level_threshold
            # Note: This line had a bug, it should probably be `level_threshold += 15`
            # self.level_threshold = + 15
            
            print(f"Congratulations! {self.name} has reached level {self.level}!")

            if self.character_class_id in [2, 4, 5]: # MP-based classes
                self.max_hit_points += 15
                self.hit_points = self.max_hit_points
                self.max_mp += 10
                self.mp = self.max_mp
                print(f"Max HP increased by 15, Max MP increased by 10!")

            elif self.character_class_id in [1, 3]: # Stamina-based classes
                self.max_hit_points += 20
                self.hit_points = self.max_hit_points
                self.max_stamina += 10
                self.stamina = self.max_stamina
                print(f"Max HP increased by 20, Max Stamina increased by 10!")

            if self.character_class_id in [2, 4, 5]:
                print(f"{self.name}'s HP: {self.hit_points}/{self.max_hit_points} | MP: {self.mp}/{self.max_mp}")
            else:
                print(f"{self.name}'s HP: {self.hit_points}/{self.max_hit_points} | Stamina: {self.stamina}/{self.max_stamina}")

class Enemy:
    def __init__(self, name, hit_points, damage, damage_range, gold_reward, exp_reward, special_attack_name=None, special_attack_range=None):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.damage_range = damage_range
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward
        self.is_alive = True
        self.special_attack_name = special_attack_name
        self.special_attack_range = special_attack_range

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage and has {self.hit_points} health remaining.")

    def special_attack(self, target):
        if self.is_alive:
            if self.special_attack_name and self.special_attack_range:
                damage = random.randint(self.special_attack_range[0], self.special_attack_range[1])
                print(f"{self.name} uses {self.special_attack_name} for {damage} damage!")
                target.take_damage(damage)
            else:
                print(f"{self.name} has no special attack.")


