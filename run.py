# The Simpsons Story Vault image 
# Input name and welcome message

def introduction():
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
    print("Please select a character from the list below...")
    print("1. Homer")
    print("2. Marge")
    print("3. Lisa")
    print("4. Bart")

    selection = input()

    if selection == "1":
        homer_story()

    elif selection == "2":
        marge_story()

    elif selection == "3":
        lisa_story()

    elif selection == "4":
        bart_story()

    else:
        print("Please enter valid option")



introduction()
select()