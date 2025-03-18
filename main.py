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
    print(r"    \_\          ___                  _      __                  ")
    print(r"   (_**)        / _ \ _   _  ___  ___| |_   / _| ___  _ __       ")
    print(r"  __) #_       | | | | | | |/ _ \/ __| __| | |_ / _ \| '__|      ")
    print(r" ( )...()      | |_| | |_| |  __/\__ \ |_  |  _| (_) | |         ")
    print(r" || | |I|       \__\_\\__,_|\___||___/\__| |_|  \___/|_|       _ ")
    print(r" || | |()__/   | ____|_ __   __ _  ___ _ __  _   _(_) |_ _   _| |")
    print(r" /\(___)       |  _| | '_ \ / _` |/ _ \ '_ \| | | | | __| | | | |")
    print(r"_-*******-_""-_| |___| | | | (_| |  __/ | | | |_| | | |_| |_| |_|")
    print(r"-,,,,,,,,- ,,- |_____|_| |_|\__, |\___|_| |_|\__,_|_|\__|\__, (_)")
    print(r"                            |___/                        |___/   ")

def main_menu():
    while True:
        os.system('cls')
        art()
        print("\n\n=== Quest for Enginuity ===".center(65))
        print("1)  Play Game".center(65))
        print("2)  Select Subject".center(65))
        print("3)  Help".center(65))
        print("4)  Exit".center(65))
        choice = input(">>  ")
        if choice == "1":
            os.system('cls')
            print("\nStarting a new adventure...\n")
            return 1
        elif choice == "2":
            os.system('cls')
            print("\nLoading saved game...\n")
        elif choice == "3":
            os.system('cls')
            print("\nEntering Math Challenges...\n")
        elif choice == "4":
            os.system('cls')
            print("\nOpening settings...\n")
        elif choice == "5":
            os.system('cls')
            print("\nExiting game. See you next time!\n")
            break
        else:
            os.system('cls')
            print("\nInvalid choice. Please try again.\n")

# Main Function
def main():
    os.system('cls')
    main_menu()

if __name__ == "__main__":
    main()
    
