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

"""


# Import System Files
import os

# Global Variables

# Functions
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

def level_selector():

    os.system('cls')
    
    art()
    
    print("\n")
    print("Choose Your Learning Path:".center(65)) 
    print("\n")
    print("1) Chemistry  ".center(65)) 
    print("2) Statistics ".center(65)) 
    print("3) Mathematics".center(65)) 
    print("(Press Any Other Key to go back)".center(65))
    print("\n\n")

    choice = input(">>  ")

    if choice == '1':
        print("\nLoading Gold & Glory: Treasurer's Dilemma...\n")
        input("Press Any Key to Continue...")
        level_chemistry()
    elif choice == '2':
        print("\nLoading Elixers & Enchantments: The Witch's Apprentice...\n")
        input("Press Any Key to Continue...")
        level_statistics()
    elif choice == '3':
        print("\nLoading Brick by Brick: Mason's Quest...\n")
        input("Press Any Key to Continue...")
        level_mathematics()
    else:
        return 0

def level_chemistry():
    pass

def level_statistics():
    pass

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

# Main Function
def main():

    invalidinput = False
    borderdraw = "-"*18

    while True:
        os.system('cls')

        art()

        print("\n")
        print(borderdraw.center(65))
        print("1)  Play Game     ".center(65))
        print("2)  Help          ".center(65))
        print("3)  Exit          ".center(65))
        print(borderdraw.center(65))

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
    
