import random

class Player:
    def __init__(self, name, character_class_id, race, level, hit_points=0, max_hit_points=0, mp=0, max_mp=0, stamina=0,
                 max_stamina=0, weapon=None, armor=None, gold=0, items=None, experience=0):
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
        self.items = items if items is not None else []
        self.experience = experience

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage and has {self.hit_points} health remaining.")
    
    def heal(self, amount):
        """Heals the player, ensuring HP doesn't exceed max_hit_points."""
        start_hp = self.hit_points
        self.hit_points = min(self.max_hit_points, self.hit_points + amount)
        healed_amount = self.hit_points - start_hp
        print(f"{self.name} recovers {healed_amount} health.")
        return healed_amount

    def restore_resources(self):
        """Fully restores HP, MP, and Stamina. Used for inns."""
        self.hit_points = self.max_hit_points
        self.mp = self.max_mp
        self.stamina = self.max_stamina

    def level_up(self):
        level_threshold = 20 + (self.level * 15)
        if self.experience >= level_threshold:
            self.level += 1
            self.experience -= level_threshold
            print(f"Congratulations! {self.name} has reached level {self.level}! 🎉")

            if self.character_class_id in [2, 4, 5]: # MP-based
                self.max_hit_points += 15
                self.max_mp += 10
                print(f"Max HP increased by 15, Max MP increased by 10!")
            elif self.character_class_id in [1, 3]: # Stamina-based
                self.max_hit_points += 20
                self.max_stamina += 10
                print(f"Max HP increased by 20, Max Stamina increased by 10!")
            
            self.restore_resources() # Fully heal on level up
            print(f"{self.name}'s stats have been fully restored.")

class Enemy:
    def __init__(self, name, hit_points, damage_range, gold_reward, exp_reward, 
                 special_attack_name=None, special_attack_range=None, special_attack_chance=0.5):
        self.name = name
        self.hit_points = hit_points
        self.damage_range = damage_range
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward
        self.special_attack_name = special_attack_name
        self.special_attack_range = special_attack_range
        self.special_attack_chance = special_attack_chance

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage and has {self.hit_points} health remaining.")

    def special_attack(self, target):
        if self.special_attack_name and self.special_attack_range:
            damage = random.randint(*self.special_attack_range)
            print(f"{self.name} uses {self.special_attack_name} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{self.name} has no special attack.")
