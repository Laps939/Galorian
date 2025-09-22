weapons = {
    1: {"name": "Short Sword", "dice": (1, 6), "cost": 10},
    2: {"name": "Battleaxe", "dice": (1, 8), "cost": 15},
    3: {"name": "Falchion", "dice": (2, 4), "cost": 1},
    4: {"name": "Dwarven Waraxe", "dice": (1, 10), "cost": 5},
    5: {"name": "Greatsword", "dice": (2, 6), "cost": 20},
    6: {"name": "Enchanted Staff", "dice": (1, 8), "cost": 25},
    7: {"name": "Composite Bow", "dice": (1, 10), "cost": 30},
    8: {"name": "Silver Dagger", "dice": (3, 4), "cost": 28},
    9: {"name": "Hammer of Thunder", "dice": (1, 12), "cost": 35},
    10: {"name": "Poisoned Blade", "dice": (1, 6), "cost": 18},
}

armor_types = {
    1: {"name": "Light Armor", "defense": 2, "cost": 10},
    2: {"name": "Medium Armor", "defense": 4, "cost": 15},
    3: {"name": "Heavy Armor", "defense": 6, "cost": 20},
    4: {"name": "Legendary Armor", "defense": 8, "cost": 25},
    5: {"name": "Dragonhide Armor", "defense": 10, "cost": 30},
    6: {"name": "Arcane Robes", "defense": 6, "cost": 20},
    7: {"name": "Shadow Cloak", "defense": 9, "cost": 28}
}

pathfinder_classes = {
    1: {"name": "Fighter", "damage_dice": (1, 8), "starting_weapon": 2, "starting_armor": 2,
        "skills": {
            "whirlwind": {"name": "Whirlwind Slash", "cost": 20, "damage_range": (25, 35)}
        }},
    2: {"name": "Wizard", "damage_dice": (1, 4), "starting_weapon": 6, "starting_armor": 1,
        "skills": {
            "fireball": {"name": "Fireball", "cost": 25, "damage_range": (15, 20)},
            "ice_lance": {"name": "Ice Lance", "cost": 26, "damage_range": (18, 25)}
        }},
    3: {"name": "Rogue", "damage_dice": (1, 6), "starting_weapon": 1, "starting_armor": 2,
        "skills": {
            "backstab": {"name": "Shadowstep Backstab", "cost": 15, "damage_range": (30, 40), "crit_chance": 0.3}
        }},
    4: {"name": "Cleric", "damage_dice": (1, 4), "starting_weapon": 3, "starting_armor": 1,
        "skills": {
            "healing_light": {"name": "Healing Light", "cost": 10, "heal_range": (15, 20)}
        }},
    5: {"name": "Paladin", "damage_dice": (1, 6), "starting_weapon": 4, "starting_armor": 3,
        "skills": {
            "smite": {"name": "Smite", "cost": 15, "damage_range": (12, 18)},
            "cure_wounds": {"name": "Cure Wounds", "cost": 10, "heal_range": (10, 15)}
        }}
}

available_races = [
    "Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Half-Elf", "Half-Orc"
]

monster_blueprints = {
    "goblin": {
        "name": "Goblin", "hit_points": (10, 15), "damage_range": (2, 4),
        "gold_reward": 10, "exp_reward": 10,
        "special_attack_name": "Goblin Kick", "special_attack_range": (5, 10),
        "special_attack_chance": 0.7
    },
    "orc": {
        "name": "Orc", "hit_points": (15, 20), "damage_range": (4, 6),
        "gold_reward": 20, "exp_reward": 18,
        "special_attack_name": "War Stomp", "special_attack_range": (10, 15),
        "special_attack_chance": 0.7
    },
    "troll": {
        "name": "Troll", "hit_points": (25, 35), "damage_range": (6, 8),
        "gold_reward": 50, "exp_reward": 30,
        "special_attack_name": "Troll Smash", "special_attack_range": (15, 25),
        "special_attack_chance": 0.8
    },
    "dragon": {
        "name": "Dragon", "hit_points": (180, 220), "damage_range": (20, 30),
        "gold_reward": 1000, "exp_reward": 100,
        "special_attack_name": "Fire Breath", "special_attack_range": (30, 50),
        "special_attack_chance": 0.9
    }
}
