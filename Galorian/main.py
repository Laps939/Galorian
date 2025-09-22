from characters import Player
from game_data import pathfinder_classes, weapons, armor_types, available_races
from game_logic import town_gameplay

def create_character():
    name = input("Enter your character's name: ")
    print(f"Welcome, {name}!")

    # Display available classes
    print("\nAvailable classes:")
    for key, value in pathfinder_classes.items():
        print(f"{key}. {value['name']}")
    
    class_choice = 0
    while class_choice not in pathfinder_classes:
        try:
            class_choice = int(input("Choose a class number: "))
        except ValueError:
            print("Invalid input! Please choose a valid class number.")

    # Display available races
    print("\nAvailable races:")
    for i, race in enumerate(available_races, 1):
        print(f"{i}. {race}")

    race_choice_idx = -1
    while race_choice_idx < 0 or race_choice_idx >= len(available_races):
        try:
            race_choice_idx = int(input("Choose a race number: ")) - 1
        except ValueError:
            print("Invalid input! Please choose a valid race number.")

    chosen_class_info = pathfinder_classes[class_choice]
    chosen_race = available_races[race_choice_idx]

    # Initialize player stats based on class
    player = Player(
        name=name,
        character_class_id=class_choice,
        race=chosen_race,
        level=1,
        max_hit_points=100,
        hit_points=100,
        max_stamina=50,
        stamina=50,
        max_mp=50,
        mp=50,
        gold=25,
        weapon=weapons[chosen_class_info["starting_weapon"]],
        armor=armor_types[chosen_class_info["starting_armor"]]
    )
    print(f"\nCharacter {player.name}, the {player.race} {chosen_class_info['name']}, has been created!")
    return player

def main():
    print(r"""  ________       .__               .__                ________       .___                                 
 /  _____/  ____ |  | _____ _______|__| ____   ____   \_____  \    __| _/__.__. ______ ______ ____ ___.__.
/   \  ___ /  _ \|  | \__  \\_  __ \  |/  _ \ /    \   /   |   \  / __ <   |  |/  ___//  ___// __ <   |  |
\    \_\  (  <_> )  |__/ __ \|  | \/  (  <_> )   |  \ /    |    \/ /_/ |\___  |\___ \ \___ \\  ___/\___  |
 \______  /\____/|____(____  /__|  |__|\____/|___|  / \_______  /\____ |/ ____/____  >____  >\___  > ____|
        \/                 \/                     \/          \/      \/\/         \/     \/     \/\/     
    """)
    
    # For now, we create one player. You can loop this for multiple players.
    player = create_character()
    
    # Start the game in town
    town_gameplay(player)

if __name__ == "__main__":
    main()
