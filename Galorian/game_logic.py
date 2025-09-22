import random
from characters import Enemy, Player
from skills import attack, special_attack_stamina, special_attack_mp
from game_data import weapons, armor_types, monster_blueprints

def create_monster(blueprint_key):
    """Creates an Enemy instance from a blueprint dictionary."""
    blueprint = monster_blueprints[blueprint_key]
    hp = random.randint(*blueprint["hit_points"])

    return Enemy(
        name=blueprint["name"],
        hit_points=hp,
        damage_range=blueprint["damage_range"],
        gold_reward=blueprint["gold_reward"],
        exp_reward=blueprint["exp_reward"],
        special_attack_name=blueprint["special_attack_name"],
        special_attack_range=blueprint["special_attack_range"],
        special_attack_chance=blueprint["special_attack_chance"]
    )

def print_inventory(player):
    print(f"\n--- Character: {player.name} the {player.race} ---")
    print(f"Level: {player.level} | EXP: {player.experience}")
    print(f"HP: {player.hit_points}/{player.max_hit_points}")
    if player.character_class_id in [1, 3]:
        print(f"Stamina: {player.stamina}/{player.max_stamina}")
    else:
        print(f"MP: {player.mp}/{player.max_mp}")
    print(f"Gold: {player.gold}")
    print(f"Weapon: {player.weapon['name'] if player.weapon else 'None'}")
    print(f"Armor: {player.armor['name'] if player.armor else 'None'}")
    print("----------------------------------\n")

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.hit_points > 0 and enemy.hit_points > 0:
        print(f"\n{player.name}: {player.hit_points}/{player.max_hit_points} HP  |  {enemy.name}: {enemy.hit_points} HP")
        
        action = input("Choose: 1. Attack, 2. Special, 3. Inventory, 4. Run: ")
        if action == '1':
            attack(player, enemy)
        elif action == '2':
            if player.character_class_id in [1, 3]: special_attack_stamina(player, enemy)
            else: special_attack_mp(player, enemy)
        elif action == '3':
            print_inventory(player)
            continue
        elif action == '4':
            print("You flee from the battle!")
            return False
        else:
            print("Invalid choice!")
            continue

        if enemy.hit_points > 0:
            if random.random() < enemy.special_attack_chance:
                 enemy.special_attack(player)
            else:
                 attack(enemy, player)
        
        if player.hit_points <= 0:
            print("You have been defeated.")
            return False

    if enemy.hit_points <= 0:
        player.gold += enemy.gold_reward
        player.experience += enemy.exp_reward
        print(f"You defeated the {enemy.name} and gained {enemy.gold_reward} gold and {enemy.exp_reward} EXP!")
        player.level_up()
        return True

def inn_rest(player):
    print("You rest at the inn. Your health and resources have been fully restored!")
    player.restore_resources()

def visit_shop(player):
    # ... (shop logic can remain largely the same) ...
    print("Welcome to the shop! (Shop logic placeholder)")

def adventure_gameplay(player):
    location_monsters = {
        "Forest": ["goblin"],
        "Caves": ["orc"],
        "Ruins": ["troll"],
        "Mountain Pass": ["dragon"]
    }
    locations = list(location_monsters.keys()) + ["Go To Town"]

    while True:
        print("\nWhere do you want to go?")
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")
        
        try:
            choice = int(input("Enter your choice: "))
            location_name = locations[choice - 1]

            if location_name == "Go To Town":
                print("Returning to town...")
                break
            
            print(f"\nYou venture into the {location_name}...")
            monster_key = random.choice(location_monsters[location_name])
            current_enemy = create_monster(monster_key)
            
            if not battle(player, current_enemy):
                print("You limp back to town to recover.")
                break
            elif location_name == "Mountain Pass":
                 print("🏆 Congratulations! You have defeated the Dragon and won the game! 🏆")
                 exit()
        except (ValueError, IndexError):
            print("Invalid choice.")

def town_gameplay(player):
    print(f"\nWelcome to town, {player.name}!")
    while True:
        print("\n--- Town Menu ---")
        choice = input("1. Adventure, 2. Shop, 3. Inn, 4. Character Info: ")
        if choice == '1':
            adventure_gameplay(player)
        elif choice == '2':
            visit_shop(player)
        elif choice == '3':
            inn_rest(player)
        elif choice == '4':
            print_inventory(player)
        else:
            print("Invalid choice.")
