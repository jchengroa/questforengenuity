"""
<DOCSTRING>

Quest For Engenuity!
(Dev Ops 3) 
PROLOGI - EQ3

Version: 0.1 (March 7, 2025)
> Created Initial File
"""

def main_menu():
    while True:
        print("\n=== Quest for Enginuity ===")
        print("1. New Game")
        print("2. Continue")
        print("3. Math Challenges")
        print("4. Settings")
        print("5. Quit")
      choice = input("Select an option: ")
  if choice == "1":
            print("\nStarting a new adventure...\n")
        elif choice == "2":
            print("\nLoading saved game...\n")
        elif choice == "3":
            print("\nEntering Math Challenges...\n")
        elif choice == "4":
            print("\nOpening settings...\n")
        elif choice == "5":
            print("\nExiting game. See you next time!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
main_menu()
'''
CHUA UPDATES for now
'''
