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

Version: 0.6 (March 28, 2025) - Cheng Roa
> Added Chem Level
> Added confirmation before exit
> Completed help menu
> Aligned menu based on terminal size instead of static
> Optimization: Removed unnecessary variables and conditions

Version: 0.6.1 (March 28, 2025) - Hotfix
> Fixed bug that causes term_width to crash the program
> Fixed inconsistent texts
> Added Story Mode Option for Later

Version: 0.6.2 (March 29, 2025) - Small Update
> Added Parts of Storymode
> Fixed functions to work with storymode
> Removed uneccessary variables and functions

"""

# Import System Files
import os
import statistics
import time
import random

# Global Variables
try:
    term_width = os.get_terminal_size().columns
except Exception:
    term_width = 65

# General Functions
def art():
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
    print("")
    print(r"     \_\           ___                  _      __                  ".center(term_width))
    print(r"    (_**)         / _ \ _   _  ___  ___| |_   / _| ___  _ __       ".center(term_width))
    print(r"   __) #_        | | | | | | |/ _ \/ __| __| | |_ / _ \| '__|      ".center(term_width))
    print(r"  ( )...()       | |_| | |_| |  __/\__ \ |_  |  _| (_) | |         ".center(term_width))
    print(r"  || | |I|        \__\_\\__,_|\___||___/\__| |_|  \___/|_|       _ ".center(term_width))
    print(r"  || | |()__/    | ____|_ __   __ _  ___ _ __  _   _(_) |_ _   _| |".center(term_width))
    print(r"  /\(___)        |  _| | '_ \ / _` |/ _ \ '_ \| | | | | __| | | | |".center(term_width))
    print(r" _-*******-_---_ | |___| | | | (_| |  __/ | | | |_| | | |_| |_| |_|".center(term_width))
    print(r" -,,,,,,,,- ,,-  |_____|_| |_|\__, |\___|_| |_|\__,_|_|\__|\__, (_)".center(term_width))
    print(r"                             |___/                        |___/   ".center(term_width))

def menubox(selector):
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
        
    if selector == 1:
        print(r"+----------------------------------------+".center(term_width))
        print(f"|{"(1)  Play Game":^40}|".center(term_width))
        print(f"|{"(2)  Level Selector":^40}|".center(term_width))
        print(f"|{"(3)  Help":^40}|".center(term_width))
        print(f"|{"(4)  Exit":^40}|".center(term_width))
        print(r"+----------------------------------------+".center(term_width))
    elif selector == 2:
        print(r"Choose Your Learning Path:".center(term_width))
        print(r"+--------------------------------------+".center(term_width))
        print(r"|           (1)  Mathematics           |".center(term_width))
        print(r"|           (2)  Chemistry             |".center(term_width))
        print(r"|           (3)  Statistics            |".center(term_width))
        print(r"|        Press Enter To Go Back        |".center(term_width))
        print(r"+--------------------------------------+".center(term_width))

def level_selector():
    os.system('cls')
    
    art()
    print("\n")
    menubox(2)

    choice = input(">>  ")

    if choice == '1':
        os.system('cls')
        level_mathematics()
    elif choice == '2':
        os.system('cls')
        level_chemistry()
    elif choice == '3':
        os.system('cls')
        level_statistics()
    else:
        return 0

def help_section():
    
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65

    art()
    print("\n\n", "Help Section".center(term_width))
    print(
    """
    Brick by Brick: Mason's Quest
    > 1) Mathematics Level
         Objective: Solve mathematical challenges
         Topics Involved: Algebra, Differentiation (Rates of Change), Matrices
        
         In the challenges, your answer must strictly be an integer. e.g. 24
         (Decimals are not allowed in this level)
         
         Do not input units.

    Gold & Glory: Treasurer's Dilemma
    > 2) Chemistry Level
         Objective: Identify amount of atoms and find the balanced equation
         Topics Involved: Balancing Chemical Equation

         In identifying amount of atoms and balancing, your answer must strictly be an integer. e.g. 3
         (Decimals are not allowed in this level)
         The maximum answer in this level is only up to 3.

         In balancing, if the compounds don't need to changed, input the integer 1
         (Decimals are not allowed in this level)

         Do not input anything else

    Elixers & Enchantments: The Witch's Apprentice
    > 3) Statistics Level
         Objective: Find the Mean, Median, and Mode of the following list of numbers
         Topics Involved: Measures of Central Tendency

         If there is no mode input \"N/A\"
         
         Decimals are allowed in this level, but only input numerical numbers
         Enter the precise answer in each measures, calculator level of accuracy.

         Do not input anything else
    """)
    input("Press Enter to Go Back...")

# Story Mode Function
def story_mode():
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
    os.system('cls')
    print("The Kingdom of Numeria is thriving, ruled by a powerful but exacting king.\n\n")
    print(r"""
   /\                                                        /\
  |  |                                                      |  |
 /----\                                                    /----\
[______]                                                  [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\|     |             |
  \  []        |     |    /'    ||    '\    |     |        []  /
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''\
[_____________[_______]--'------''------'--[_______]_____________]
""".center(term_width))
    input("Press Enter to Continue")
    os.system('cls')
    print("You, the Royal Mason, have long served under his command, ensuring the kingdom’s structures remain strong.\n\n")
    print(r"""
      __      _
     /__\__  //
    //_____\///
   _| /-_-\)|/_
  (___\ _ //___\
  (  |\\_/// * \\
   \_| \_((*   *))
   ( |__|_\\  *//
   (o/  _  \_*_/
   //\__|__/\
  // |  | |  |
 //  _\ | |___)
//  (___|
""".center(term_width))
    input("Press Enter to Continue")
    os.system('cls')
    print("The king demands that a tower of wisdom and power be built, one that will stand the test of time.")
    print(r"""
             _,._
           ,'   ,`-.
|.        /     |\  `.
\ \      (  ,-,-` ). `-._ __
 \ \      \|\,'     `\  /'  `\
  \ \      ` |, ,  /  \ \     \
   \ \         `,_/`, /\,`-.__/`.
    \ \            | ` /    /    `-._
     \\\           `-/'    /         `-.
      \\`/ _______,-/_   /'             \
     ---'`|       |`  ),' `---.  ,       |
      \..-`--..___|_,/          /       /
                 |    |`,-,...,/      ,'     
                 \    | |_|   /     ,' __  r-'',
                  |___|/  |, /  __ /-''  `'`)  |  
               _,-'   ||__\ /,-' /     _,.--|  (
            .-'       )   `(_   / _,.-'  ,-' _,/
             `-------'       `--''       `'''
""".center(term_width))
    input("Press Enter to Continue")
    os.system('cls')
    print("The King orders you to ensure that the tower’s foundation is mathematically sound.")
    print(r"""
                                                |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       \,/
                                             ||: , |            /`\
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~
""".center(term_width))
    os.system("cls")
    level_mathematics(storymode = True)
    os.system("cls")
    level_chemistry(storymode = True)
    os.system('cls')
    print("The King leads you deep into the Royal Gold Vaults, where mountains of wealth are stored.")
    print(r"""
                    .
                   / \
                  _\ /_
        .     .  (,'v`.)  .     .
        \)   ( )  ,' `.  ( )   (/
         \`. / `-'     `-' \ ,'/
          : '    _______    ' :
          |  _,-'  ,-.  `-._  |
          |,' ( )__`-'__( ) `.|
          (|,-,'-._   _.-`.-.|)
          /  /<( o)> <( o)>\  \
          :  :     | |     :  :
          |  |     ; :     |  |
          |  |    (.-.)    |  |
          |  |  ,' ___ `.  |  |
          ;  |)/ ,'---'. \(|  :
      _,-/   |/\(       )/\|   \-._
_..--'.-(    |   `-'''-'   |    )-.`--.._
         `.  ;`._________,':  ,'
        ,' `/               \'`.
             `------.------'          
""".center(term_width))
    input("Press Enter to Continue")
    os.system('cls')
    level_statistics()

# Chemistry Level Function - JOHN CARLO
def question_atoms(element, ans, side="reactant"):
    os.system('cls')
    print("\n🧉 **Gold & Glory: The Treasurer's Ultimate Dilemma** 🧈")
    print("\nYour task is to balance these chemicals perfectly to ensure the potion succeeds.\n\n\n")
    
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
    
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width))
    print(r"| The witch puts in Sodium Carbonate (Na2CO3) and Hydrochloric Acid (HCl) into the cauldron |".center(term_width))
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width))
    print(r"| It resulted in Sodium Chloride (NaCl), Water (H2O), and Carbon Dioxide Gas (CO2)          |".center(term_width))
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width)+"\n\n")
    answer = input(f"Identify the number of atoms of {element} from the {side} side:\n>> ")
    if answer == ans:
        print("\n✅ Correct!")
        time.sleep(1)
        return 1
    else:
        print("\n❌ Incorrect! Try again.")
        time.sleep(1)
        return 0

def balancing_table():
    os.system('cls')
    print("\n🧉 **Gold & Glory: The Treasurer's Ultimate Dilemma** 🧈")
    print("\nYour task is to balance these chemicals perfectly to ensure the potion succeeds.\n\n\n")
    
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
        
    print(r"+------------------------------------------------------+".center(term_width))
    print(r"| Unbalanced Equation: Na2Co3 + HCl → NaCl + H2O + CO2 |".center(term_width))
    print(r"+------------------------------------------------------+".center(term_width))

    print(r"+---------------+-----------+----------+".center(term_width))
    print(r"|    Element    | Reactants | Products |".center(term_width))
    print(r"+---------------+-----------+----------+".center(term_width))
    print(r"| Na (Sodium)   |         2 |        1 |".center(term_width))
    print(r"| C (Carbon)    |         1 |        1 |".center(term_width))
    print(r"| O (Oxygen)    |         3 |        3 |".center(term_width))
    print(r"| H (Hydrogen)  |         1 |        2 |".center(term_width))
    print(r"| Cl (Chlorine) |         1 |        1 |".center(term_width))
    print(r"+---------------+-----------+----------+".center(term_width))

def level_chemistry(storymode = "False"):
    # Back Story
    if storymode == True:
        print("As you enter the Witch’s lair, the air smelt of the scent of herbs…\n")
        time.sleep(1)
        print("You see a cauldron bubbling…\n")
        time.sleep(1)
        print("You hear a faint crackling sound of whooshes and sparkles.\n\n\n")
        time.sleep(2)
        print("Through the dark, eerie night, you see shelves lined with vials…\n")
        time.sleep(1)
        print("At last! You saw the kingdom’s top witch…\n\n\n")

        print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣼⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢣⣿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡼⠏⣼⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⢹⣿⢻⣿⣿⣿⣦⣄⠀
    ⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⣸⠟⠛⠿⠶⢾⣿⣿⣿⣿⡿⠗
    ⠘⢿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣿⠐⡀⠀⠰⠘⣿⣿⣿⣿⡄⠀
    ⠀⠀⠈⠉⠛⠻⠿⣶⣶⠄⢸⣿⣧⣄⣀⠀⢀⣿⣿⣿⣿⡇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⢞⣿⣿⣿⣧⣾⣶⣿⣿⣿⠿⠟⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⡿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣼⢄⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠧⠈⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⠉⠀⠀⠀⠀
    """)

        input("\n\nPress Enter to Continue")
        os.system('cls')

        time.sleep(2)
        print("She turns to you, eyes gleaming with curiosity…\n")
        time.sleep(1)
        print("“Ah, just in time!” – The witch said…\n")
        time.sleep(1)
        print("\"I require assistance to perfect my latest creation\"" + "\n")
        time.sleep(1)
        print("\"I need your brain power to help me balance the chemicals I’m gonna use.\""+"\n\n\n")
        time.sleep(2)
        print("You have no choice but to comply, as she said she would turn you into a spoon if you don’t comply…\n")
        time.sleep(1)
        print("The King had told you, before you left, to comply to the witch when you are being threathened…")

        input("\n\nPress Enter to Continue")
    
    # Identify Number of Atoms - Challenge 1
    while True:
        question_1 = question_atoms("Sodium (Na)", "2")
        if question_1 == 1:
            break
        else: 
            continue
    while True:
        question_2 = question_atoms("Carbon (C)", "1")
        if question_2 == 1:
            break
        else: 
            continue
    while True:
        question_3 = question_atoms("Oxygen (O)", "3")
        if question_3 == 1:
            break
        else: 
            continue
    while True:
        question_4 = question_atoms("Hydrogen (H)", "1")
        if question_4 == 1:
            break
        else: 
            continue
    while True:
        question_5 = question_atoms("Chlorine (Cl)", "1")
        if question_5 == 1:
            break
        else: 
            continue
    while True:
        question_6 = question_atoms("Sodium (Na)", "1", side="product")
        if question_6 == 1:
            break
        else: 
            continue
    while True:
        question_7 = question_atoms("Carbon (C)", "1", side="product")
        if question_7 == 1:
            break
        else: 
            continue
    while True:
        question_8 = question_atoms("Oxygen (O)", "3", side="product")
        if question_8 == 1:
            break
        else: 
            continue
    while True:
        question_9 = question_atoms("Hydrogen (H)", "2", side="product")
        if question_9 == 1:
            break
        else: 
            continue
    while True:
        question_10 = question_atoms("Chlorine (Cl)", "1", side="product")
        if question_10 == 1:
            break
        else: 
            continue

    # Balance Equation - Final Challenge
    while True:
        r1 = 0
        r2 = 0
        p1 = 0
        p2 = 0
        p3 = 0
        while True:
            if r1 == 0:
                balancing_table()
                answer_r1 = "\n\nFill the Blanks:\n__ Na2CO3 + HCl → NaCl + H2O + CO2\n>> "
                answer = input(answer_r1)
                try:
                    r1 += int(answer)
                except Exception:
                    print("\nERROR: Please enter an integer!")
                    time.sleep(2)
                    continue

            if r2 == 0:
                balancing_table()
                answer_r2 = f"\n\nFill the Blanks:\n{r1} Na2CO3 + __ HCl → NaCl + H2O + CO2\n>> "
                answer = input(answer_r2)
                try:
                    r2 += int(answer)
                except Exception:
                    print("\nERROR: Please enter an integer!")
                    time.sleep(2)
                    continue

            if p1 == 0:
                balancing_table()
                answer_p1 = f"\n\nFill the Blanks:\n{r1} Na2CO3 + {r2} HCl → __ NaCl + H2O + CO2\n>> "
                answer = input(answer_p1)
                try:
                    p1 += int(answer)
                except Exception:
                    print("\nERROR: Please enter an integer!")
                    time.sleep(2)
                    continue

            if p2 == 0:
                balancing_table()
                answer_p2 = f"\n\nFill the Blanks:\n{r1} Na2CO3 + {r2}HCl → {p1} NaCl + __ H2O + CO2\n>> "
                answer = input(answer_p2)
                try:
                    p2 += int(answer)
                except Exception:
                    print("\nERROR: Please enter an integer!")
                    time.sleep(2)
                    continue

            if p3 == 0:
                balancing_table()
                answer_p3 = f"\n\nFill the Blanks:\n{r1} Na2CO3 + {r2} HCl → {p1} NaCl + {p2} H2O + __ CO2\n>> "
                answer = input(answer_p3)
                try:
                    p3 += int(answer)
                except Exception:
                    print("\nERROR: Please enter an integer!")
                    time.sleep(2)
                    continue

            if r1 > 0 and r2 > 0 and p1 > 0 and p2 > 0 and p3 > 0:
                result = f"{r1} Na2CO3 + {r2} HCl → {p1} NaCl + {p2} H2O + {p3} CO2"
                break
    
        if result == "1 Na2CO3 + 2 HCl → 2 NaCl + 1 H2O + 1 CO2":
            print("\n✅ Correct!")
            time.sleep(2)
            break
        else:
            print("\n❌ Incorrect! Try again.")
            time.sleep(2)
            continue

    # Result
    os.system('cls')
    print("Your Answer was: " + result + "\n\n")
    print("\n🎉 Congratulations, Mason! You have successfully balanced her potion! 🧪\n")
    time.sleep(2)
    if storymode == False:
        input("Press Enter to go back to the main menu")

# Mathematics Level Function - YVAN
def level_mathematics(storymode = False):
    if storymode == False:
        print("\n🏰 **Brick by Brick: The Castle Mason’s Quest** 🏰")
        print("\nThe King has ordered a grand tower to be built, and as the royal mason, you must ensure its strength and stability!")
        print("You will need to solve mathematical challenges to proceed.\n")

    # Challenge 1: Algebra - Calculating the height of the tower
    time.sleep(1)
    print("\n🧱 **Challenge 1: Algebra - Tower Height Calculation** 🧱")
    print("The King wants the tower to be 5 times as tall as the castle gate (which is 12 meters).")
    
    time.sleep(1)
    while True:
        answer = input("How tall should the tower be? (in meters): ")
        if answer.strip() == "60":
            print("✅ Correct! The tower will stand at 60 meters tall.")
            time.sleep(1)
            break
        else:
            print("❌ Incorrect! Try again.")
            time.sleep(1)

    # Challenge 2: Differentiation - Rate of brick stacking
    print("\n📐 **Challenge 2: Differentiation - Speed of Construction** 📐")
    print("The workers stack bricks at a rate of f(x) = 3x^2 + 2x - 5 bricks per hour.")
    print("Find the rate of stacking at x = 4 hours.")

    while True:
        answer = input("Enter the derivative evaluated at x = 4: ")
        if answer.strip() == "29":
            print("✅ Correct! The workers are stacking bricks at 29 bricks per hour at that moment.")
            time.sleep(1)
            break
        else:
            print("❌ Incorrect! Try again.")
            time.sleep(1)

    # Challenge 3: Matrices - Structural Integrity Check
    print("\n🏗 **Challenge 3: Matrices - Load Distribution** 🏗")
    print("The weight distribution of the tower is represented by matrix A:")
    print("\nA = [ 2  4 ]\n    [ 1  3 ]")
    print("\nFind the determinant of matrix A.")

    while True:
        answer = input("Enter the determinant: ")
        if answer.strip() == "2":
            print("✅ Correct! The determinant is 2, meaning the structure is stable.")
            time.sleep(1)
            break
        else:
            print("❌ Incorrect! Try again.")
            time.sleep(1)

    print("\n🎉 Congratulations, Mason! You have successfully built the tower! 🏰\n")
    time.sleep(2)
    if story_mode == False:
        input("Press Enter to go back to the main menu")

# Statistics Level Function - JUSTINE 
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    return statistics.median(numbers)

def mode(numbers):
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "N/A"

def level_statistics():
    print("\n🪄 **Elixers & Enchantments: The Witch's Apprentice** ✨")
    print("Welcome to the GOLD MINE! The King wants you to compute the mean, median, and mode of a list of all the gold in the kingdom.")
    time.sleep(2)
    print(f"Find the Mean, Median, and Mode of the following list of numbers to prove your worth to the king, If there is no mode input \"N/A\".")
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
        print("\n🎉 Congratulations, Mason! your computations are correct and the king has found you useful. Your life is spared! 🏰\n")
        time.sleep(2)
        input("Press Enter to go back to the main menu")
    else:
        print("Your answers are incorrect. The king has no use for you.")
        time.sleep(2)
        input("Press Enter to go back to the main menu")

# Main Function
def main():

    invalidinput = False

    while True:
        os.system('cls')

        art()
        print("\n")
        menubox(1)

        if invalidinput == True:
            print("\nInvalid choice. Please try again.")

        choice = input(">>  ")

        if choice == "1":
            invalidinput = True
            story_mode()
        if choice == "2":
            invalidinput = False
            os.system('cls')
            level_selector()
        elif choice == "3":
            invalidinput = False
            os.system('cls')
            help_section()
        elif choice == "4":
            invalidinput = False
            os.system('cls')
            confirmation = input("\nAre you sure?\nType 'Yes' to exit\n\n>> ")
            if confirmation == "Yes":
                os.system('cls')
                time.sleep(1)
                print("\nExiting game. See you next time!\n")
                time.sleep(1)
                break
            else:
                continue
        else:
            invalidinput = True

if __name__ == "__main__":
    main()
    
