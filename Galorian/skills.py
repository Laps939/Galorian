import random
from characters import Player, Enemy
from game_data import pathfinder_classes

def apply_damage(target, damage):
    target.take_damage(damage)

def attack(attacker, target):
    if isinstance(attacker, Player):
        if attacker.weapon and "dice" in attacker.weapon:
            num_dice, dice_faces = attacker.weapon["dice"]
            damage_dealt = sum(random.randint(1, dice_faces) for _ in range(num_dice))
            
            class_id = attacker.character_class_id
            damage_dice = pathfinder_classes[class_id]["damage_dice"]
            class_damage_bonus = random.randint(*damage_dice)
            
            total_damage = damage_dealt + class_damage_bonus
            print(f"{attacker.name} attacks {target.name} for {total_damage} damage!")
            apply_damage(target, total_damage)
        else:
            print(f"{attacker.name} has no weapon!")

    elif isinstance(attacker, Enemy):
        damage_roll = random.randint(*attacker.damage_range)
        print(f"{attacker.name} attacks {target.name} for {damage_roll} damage!")
        apply_damage(target, damage_roll)

def special_attack_stamina(player, enemy):
    if player.character_class_id == 1:
        fighter_special_attack(player, enemy)
    elif player.character_class_id == 3:
        rogue_special_attack(player, enemy)

def special_attack_mp(player, enemy):
    if player.character_class_id == 2:
        wizard_special_attack(player, enemy)
    elif player.character_class_id == 4:
        cleric_special_attack(player, enemy)
    elif player.character_class_id == 5:
        paladin_special_attack(player, enemy)

def fighter_special_attack(player, enemy):
    skill_info = pathfinder_classes[player.character_class_id]["skills"]["whirlwind"]
    if player.stamina >= skill_info["cost"]:
        player.stamina -= skill_info["cost"]
        damage = random.randint(*skill_info["damage_range"])
        print(f"{player.name} performs a {skill_info['name']} for {damage} damage!")
        apply_damage(enemy, damage)
    else:
        print(f"Not enough stamina for {skill_info['name']}.")

def rogue_special_attack(player, enemy):
    skill_info = pathfinder_classes[player.character_class_id]["skills"]["backstab"]
    if player.stamina >= skill_info["cost"]:
        player.stamina -= skill_info["cost"]
        damage = random.randint(*skill_info["damage_range"])
        if random.random() < skill_info["crit_chance"]:
            damage *= 2
            print(f"{player.name}'s {skill_info['name']} is a critical hit for {damage} damage!")
        else:
            print(f"{player.name} performs {skill_info['name']} for {damage} damage!")
        apply_damage(enemy, damage)
    else:
        print(f"Not enough stamina for {skill_info['name']}.")

def wizard_special_attack(player, enemy):
    skill_info = pathfinder_classes[player.character_class_id]["skills"]["fireball"]
    if player.mp >= skill_info["cost"]:
        player.mp -= skill_info["cost"]
        damage = random.randint(*skill_info["damage_range"])
        print(f"{player.name} casts {skill_info['name']} for {damage} damage!")
        apply_damage(enemy, damage)
    else:
        print(f"Not enough MP for {skill_info['name']}.")

def cleric_special_attack(player, enemy):
    skill_info = pathfinder_classes[player.character_class_id]["skills"]["healing_light"]
    if player.mp >= skill_info["cost"]:
        player.mp -= skill_info["cost"]
        heal_amount = random.randint(*skill_info["heal_range"])
        print(f"{player.name} casts {skill_info['name']}.")
        player.heal(heal_amount)
    else:
        print(f"Not enough MP for {skill_info['name']}.")

def paladin_special_attack(player, enemy):
    smite_info = pathfinder_classes[player.character_class_id]["skills"]["smite"]
    cure_info = pathfinder_classes[player.character_class_id]["skills"]["cure_wounds"]
    
    choice = input(f"Choose spell: 1. {smite_info['name']} ({smite_info['cost']} MP) or 2. {cure_info['name']} ({cure_info['cost']} MP): ")
    if choice == '1':
        if player.mp >= smite_info["cost"]:
            player.mp -= smite_info["cost"]
            damage = random.randint(*smite_info["damage_range"])
            print(f"{player.name} casts {smite_info['name']} for {damage} holy damage!")
            apply_damage(enemy, damage)
        else:
            print(f"Not enough MP for {smite_info['name']}.")
    elif choice == '2':
        if player.mp >= cure_info["cost"]:
            player.mp -= cure_info["cost"]
            heal_amount = random.randint(*cure_info["heal_range"])
            print(f"{player.name} casts {cure_info['name']}.")
            player.heal(heal_amount)
        else:
            print(f"Not enough MP for {cure_info['name']}.")
