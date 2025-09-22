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
    1: {"name": "Fighter", "damage_dice": (1, 8), "defense": 4, "starting_weapon": 2, "starting_armor": 2},
    2: {"name": "Wizard", "damage_dice": (1, 4), "defense": 2, "starting_weapon": 6, "starting_armor": 1},
    3: {"name": "Rogue", "damage_dice": (1, 6), "defense": 3, "starting_weapon": 1, "starting_armor": 2},
    4: {"name": "Cleric", "damage_dice": (1, 4), "defense": 3, "starting_weapon": 3, "starting_armor": 1},
    5: {"name": "Paladin", "damage_dice": (1, 6), "defense": 5, "starting_weapon": 4, "starting_armor": 3}
}

available_races = [
    "Human", "Elf", "Dwarf", "Halfling", "Orc", "Gnome", "Half-Elf", "Half-Orc"
]
