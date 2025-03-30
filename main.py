"""
<DOCSTRING>

QUEST FOR ENGENUITY! - NOVEL RPG WITH ENGINEERING SUBJECT CONCEPTS

PROLOGI - EQ3
(Dev Ops 3) 
- Cheng Roa, John Carlo
- Chua, Yvan Dayniel
- Lumilan, Justine

Version: 0.1 (March 7, 2025)
> Created Initial File

Version: 0.2 (March 11, 2025) - Chua
> Created Main Menu
> Added Error Handling
> Added User Input

Version: 0.3 (March 18, 2025) - Cheng Roa + Chua + Lumilan
> Organized Codespace Layout (Added Main Function)
> Added ASCII ART
> Centered Elements and Changed Cursor
> Added Clear Screen after updates

Version: 0.4 (March 25, 2025) - Chua
> Added Math Level

Version: 0.5 (March 27, 2025) - Lumilan
> Added Stats Level

Version: 0.5.1 (March 27, 2025) - Small Update
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

Version: 0.7 (March 30, 2025) - Cheng Roa
> Reworked and completed the storymode structure
> Reworked and completed level selector
> Reworked different levels to work with storymode
> Fixed bugs while adding storymode
> Fixed error in stats level
> Optimization: Organized codespace
> Polished and Ready for Release!

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
        print(r"|                                        |".center(term_width))
        print(f"|{"(1)  Play Game      ":^40}|".center(term_width))
        print(f"|{"(2)  Level Selector ":^40}|".center(term_width))
        print(f"|{"(3)  Help           ":^40}|".center(term_width))
        print(f"|{"(4)  Exit           ":^40}|".center(term_width))
        print(r"|                                        |".center(term_width))
        print(r"+----------------------------------------+".center(term_width))
    elif selector == 2:
        print(r"Select Level:".center(term_width))
        print(r"+--------------------------------------+".center(term_width))
        print(r"|                                      |".center(term_width))
        print(r"|           (1)  Mathematics           |".center(term_width))
        print(r"|           (2)  Chemistry             |".center(term_width))
        print(r"|           (3)  Statistics            |".center(term_width))
        print(r"|                                      |".center(term_width))
        print(r"|        Press Enter To Go Back        |".center(term_width))
        print(r"|                                      |".center(term_width))
        print(r"+--------------------------------------+".center(term_width))

def level_selector():

    os.system('cls')
    
    art()
    print("\n")
    menubox(2)

    choice = input(">>  ")

    if choice == '1': # User Picks Math
        os.system('cls')
        print("\n🏰 **Brick by Brick: The Castle Mason’s Quest** 🏰")
        print("\nThe King has ordered a grand tower to be built, and as the royal mason, you must ensure its strength and stability!")
        print("You will need to solve mathematical challenges to proceed.\n")

        level_mathematics()

        print("\n🎉 Congratulations, Mason! You have successfully built the tower! 🏰\n")

        time.sleep(2)
        input("Press Enter to go back to the main menu")
    elif choice == '2': # User Picks Chem
        os.system('cls')
        print("\n🧉 **Gold & Glory: The Treasurer's Ultimate Dilemma** 🧈")
        print("\nYour task is to balance these chemicals perfectly to ensure the potion succeeds.\n\n\n")

        resultchem = level_chemistry()
        
        print("Your Answer was: " + resultchem + "\n\n")
        print("\n🎉 Congratulations, Mason! You have successfully balanced her potion! 🧪\n")

        time.sleep(2)
        input("Press Enter to go back to the main menu")
    elif choice == '3': # User Picks Stats
        os.system('cls')
        print("\n🪄 **Elixers & Enchantments: The Witch's Apprentice** ✨")
        print("Welcome to the GOLD MINE! The King wants you to compute the mean, median, and mode of a list of all the gold in the kingdom.\n")
        print(f"Find the Mean, Median, and Mode of the following list of numbers to prove your worth to the king, If there is no mode input \"N/A\".")

        resultstats = level_statistics()

        if resultstats == 1:
            print("\n🎉 Congratulations, Mason! your computations are correct and the king has found you useful. Your life is spared! 🏰\n")
        elif resultstats == 0:
            print("\nYour answers are incorrect. The king has no use for you.\n")

        time.sleep(2)
        input("Press Enter to go back to the main menu")
    else: # Returns to Main Menu
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
    
                        Quest for Engenuity!

                        Version: 0.7

                        A PROLOGI Project created by Dev Ops 3
                        - Cheng Roa, John Carlo
                        - Chua, Yvan Dayniel
                        - Lumilan, Justine

                        Presented to Mr. John Vincent P. Cortez
    """)

    input("Press Enter to Go Back...")

# Story Mode Function
def story_mode():

    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65

    # Introduction Story

    os.system('cls')
    print(r"             _,._                               ".center(term_width))
    print(r"           ,'   ,`-.                            ".center(term_width))
    print(r"|.        /     |\  `.                          ".center(term_width))
    print(r"\ \      (  ,-,-` ). `-._ __                    ".center(term_width))
    print(r" \ \      \|\,'     `\  /'  `\                  ".center(term_width))
    print(r"  \ \      ` |, ,  /  \ \     \                 ".center(term_width))
    print(r"   \ \         `,_/`, /\,`-.__/`.               ".center(term_width))
    print(r"    \ \            | ` /    /    `-._           ".center(term_width))
    print(r"     \\\           `-/'    /         `-.        ".center(term_width))
    print(r"      \\`/ _______,-/_   /'             \       ".center(term_width))
    print(r"     ---'`|       |`  ),' `---.  ,       |      ".center(term_width))
    print(r"      \..-`--..___|_,/          /       /       ".center(term_width))
    print(r"                 |    |`,-,...,/      ,'        ".center(term_width))
    print(r"                 \    | |_|   /     ,' __  --'',".center(term_width))
    print(r"                  |___|/  |, /  __ /-''  `'`)  |".center(term_width))
    print(r"               _,-'   ||__\ /,-' /     _,.--|  (".center(term_width))
    print(r"            .-'       )   `(_   / _,.-'  ,-' _,/".center(term_width))
    print(r"             `-------'       `--''       `'''   ".center(term_width))
    print("\n\n")

    equallength = "="*107
    print(equallength.center(term_width))
    print(f"|{"The Kingdom of Numeria is thriving, ruled by a powerful but exacting king.":^105}|".center(term_width))
    print(f"|{"You, the Royal Mason, have long served under his command.":^105}|".center(term_width))
    print(f"|{"Ensuring the kingdom’s governance and peace remain protected and strong.":^105}|".center(term_width))
    print(f"|{"As you bow down to him to reveive his order, You noticed the king furious!":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    # Start of Math Story

    os.system("cls")
    print(r"                                                |>>>                            ".center(term_width))
    print(r"                                                |                               ".center(term_width))
    print(r"                                            _  _|_  _                           ".center(term_width))
    print(r"                                           |;|_|;|_|;|                          ".center(term_width))
    print(r"                                           \\.    .  /                          ".center(term_width))
    print(r"                                            \\:  .  /                           ".center(term_width))
    print(r"                                             ||:   |                            ".center(term_width))
    print(r"                                             ||:.  |                            ".center(term_width))
    print(r"                                             ||:  .|                            ".center(term_width))
    print(r"                                             ||:   |       \,/                  ".center(term_width))
    print(r"                                             ||: , |            /`\             ".center(term_width))
    print(r"                                             ||:   |                            ".center(term_width))
    print(r"                                             ||: . |                            ".center(term_width))
    print(r"              __                            _||_   |                            ".center(term_width))
    print(r"     ____--`~    '--~~__            __ ----~    ~`---,              ___         ".center(term_width))
    print(r"-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~ ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"The king has orderd that a tower of wisdom and power be built.":^105}|".center(term_width))
    print(f"|{"One that will stand the test of time!":^105}|".center(term_width))
    print(f"|{"Using your knowledge of Mathematics, The king expects only the best!":^105}|".center(term_width))
    print(f"|{"He wants it to be built in the newly occupied land...":^105}|".center(term_width))
    print(f"|{"That will protect and guard the kingdom and its might!":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    level_mathematics()

    # End of Math Story

    os.system("cls")
    print(r"                  [_]___[_]__[_]___[_]       ".center(term_width))
    print(r"                  [__#__][__I_]__I__#]       ".center(term_width))
    print(r"                  [_I_#_I__#[__]__#__]       ".center(term_width))
    print(r"                     [_]_#_]__I_#_]          ".center(term_width))
    print(r"                     [I_|/ _W_ \|#]          ".center(term_width))
    print(r"                     [_I||{/~\}||_]          ".center(term_width))
    print(r"                     [__]|/\_/\||#]          ".center(term_width))
    print(r"                     [_I__I#___]__]          ".center(term_width))
    print(r"                     [__I_#_I___#_]          ".center(term_width))
    print(r"                     [#__I____]__I]          ".center(term_width))
    print(r"      .-.            [__I_#__I__[_]          ".center(term_width))
    print(r"   __|=|__          [_#_[__#_]__#]           ".center(term_width))
    print(r"   (_/`-`\_)         [__#_I__[#_I_]          ".center(term_width))
    print(r"   //\___/\\         [_I__]__#_I__]          ".center(term_width))
    print(r"   <>/   \<>         [#__I__#_]__I]          ".center(term_width))
    print(r"    \|_._|/          [_I#__I___I_#]    .:.   ".center(term_width))
    print(r"     <_I_>           [#__I__]_#___]   -=o=-  ".center(term_width))
    print(r"      |||            [_I__I#__]___]    ':'   ".center(term_width))
    print(r"     /_|_\         \\[__]#___][__#]//, \|/   ".center(term_width))
    print(r"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"The king was satisfied with the tower, 'This should protect us for now' - He said.":^105}|".center(term_width))
    print(f"|{"He ordered you to go back to the throne room, He has another mission for you!":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    # Start of Chemistry Story

    os.system("cls")
    print(r"                  _____                            ".center(term_width))
    print(r"           .-'     '-.                             ".center(term_width))
    print(r" _______ .'    __/  / '.      ___________          ".center(term_width))
    print(r"   ___ ____    \/`-/    \  __________________      ".center(term_width))
    print(r" __ _____      /) /      ;  _____ ---- _____       ".center(term_width))
    print(r" ____  |       /_\\      |                         ".center(term_width))
    print(r"       ;       _///      ;                         ".center(term_width))
    print(r"        \     /_|      _/_                         ".center(term_width))
    print(r"         '.   ______  |__||  ____                  ".center(term_width))
    print(r" _______   '-/\     `-|__||___________             ".center(term_width))
    print(r"____ ___    /__\      |__|| _______ ______         ".center(term_width))
    print(r"___        /____\     |__||      _______           ".center(term_width))
    print(r"          /___   \    |__||\                       ".center(term_width))
    print(r"         /____`-.-\   |__|| \                      ".center(term_width))
    print(r"        /___ __ ___\  |__|/  \       _________     ".center(term_width))
    print(r"       /____| /|____\         \    ___  ______     ".center(term_width))
    print(r"      /__   |_\|`.___\         \  ____ ____ ___    ".center(term_width))
    print(r"     /___`-.| <|______\         \                  ".center(term_width))
    print(r"    /__.-' _|__|_______\        _\_      __        ".center(term_width))
    print(r"   /__________________  \ ..--""   `--.-' /\       ".center(term_width))
    print(r"    /                 / /'               //\\      ".center(term_width))
    print(r"   /_________________/.|________________/ //\\     ".center(term_width))
    print(r"___||_ __ __ __ _ _||_ |_-__ _ __ _ __.-|/|/|_____ ".center(term_width))
    print(r"   ||_|  |__|\ |_| || ||_| >|_|  |_| _|_|||/|      ".center(term_width))
    print(r"   ||_|__|__| ||_|_||_||_|/_|_|__| |< |_||//|      ".center(term_width))
    print(r"   ||_|< |__|.||_| || ||_|  |_|  |_|_\|_| //       ".center(term_width))
    print(r"   ||_|_\|__| ||_|_||_||\|_/|_|__|_|__|_|//        ".center(term_width))
    print(r"   ||_______|_||___||__|________________|/         ".center(term_width))
    print(r"   || / / / / / / /||//|________________|          ".center(term_width))
    print(r"  /||/_/_/_/_/_/_/_||/ /                           ".center(term_width))
    print(r"  |__________________|/                            ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"The king wants you with your bravery to go to the Witch's lair.":^105}|".center(term_width))
    print(f"|{"He wanted the potion that the witch has been working on for a while.":^105}|".center(term_width))
    print(f"|{"He wants you to retrieve it to him!":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    os.system("cls")                       
    print(r"           |       *     |                  ".center(term_width))
    print(r"            | _  *                          ".center(term_width))
    print(r"               * (     /      \    ___      ".center(term_width))
    print(r"                  "     "        _/ /       ".center(term_width))
    print(r"                 (   *  )    ___/   |       ".center(term_width))
    print(r"                   )   *     _ o)'-./__     ".center(term_width))
    print(r"                  *  _ )    (_, . $$$       ".center(term_width))
    print(r"                  (  )   __ __ 7_ $$$$      ".center(term_width))
    print(r"                   ( :  { _)  '---  $\      ".center(term_width))
    print(r"              ______'___//__\   ____, \     ".center(term_width))
    print(r"               )           ( \_/ _____\_    ".center(term_width))
    print(r"             .'             \   \------''.  ".center(term_width))
    print(r"             |='           '=|  |         ) ".center(term_width))
    print(r"             |               |  |  .    _/  ".center(term_width))
    print(r"              \    (. ) ,   /  /__I_____\   ".center(term_width))
    print(r"               '._/_)_(\__.'   (__,(__,_]   ".center(term_width))
    print(r"              @---()_.'---@                 ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"As you enter the Witch’s lair, the air smelt of the scent of herbs…":^105}|".center(term_width))
    print(f"|{"You see a cauldron bubbling…":^105}|".center(term_width))
    print(f"|{"You hear a faint crackling sound of whooshes and sparkles.":^105}|".center(term_width))
    print(f"|{"Through the dark, eerie night, you see shelves lined with vials…":^105}|".center(term_width))
    print(f"|{"At last! You saw the kingdom’s top witch.":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    os.system('cls')
    print("\n\n")
    print(equallength.center(term_width))
    print(f"|{"She turns to you, eyes gleaming with curiosity…":^105}|".center(term_width))
    print(f"|{"“Ah, just in time!” – The witch said…":^105}|".center(term_width))
    print(f"|{"'I require assistance to perfect my latest creation'":^105}|".center(term_width))
    print(f"|{"'I need your brain power to help me balance the chemicals I’m gonna use.'":^105}|".center(term_width))
    print(f"|{"'You have no choice but to comply', as she said she would turn you into a spoon if you don’t comply…":^105}|".center(term_width))
    print(f"|{"The King had told you, before you left, to comply to the witch when you are being threathened…":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    level_chemistry()

    # End of Chem Story

    os.system('cls')
    print(r"      _____    ".center(term_width))
    print(r"     `.___,'   ".center(term_width))
    print(r"      (___)    ".center(term_width))
    print(r"      < X >    ".center(term_width))
    print(r"       ) (     ".center(term_width))
    print(r"      /`-.\    ".center(term_width))
    print(r"     /   X \   ".center(term_width))
    print(r"    / _    _\  ".center(term_width))
    print(r"   :,' `-.' `: ".center(term_width))
    print(r"   |   X     | ".center(term_width))
    print(r"   :     X   ; ".center(term_width))
    print(r"    \       /  ".center(term_width))
    print(r"     `.___.'   ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"As you exit her lair, you've managed to steal the potion...":^105}|".center(term_width))
    print(f"|{"“The king was estatic! He Immediately sold it and made a lot of money.":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("\nPress Enter to Continue")
    os.system('cls')

    # Statistics Story

    os.system('cls')

    print(r"                    .                     ".center(term_width))
    print(r"                   / \                    ".center(term_width))
    print(r"                  _\ /_                   ".center(term_width))
    print(r"        .     .  (,'v`.)  .     .         ".center(term_width))
    print(r"        \)   ( )  ,' `.  ( )   (/         ".center(term_width))
    print(r"         \`. / `-'     `-' \ ,'/          ".center(term_width))
    print(r"          : '    _______    ' :           ".center(term_width))
    print(r"          |  _,-'  ,-.  `-._  |           ".center(term_width))
    print(r"          |,' ( )__`-'__( ) `.|           ".center(term_width))
    print(r"          (|,-,'-._   _.-`.-.|)           ".center(term_width))
    print(r"          /  /<( o)> <( o)>\  \           ".center(term_width))
    print(r"          :  :     | |     :  :           ".center(term_width))
    print(r"          |  |     ; :     |  |           ".center(term_width))
    print(r"          |  |    (.-.)    |  |           ".center(term_width))
    print(r"          |  |  ,' ___ `.  |  |           ".center(term_width))
    print(r"          ;  |)/ ,'---'. \(|  :           ".center(term_width))
    print(r"      _,-/   |/\(       )/\|   \-._       ".center(term_width))
    print(r"_..--'.-(    |   `-'''-'   |    )-.`--.._ ".center(term_width))
    print(r"         `.  ;`._________,':  ,'          ".center(term_width))
    print(r"        ,' `/               \'`.          ".center(term_width))
    print(r"             `------.------'          '   ".center(term_width))
    print(r"             '                            ".center(term_width))
    print("\n\n")

    print(equallength.center(term_width))
    print(f"|{"The King leads you deep into the Royal Gold Vaults, where mountains of wealth are stored.":^105}|".center(term_width))
    print(f"|{"He wants you to use your statistical knowledge to calculate the wealth that the kingdom has.":^105}|".center(term_width))
    print(f"|{"This is the final test, as this will determine if you live or perish!":^105}|".center(term_width))
    print(equallength.center(term_width))

    input("Press Enter to Continue")
    os.system('cls')

    result_storymode = level_statistics()

    # The Ending

    if result_storymode == 0: # LOSE
        
        os.system('cls')

        print(r"                                                               o .,<>., o         ".center(term_width))
        print(r"                                                               |\/\/\/\/|         ".center(term_width))
        print(r"                                                               '========'         ".center(term_width))
        print(r"                                                               (_ SSSSSSs         ".center(term_width))
        print(r"                                                               )a'`SSSSSs         ".center(term_width))
        print(r"                                                              /_   SSSSSS         ".center(term_width))
        print(r"                                                              .=## SSSSS          ".center(term_width))
        print(r"                                                              .####  SSSSs        ".center(term_width))
        print(r"                                                              ###::::SSSSS        ".center(term_width))
        print(r"                                                             .;:::''''SSS         ".center(term_width))
        print(r"                                                            .:;:'  . .  \\        ".center(term_width))
        print(r"                                                           .::/  '     .'|        ".center(term_width))
        print(r"                                                          .::( .         |        ".center(term_width))
        print(r"                                                          :::)           \        ".center(term_width))
        print(r"                                                          /\(            /        ".center(term_width))
        print(r"                                                         /)            ( |        ".center(term_width))
        print(r"                                                       .'  \  .       ./ /        ".center(term_width))
        print(r"                                                    _-'    |\  .        |         ".center(term_width))
        print(r"                                  _..--..   .  /'---\      | ` |      . |         ".center(term_width))
        print(r"          -=====================,' _     \=(*#(7.#####()   |  `/_..   , (         ".center(term_width))
        print(r"                      _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.) \         ".center(term_width))
        print(r"                    ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |        ".center(term_width))
        print(r"                  ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )'  |        ".center(term_width))
        print(r"                _/   `._,' ,')`;  `-'`'                    |     L  /    /        ".center(term_width))
        print(r"               / `.   ,' ,|_/ / \                          (    <_-'     \        ".center(term_width))
        print(r"               \ / `./  '  / /,' \                        /|`         `. |        ".center(term_width))
        print(r"               )\   /`._   ,'`._.-\                       |)            \'        ".center(term_width))
        print(r"              /  `.'    )-'.-,' )__)                      |\            `|        ".center(term_width))
        print(r"             : /`. `.._(--.`':`':/ \                      ) \             \       ".center(term_width))
        print(r"             |::::\     ,'/::;-))  /                      ( )`.            |      ".center(term_width))
        print(r"             ||:::::  . .::':  :`-(                       |/    .          |      ".center(term_width))
        print(r"             ||::::|  . :|  |==[]=:                       .        -       \      ".center(term_width))
        print(r"             |||:::|  : ||  :  |  |                      /\           `     |     ".center(term_width))
        print(r" ___ ___     '|;:::|  | |'   \=[]=|                     /  \                \     ".center(term_width))
        print(r"|   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.  ".center(term_width))
        print(r":   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .              \ ".center(term_width))
        print(r" \___.>`''-.||:.__,'     SSt |_______`>              <_____:::.         . . \  _/ ".center(term_width))
        print(r"                                                           `+a:f:......jrei'''    ".center(term_width))
        print("\n\n")

        print(equallength.center(term_width))
        print(f"|{"The kingdom suffered, after the king's incorrect decisions based on your answers!":^105}|".center(term_width))
        print(f"|{"":^105}|".center(term_width))
        print(f"|{"You Perished!":^105}|".center(term_width))
        print(equallength.center(term_width))

        input("Press Enter to go back to the main menu")
        os.system('cls')

    if result_storymode == 1: # WIN

        os.system('cls')

        print(r"                    |>>>                        |>>>                           ".center(term_width))
        print(r"                    |                           |                              ".center(term_width))
        print(r"                _  _|_  _                   _  _|_  _                          ".center(term_width))
        print(r"               | |_| |_| |                 | |_| |_| |                         ".center(term_width))
        print(r"               \  .      /                 \ .    .  /                         ".center(term_width))
        print(r"                \    ,  /                   \    .  /                          ".center(term_width))
        print(r"                 | .   |_   _   _   _   _   _| ,   |                           ".center(term_width))
        print(r"                 |    .| |_| |_| |_| |_| |_| |  .  |                           ".center(term_width))
        print(r"                 | ,   | .    .     .      . |    .|                           ".center(term_width))
        print(r"                 |   . |  .     . .   .  ,   |.    |                           ".center(term_width))
        print(r"     ___----_____| .   |.   ,  _______   .   |   , |---~_____                  ".center(term_width))
        print(r"_---~            |     |  .   /+++++++\    . | .   |         ~---_             ".center(term_width))
        print(r"                 |.    | .    |+++++++| .    |   . |              ~-_          ".center(term_width))
        print(r"              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_       ".center(term_width))
        print(r"     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__   ".center(term_width))
        print(r"-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~ ".center(term_width))
        print("\n\n")

        print(equallength.center(term_width))
        print(f"|{"The kingdom grows richer, after the king's correct decisions based on your answers!":^105}|".center(term_width))
        print(f"|{"":^105}|".center(term_width))
        print(f"|{"You Win!":^105}|".center(term_width))
        print(equallength.center(term_width))

        input("Press Enter to go back to the main menu")
        os.system('cls')

# Chemistry Level Function - JOHN CARLO
def question_atoms(element, ans, side="reactant"):

    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
    
    print("\n⚛️ **Challenge 1: Identify Atoms in Chemical Equation** 🔬\n\n")
    
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width))
    print(r"| The witch puts in Sodium Carbonate (Na2CO3) and Hydrochloric Acid (HCl) into the cauldron |".center(term_width))
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width))
    print(r"| It resulted in Sodium Chloride (NaCl), Water (H2O), and Carbon Dioxide Gas (CO2)          |".center(term_width))
    print(r"+-------------------------------------------------------------------------------------------+".center(term_width)+"\n\n")

    answer = input(f"Identify the number of atoms of {element} from the {side} side:\n>> ")
    if answer == ans:
        print("\n✅ Correct!")
        time.sleep(1)
        os.system('cls')
        return 1
    else:
        print("\n❌ Incorrect! Try again.")
        time.sleep(1)
        os.system('cls')
        return 0

def balancing_table():

    os.system('cls')
    
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 65
    
    print("\n⚗️ **Challenge 2: Balance Chemical Equation** 👩‍🔬\n\n")

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

def level_chemistry():

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

    # Balance Equation - Challenge 2

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

    return result 

# Mathematics Level Function - YVAN
def level_mathematics():

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

    numbers = [random.randint(1, 10) for _ in range(10)]

    while True:
        print("\n🧮 **Challenge: Measures of Central Tendency** 📖")
        print("If there is no mode, Enter \"N/A\"\n\n")

        stats_numbers = f"| Numbers: {numbers} |"
        border_stats = "="*len(stats_numbers)
        print(border_stats.center(term_width))
        print(stats_numbers.center(term_width))
        print(border_stats.center(term_width))

        try:
            correct_mean = mean(numbers)
            correct_median = median(numbers)
            correct_mode = mode(numbers)
            
            user_mean = float(input("Enter the mean: "))
            user_median = float(input("Enter the median: "))
            if correct_mode == "N/A":
                user_mode = input("Enter the mode: ")
            else:
                user_mode = float(input("Enter the mode: "))
            break
        except Exception:
            os.system('cls')
            continue
    
    print("\nResults:")
    print(f"Your mean: {user_mean} (Correct: {correct_mean})")
    print(f"Your median: {user_median} (Correct: {correct_median})")
    print(f"Your mode: {user_mode} (Correct: {correct_mode})")

    time.sleep(3)
    
    if user_mean == correct_mean and user_median == correct_median and user_mode == correct_mode:
        return 1
    else:
        return 0

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
            invalidinput = False
            story_mode()
        elif choice == "2":
            invalidinput = False
            os.system('cls')
            level_selector()
        elif choice == "3":
            invalidinput = False
            os.system('cls')
            help_section()
        elif choice == "4":
            invalidinput = False
            while True:
                os.system('cls')
                confirmation = input("\nAre you sure?\nType 'Yes' to exit\n\n>> ")
                if confirmation == "Yes":
                    os.system('cls')
                    print("\nExiting game. See you next time!\n")
                    break
                else:
                    continue
            break
        elif choice == "exit":
            break
        else:
            invalidinput = True

if __name__ == "__main__":
    main()