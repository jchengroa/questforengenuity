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
    pass

def help_section():
    art()
    print("\n\n", "Help Section".center(65))
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
            print("\nStarting a new adventure...\n")
            input("Press Any Key to Continue...")
            level_selector()
        elif choice == "2":
            os.system('cls')
            print("\nEntering Help Menu...\n")
            input("Press Any Key to Continue...")
        elif choice == "3":
            os.system('cls')
            print("\nExiting game. See you next time!\n")
            break
        else:
            invalidinput = True

if __name__ == "__main__":
    main()
    
