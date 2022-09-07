
words = {
    "character1": ["Mr Burns", "Ned Flanders", "Milhouse", "Barney", "Krusty the Clown"],
    "character2": ["Smithers", "Moe", "Principle Skinner", "Apu", "Cheif Wiggum"],
    "location": ["Springfield Elementary School", "Burns Manor", "Nuclear Power Plant", "Moe's Tavern", "Kwik-E-Mart"],
    "food": ["Burger", "Fried Shrimp", "Buttered Noodles", "Pork Chops", "Doghnuts"],
}


def introduction():
    # The Simpsons Story Vault image 
    # Input name and welcome message
    print("_____________________________________________________________")
    print("| |_   _| || | __| / __|| ||  \/  | _ \/ __|/ _ \| \| |/ __|  |")
    print("|   | | | _  | _|  \__ \| || |.,| |  _/\__ \ (_) | .` |\__ \  |")
    print("|   |_| |_||_|___| |___/|_||_|  |_|_|  |___/\___/|_|\_||___/  |")
    print("|   __  ___  __   __                     _            ___     |")
    print("|  (__   |  /  \ |__) \ /        \   /  /_\  |  | |    |      |")
    print("| _ __)__|__\__/_|__\__|__________\_/__/___\_\__/_|__ _|_____ |")
    print("||         _.-'-``-._          |      \:::::::::'      /     ||")
    print("||       ,'::::::''  `.        |      /::::::'         \     ||")
    print("||      ::::::'        :       |      \:::::           /     ||")
    print("||      |:::'          |       |      /;'`--'`--'`--'`.\     ||")
    print("||      ;:::  .  ,     :       |      \_.`--'.  ,'- '._/     ||")
    print("||     :-------::-------:      |      /:  o   ::  o   :\     ||")
    print("||     `.__o__.;:.__o__.'      |      \:.____.;:.____.'/     ||")
    print("||_____(.:::::(:_)_____.)______|______(.:::::(:_)_____.)_____||")
    print("||          _     _            |                             ||")
    print("||        ,':`._.':`.          |       \`.`.'`.'`.'`'(       ||")
    print("||    ..-':::::::'   `--..     |        :::::::::''  :       ||")
    print("||   \:::::::::          /     |        |:::::'      |       ||")
    print("||   _`.::::::          `._    |        |::::        |       ||")
    print("|| .':::_.`--'.  ,'--'._   `,  |       (.----.  ,----.)      ||")
    print("||  `.:::  o   ::  o   :  ,'   |       :  o   ::  o   :      ||")
    print("||   ,':`.____.;:.____.' `.    |       `.____.;:.____.'      ||")
    print("||__`.:(.:::::(:_)_____.)_, ___|_______(.::::(:_)____.)______||")
    print("'-------------------------------------------------------------'")
    
    name = input("Enter your name: ")
    print(f"Welcome {name} to The Simpsons Story Vault")



def select():
    # Displays the four story options and and exit option
    # Options will repeat if a number outside 1-5 is selected
    # While loop breaks if exit option (5) is selected
    while True: 
        print("Please select a character from the list below...")
        print("1. Homer")
        print("2. Marge")
        print("3. Lisa")
        print("4. Bart")
        print("5. Exit")

        selection = input()

        if selection == "1":
            homer_story()

        elif selection == "2":
            marge_story()

        elif selection == "3":
            lisa_story()

        elif selection == "4":
            bart_story()

        elif selection == "5":
            print("Goodbye")
            break

        else:
            print("Please enter valid option")



def marge_story():
    print("~~~~~~~~~~~~~~~ Marge Story ~~~~~~~~~~~~~~~")
    print("        (                          )")
    print("         \                        /")
    print("        ,' ,__,___,__,-._         )")
    print("        )-' ,    ,  , , (        /")
    print("-hrr-   ;''-^-.,-'''''\' \       )")
    print("       (      (        ) /  __  /")
    print("        \o,----.  o  _,'( ,.^. \ ")
    print("        ,'`.__  `---'    `\ \ \ \_")
    print(" ,.,. ,'                   \    ' )")
    print(" \ \ \\__  ,------------.  /     /")
    print("( \ \ \( `---.-`-^--,-,--\:     :")
    print(" \       (   (''''''`----'|     :")
    print("  \   `.  \   `.          |      \ ")
    print("   \   ;  ;     )      __ _\      \ ")
    print("   /     /    ,-.,-.''Y  Y  \      `. ")
    print("  /     :    ,`-'`-'`-'`-'`-'\       `. ")
    print(" /      ;  ,'  /              \        ` ")
    print("/      / ,'   /                \ ")

    print("Kids we have visitors coming round for dinner so I want you back from the {location} at 6pm.")
    print("Mmm-mmmmm I hope they like the {food} I have prepared, I have spent {number} hours cooking this.")
    print("{character 1} can sit next to Bart and I think I’ll place {character 2} next to Homer.")
    print("I hope they don’t bring their {adjective} {pet} or there won’t be enough food to go round.")
    print("I am so {feeling} to see them, the saddest thing is seeing a family broken apart. ")



introduction()
select()
marge_story()