import random
from characters import Enemy
from skills import attack, special_attack_stamina, special_attack_mp
from game_data import weapons, armor_types

def print_inventory(player):
    print(f"\n--- Inventory for {player.name} ---")
    print(f"Gold: {player.gold}")
    print(f"Weapon: {player.weapon['name'] if player.weapon else 'None'}")
    print(f"Armor: {player.armor['name'] if player.armor else 'None'}")
    print("Items:")
    if not player.items:
        print("- Empty")
    else:
        for item in player.items:
            print(f"- {item}")
    print("------------------------\n")

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.hit_points > 0 and enemy.hit_points > 0:
        print(f"\n{player.name}: {player.hit_points}/{player.max_hit_points} HP")
        print(f"{enemy.name}: {enemy.hit_points} HP\n")
        
        print("Choose your action:")
        print("1. Attack")
        if player.character_class_id in [1, 3]: # Stamina users
            print("2. Special Attack")
        elif player.character_class_id in [2, 4, 5]: # MP users
            print("2. Magic")
        print("3. Inventory")
        print("4. Run")
        
        player_action = input("Enter your choice: ")

        if player_action == '1':
            attack(player, enemy)
        elif player_action == '2':
            if player.character_class_id in [1, 3]:
                special_attack_stamina(player, enemy)
            else:
                special_attack_mp(player, enemy)
        elif player_action == '3':
            print_inventory(player)
            continue # Skip enemy turn after checking inventory
        elif player_action == '4':
            print("You flee from the battle!")
            return False # Battle lost
        else:
            print("Invalid input! Try again.")
            continue

        # Enemy's turn
        if enemy.hit_points > 0:
            if random.random() < 0.7: # 70% chance for special attack
                 enemy.special_attack(player)
            else:
                 attack(enemy, player)
        
        if player.hit_points <= 0:
            print("Game over! You were defeated.")
            return False

    if enemy.hit_points <= 0:
        player.gold += enemy.gold_reward
        player.experience += enemy.exp_reward
        print(f"You defeated the {enemy.name} and gained {enemy.gold_reward} gold and {enemy.exp_reward} EXP!")
        player.level_up()
        return True # Battle won

def inn_rest(player):
    print("You rest at the inn. Your health and resources have been fully restored!")
    player.restore_resources() # Much cleaner!

def visit_shop(player):
    print("Welcome to the shop!")
    while True:
        print("\n1. Buy Weapon")
        print("2. Buy Armor")
        print("3. View Inventory")
        print("4. Leave Shop")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable weapons:")
            for id, data in weapons.items():
                print(f"{id}: {data['name']} ({data['dice'][0]}d{data['dice'][1]}) - {data['cost']} gold")
            
            try:
                weapon_choice = int(input("Enter the weapon number to buy (0 to cancel): "))
                if weapon_choice in weapons:
                    if player.gold >= weapons[weapon_choice]['cost']:
                        player.gold -= weapons[weapon_choice]['cost']
                        player.weapon = weapons[weapon_choice]
                        print(f"You bought the {weapons[weapon_choice]['name']}.")
                    else:
                        print("Not enough gold!")
            except ValueError:
                print("Invalid input.")
        # ... (similar logic for buying armor) ...
        elif choice == '3':
            print_inventory(player)
        elif choice == '4':
            print("Thanks for visiting the shop!")
            break
        else:
            print("Invalid choice!")

def adventure_gameplay(player):
    # Simplified monster generation for this example
    monsters = {
        "Forest": [Enemy("Goblin", 15, 4, (2, 4), 10, 10, "Goblin Kick", (5, 10))],
        "Caves": [Enemy("Orc", 20, 6, (4, 6), 20, 18, "War Stomp", (10, 15))],
        "Ruins": [Enemy("Troll", 30, 8, (6, 8), 50, 30, "Troll Smash", (15, 25))],
        "Mountain Pass": [Enemy("Dragon", 200, 30, (20, 40), 1000, 100, "Fire Breath", (30, 50))]
    }
    locations = list(monsters.keys()) + ["Go To Town"]

    while True:
        print("\nWhere do you want to go?")
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")
        
        try:
            choice = int(input("Enter your choice: "))
            location_name = locations[choice - 1]

            if location_name == "Go To Town":
                print("Returning to town...")
                break # Exit adventure loop to go back to town
            
            print(f"\nYou venture into the {location_name}...")
            enemy_to_fight = random.choice(monsters[location_name])
            # Create a new instance of the enemy for the battle
            current_enemy = Enemy(**enemy_to_fight.__dict__) 
            
            if not battle(player, current_enemy):
                print("You limp back to town to recover.")
                break # Defeated, return to town
            else:
                if location_name == "Mountain Pass":
                     print("Congratulations! You have defeated the Dragon and won the game!")
                     exit() # End the game
        except (ValueError, IndexError):
            print("Invalid choice.")

def town_gameplay(player):
    print(f"\nWelcome to town, {player.name}!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Adventure")
        print("2. Visit Shop")
        print("3. Rest at Inn")
        print("4. View Character")
        choice = input("Enter your choice (1-4): ")

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

