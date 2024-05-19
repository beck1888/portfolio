import os
import time
import datetime

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_to_buy(item, cost, point_penalty, money, points):
    """Process purchase decisions and update money and points."""
    choice = input(f"Do you want to buy {item} for ${cost}? ")
    if choice.lower() == 'y':
        money -= cost
        print(f"UPDATE: {item} added to cart")
    else:
        points -= point_penalty
        print(f"UPDATE: {item} skipped")
    return money, points

def game_over(reason):
    """Display game over message and exit."""
    print("\n" * 10)  # Create space to show game over
    print(f"GAME OVER: {reason}.")
    exit()

def update_points(subtract, points):
    """Update points and check if the game should end."""
    points -= subtract
    if points < 0:
        game_over("You've run out of points!")
    return points

def update_money(subtraction, money):
    """Update money and check if the game should end."""
    money -= subtraction
    if money < 0:
        game_over("You've run out of money!")
    return money

def trick_question(question, game_over_note, update_when_no):
    """Ask the player a trick question and handle their response."""
    user_choice = input(f"{question}")
    if user_choice.lower() == 'y':
        clear_console()
        game_over(game_over_note)
    else:
        print(update_when_no)

def validate_age_input(age):
    """Validate the age input as an integer."""
    if age.isdigit():
        return True, int(age)
    else:
        print("ERROR: Please enter your age as an integer")
        return False, 0

def main():
    """Main function to run the game logic."""
    money = 50
    points = 10
    age_input = input("Please enter your age: ")
    valid_age, age = validate_age_input(age_input)
    if not valid_age:
        return

    print("Welcome to the game!")

    # Sample gameplay logic - replace or extend with your actual game functions and logic
    money, points = ask_to_buy("Magic Wand", 30, 5, money, points)
    points = update_points(3, points)
    money = update_money(5, money)
    trick_question("Is it sunny outside? (y/n)", "It's too sunny to play!", "Good, let's play!")

if __name__ == "__main__":
    main()
