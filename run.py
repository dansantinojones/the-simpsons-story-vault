
words = {
    "character1": ["Mr Burns", "Ned Flanders", "Milhouse", "Barney", "Krusty the Clown"],
    "character2": ["Smithers", "Moe", "Principle Skinner", "Apu", "Cheif Wiggum"],
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



introduction()
select()