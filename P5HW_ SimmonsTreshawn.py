# Treshawn Simmons
# 10/2/2024
# P5HW
# Using AI and functions to create a game

def create_character():
    """
    Create a dictionary representing an alien character.

    Returns:                                           
    dict: A dictionary containing the alien's attributes.
    """
    print()
    alien_character = {
        "alien_name": input("Enter alien name: "),
        "shot_attack": int(input("Enter attack damage: ")),
        "ship_beam": int(input("Enter ship damage: ")),
        "flight_height": int(input("Enter flight height: ")),
        "alien_health": int(input("Enter alien health: ")) 
    }
    
    return alien_character

def display_aliens(char):
    for key, value in char.items() :
        print(f"{key}: {value}")

def simulate_shooting(attacker, target):
    """
    Simulate an alien shooting another alien.

    Parameters:
    attacker (dict): The alien character performing the attack.
    target (dict): The alien character being attacked.

    Returns:
    dict: The updated target alien with reduced health.
    """
    print(f"{attacker['alien_name']} is attacking {target['alien_name']}")
    damage = attacker["shot_attack"]
    target["alien_health"] -= damage
    
    # Ensure health doesn't go below zero
    if target["alien_health"] < 0:
        target["alien_health"] = 0
    
    return attacker, target

def board_ship(aliens):
    """
    Simulate aliens getting on a ship and getting ready to fight.

    Parameters:
    aliens (list): A list of alien characters.

    Returns:
    None
    """
    if not aliens:
        print("No aliens to board the ship.")
        return
    
    print("The following aliens are boarding the ship:")
    for alien in aliens:
        print(f"- {alien['alien_name']}")
    
    print("The aliens are now aboard the ship and ready to fight!")

def fight(aliens):
    """
    Simulate turn-based fighting between two aliens until one is defeated.

    Parameters:
    aliens (list): A list of two alien characters.

    Returns:
    None
    """
    attacker, target = aliens[0], aliens[1]
    
    while attacker["alien_health"] > 0 and target["alien_health"] > 0:
        # Attacker's turn
        updated_attacker, updated_target = simulate_shooting(attacker, target)
        print(f"{updated_target['alien_name']}'s remaining health: {updated_target['alien_health']}\n")

        # Swap roles
        attacker, target = target, updated_target

    if attacker["alien_health"] <= 0:
        print(f"{attacker['alien_name']} has been defeated!")
    else:
        print(f"{target['alien_name']} has been defeated!")

# Example usage:
if __name__ == "__main__":
    # Create 2 characters
    alien1 = create_character()
    alien2 = create_character()
    char_list = []
    char_list.append(alien1)
    char_list.append(alien2)



    # Display the characters before boarding the ship
    print("\nCharacters before boarding the ship:")
    display_aliens(alien1)
    display_aliens(alien2)

    # Simulate aliens boarding the ship
    board_ship(char_list)

    # Display the characters after boarding
    print("\nCharacters ready for battle:")
    display_aliens(alien1)
    display_aliens(alien2)

    fight(char_list)

    # Simulate fighting
    alien1, alien2 = simulate_shooting(alien1, alien2)

    # Add characters to list
    display_aliens(alien1)
    display_aliens(alien2)

   
