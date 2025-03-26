"""
<DOCSTRING>

Quest For Engenuity!
(Dev Ops 3) 
PROLOGI - EQ3

Version: 0.1 (March 7, 2025) - Cheng Roa
> Created Initial File

Version: 0.2 (March 11, 2025) - Chua
> Created Main Menu
> Added Error Handling
> Added User Input

Version: 0.3 (March 18, 2025) - Cheng Roa
> Organized Codespace Layout (Added Main Function)
> Added ASCII ART
> Centered Elements and Changed Cursor
> Added Clear Screen after updates

Version: 0.4 (March 25, 2025) - Chua
> Added Math Level

Version: 0.5 (March 27, 2025) - Lumilan
> Added Stats Level

Version: 0.5.1 (March 27, 2025) - Cheng Roa
> Updated ASCII Art
> Organized Codespace

"""

# Import System Files
import os

# Global Variables

# General Functions
def art():
    print("")
    print(r"     \_\          ___                  _      __                  ")
    print(r"    (_**)        / _ \ _   _  ___  ___| |_   / _| ___  _ __       ")
    print(r"   __) #_       | | | | | | |/ _ \/ __| __| | |_ / _ \| '__|      ")
    print(r"  ( )...()      | |_| | |_| |  __/\__ \ |_  |  _| (_) | |         ")
    print(r"  || | |I|       \__\_\\__,_|\___||___/\__| |_|  \___/|_|       _ ")
    print(r"  || | |()__/   | ____|_ __   __ _  ___ _ __  _   _(_) |_ _   _| |")
    print(r"  /\(___)       |  _| | '_ \ / _` |/ _ \ '_ \| | | | | __| | | | |")
    print(r" _-*******-_""-_| |___| | | | (_| |  __/ | | | |_| | | |_| |_| |_|")
    print(r" -,,,,,,,,- ,,- |_____|_| |_|\__, |\___|_| |_|\__,_|_|\__|\__, (_)")
    print(r"                             |___/                        |___/   ")

def menubox(selector):
    if selector == 1:
        print(r"+----------------------+".center(65))
        print(r"|    (1)  Play Game    |".center(65))
        print(r"|    (2)  Help         |".center(65))
        print(r"|    (3)  Exit         |".center(65))
        print(r"+----------------------+".center(65))
    elif selector == 2:
        print(r"Choose Your Learning Path:".center(65))
        print(r"+--------------------------------------+".center(65))
        print(r"|           (1)  Chemistry             |".center(65))
        print(r"|           (2)  Statistics            |".center(65))
        print(r"|           (3)  Mathematics           |".center(65))
        print(r"|    Press Any Other Key To Go Back    |".center(65))
        print(r"+--------------------------------------+".center(65))

def level_selector():
    os.system('cls')
    
    art()
    print("\n")
    menubox(2)

    choice = input(">>  ")

    if choice == '1':
        os.system('cls')
        level_chemistry()
    elif choice == '2':
        os.system('cls')
        level_statistics()
    elif choice == '3':
        os.system('cls')
        level_mathematics()
    else:
        return 0

def help_section():
    art()
    print("\n\n", "Help Section".center(65))
    print(
    """
    Gold & Glory: Treasurer's Dilemma
    > 1) Chemistry Level

    Elixers & Enchantments: The Witch's Apprentice
    > 2) Statistics Level

    Brick by Brick: Mason's Quest
    > 3) Mathematics Level
    
    """)
    input("Press Any Key To Exit...")

# Chemistry Level Function - JOHN CARLO
def level_chemistry():
    pass

# Mathematics Level Function - YVAN
def level_mathematics():
    print("\n🏰 **Brick by Brick: The Castle Mason’s Quest** 🏰")
    print("\nThe King has ordered a grand tower to be built, and as the royal mason, you must ensure its strength and stability!")
    print("You will need to solve mathematical challenges to proceed.\n")

    # Challenge 1: Algebra - Calculating the height of the tower
    print("\n🧱 **Challenge 1: Algebra - Tower Height Calculation** 🧱")
    print("The King wants the tower to be 5 times as tall as the castle gate (which is 12 meters).")
    
    while True:
        answer = input("How tall should the tower be? (in meters): ")
        if answer.strip() == "60":
            print("✅ Correct! The tower will stand at 60 meters tall.")
            break
        else:
            print("❌ Incorrect! Try again.")

    # Challenge 2: Differentiation - Rate of brick stacking
    print("\n📐 **Challenge 2: Differentiation - Speed of Construction** 📐")
    print("The workers stack bricks at a rate of f(x) = 3x^2 + 2x - 5 bricks per hour.")
    print("Find the rate of stacking at x = 4 hours.")

    while True:
        answer = input("Enter the derivative evaluated at x = 4: ")
        if answer.strip() == "29":
            print("✅ Correct! The workers are stacking bricks at 29 bricks per hour at that moment.")
            break
        else:
            print("❌ Incorrect! Try again.")

    # Challenge 3: Matrices - Structural Integrity Check
    print("\n🏗 **Challenge 3: Matrices - Load Distribution** 🏗")
    print("The weight distribution of the tower is represented by matrix A:")
    print("\nA = [ 2  4 ]\n    [ 1  3 ]")
    print("\nFind the determinant of matrix A.")

    while True:
        answer = input("Enter the determinant: ")
        if answer.strip() == "2":
            print("✅ Correct! The determinant is 2, meaning the structure is stable.")
            break
        else:
            print("❌ Incorrect! Try again.")

    print("\n🎉 Congratulations, Mason! You have successfully built the tower! 🏰")

# Statistics Level Function - JUSTINE 
import statistics
import time
import random

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    return statistics.median(numbers)

def mode(numbers):
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "N/A"

def stats_level():
    print("Welcome to the GOLD MINE the King wants you to compute the mean, median, and mode of a list of all the gold in the kingdom")
    time.sleep(2)
    print(f"Find the Mean, Median, and Mode of the following list of numbers to prove your worth to the king, If there is no mode input \"N/A\" ")
    time.sleep(2)   
    
    numbers = [random.randint(1, 10) for _ in range(10)]
    print(f"\nNumbers: {numbers}")
    
    user_mean = float(input("Enter the mean: "))
    user_median = float(input("Enter the median: "))
    user_mode = float(input("Enter the mode: "))
    
    correct_mean = mean(numbers)
    correct_median = median(numbers)
    correct_mode = mode(numbers)
    
    print("\nResults:")
    print(f"Your mean: {user_mean} (Correct: {correct_mean})")
    print(f"Your median: {user_median} (Correct: {correct_median})")
    print(f"Your mode: {user_mode} (Correct: {correct_mode})")
    
    if user_mean == correct_mean and user_median == correct_median and user_mode == correct_mode:
        print("Congratulations your computations are correct and the king has found you useful. Your life is spared!")
    else:
        print("Your answers are incorrect. The king has no use for you.")

# Main Function
def main():

    invalidinput = False
    borderdraw = "-"*18

    while True:
        os.system('cls')

        art()
        print("\n")
        menubox(1)

        if invalidinput == True:
            print("\nInvalid choice. Please try again.")

        choice = input(">>  ")

        if choice == "1":
            os.system('cls')
            level_selector()
        elif choice == "2":
            os.system('cls')
            help_section()
        elif choice == "3":
            os.system('cls')
            print("\nExiting game. See you next time!\n")
            break
        else:
            invalidinput = True

if __name__ == "__main__":
    main()
    
