# import colorama
# from colorama import Fore, Back, Style
# colorama.init()

import time 


words = {
    "character1": ["Mr Burns", "Ned Flanders", "Milhouse", "Barney", "Krusty the Clown"],
    "character2": ["Smithers", "Moe", "Principle Skinner", "Apu", "Cheif Wiggum"],
    "location": ["Springfield Elementary School", "Burns Manor", "Nuclear Power Plant", "Moe's Tavern", "Kwik-E-Mart"],
    "food": ["burger", "fried shrimp", "buttered noodles", "pork chops", "doghnuts"],
    "emotion": ["happy", "sad", "excited", "angry", "nervous", ],
    "animal": ["dog", "snake", "cat", "spider pig", "monkey"],
    "colour": ["red", "blue", "yellow", "green", "purple"],
    "transport": ["car", "truck", "train", "horse & carriage", "airplane"],
    "subject": ["history", "art", "geography", "music", "physics"],
    "thing1": ["the ocean", "flowers", "trees", "houses", "space"],
    "thing2": ["alien", "ghost", "cowboy", "vampire", "dinosaur"],
    "activity": ["dance", "sing", "ride a bike", "take a selfie", "meditate"],
    "adjective": ["small", "rough", "kind", "ancient", "wide"],
    "number": ["3", "9", "6", "1", "4"],
    "liquid": ["water", "milk", "vinegar", "duff beer", "mustard"],
    "celebrity": ["Donald Trump", "Johnny Depp", "Kim Kardashian", "Mark Zuckerberg", "Taylor Swift"],
    "objects": ["candles", "flowers", "fruit", "pencils", "Sideshow Bob bobbleheads"],
}


def introduction():
    # The Simpsons Story Vault image
    # Input name and welcome message
    # print(Fore.YELLOW)
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

    time.sleep(2)

    name = input("Enter your name: \n")
    print(f"Welcome {name} to The Simpsons Story Vault\n")


introduction()


def selectItem(key):
    # Get the array of items
    items = words[key]
    for i in range(len(items)):
        # Print the number index and value from dictionary into a nenu
        print("{}.- {}".format(i + 1, items[i]))

    selection = -1

    validInput = False

    item = None

    while not validInput:
        # User must enter a number associated with the dictionary value
        input_value = input("Select a '{}' form the list above: [1..{}]\n"
                            .format(key, len(items)))
        try:
            selection = int(input_value)
            item = items[selection-1]
            validInput = True
        except (ValueError, IndexError):
            validInput = False
    return item


def main():
    # Displays the four story options and and exit option
    # Options will repeat if a number outside 1-5 is selected
    # While loop breaks if exit option (5) is selected
    while True:
        time.sleep(1)
        print("Please select a character from the list below...\n")
        print("1. Homer")
        print("2. Marge")
        print("3. Lisa")
        print("4. Bart\n")
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
            time.sleep(1)
            print("                            . .  ,  , ")
            print("                            |` \/ \/ \,', ")
            print("                            ;          ` \/\,. ")
            print("                           :               ` \,/ ")
            print("                           |                  / ")
            print("                           ;                 : ")
            print("                          :                  ; ")
            print("                          |      ,---.      / ")
            print("                         :     ,'     `,-._ \  ")
            print("                         ;    (   o    \   `' ")
            print("                       _:      .      ,'  o ; ")
            print("                      /,.`      `.__,'`-.__, ")
            print("                      \_  _               \ ")
            print("                     ,'  / `,          `.,' ")
            print("               ___,'`-._ \_/ `,._        ; ")
            print("            __;_,'      `-.`-'./ `--.____) ")
            print("         ,-'           _,--\^-' ")
            print("       ,:_____      ,-'     \ ")
            print("      (,'     `--.  \;-._    ; ")
            print("      :    Y      `-/    `,  : ")
            print("      : GOODBYE    :     /_;' ")
            print("      :    :       |    : ")
            print("       \    \      :    : ")
            print("        `-._ `-.__, \    `. ")
            print("           \   \  `. \     `. ")
            print("         ,-;    \---)_\ ,','/ ")
            print("         \_ `---'--''  '^-;' ")
            print("         (_`     ---''   ''  ")
            print("         / `--.__,. ,-'    \ ")
            print("-hrr-    )-.__,-- ||___,--' `-. ")
            print("        /._______,|__________,'\ ")
            print("        `--.____,'|_________,-'\n\n")

            time.sleep(1)

            print("Click 'Run Program' button above terminal to restart.")
            break

        else:
            print("Please enter valid option")


def homer_story():
    # Display dictionary values allowing user to choose words to create story
    time.sleep(0.5)
    celebrity = selectItem("celebrity")
    time.sleep(0.5)
    number = selectItem("number")
    time.sleep(0.5)
    food = selectItem("food")
    time.sleep(0.5)
    objects = selectItem("objects")
    time.sleep(0.5)
    liquid = selectItem("liquid")
    time.sleep(0.5)
    character1 = selectItem("character1")
    time.sleep(0.5)
    emotion = selectItem("emotion")

    time.sleep(1)

    print("\n~~~~~~~~~~~~~~~ Homer Story ~~~~~~~~~~~~~~~\n")

    time.sleep(1.5)

    print("     ,---. ")
    print("   ,.'-.   \ ")
    print("  ( ( ,''''''-. ")
    print("  `,X          `. ")
    print("  /` `           `._ ")
    print(" (            ,   ,_\ ")
    print(" |          ,---.,'  `. ")
    print(" |         /     \   o  ) ")
    print("  \ ,.    (   o   .____, ")
    print("   \| \    \____,'     \ ")
    print(" '`'\  \        _,____,' ")
    print(" \  ,--      ,-'     \ ")
    print("   ( C     ,'         \ ")
    print("    `--'  .'           | ")
    print("      |   |         .O | ")
    print("    __|    \        ,-'_ ")
    print("   / `L     `._  _,'  ' `. ")
    print("  /    `--.._  `',.   _\  ` ")
    print("  `-.       /\  | `. ( ,\  \ ")
    print(" _/  `-._  /  \ |--'  (     \ ")
    print("'  `-.   `'    \/\`.   `.    ) ")
    print("      \  -hrr-    \ `.  |    | \n\n")

    time.sleep(1)

    print(f"I was woken up to a call from {celebrity} saying I ") 
    print(f"have won {number} hundred dollars on the lottery... ")
    print(f"But I don’t do the lottery... Oh well free money woo hoo!")
    print(f"When I first went down for breakfast my favourite ")
    print(f"{food} was replaced by {objects}... 'Hmmm strange'.")
    print(f"D’oh my toothpaste had been replaced with {liquid}.")
    print(f"After putting on my clothes I received another call,")
    print(f"this time from {character1} telling me I had the day ")
    print(f"off from work woo hoo! I then heard a familiar laugh…")
    print("It was Bart, he shouted 'April fools!!!' ")
    print(f"I screamed 'why you little!' before choking him.")
    print(f"Boy did I feel {emotion}.\n\n")

    time.sleep(10)


def marge_story():
    time.sleep(0.5)
    location = selectItem("location")
    time.sleep(0.5)
    food = selectItem("food")
    time.sleep(0.5)
    number = selectItem("number")
    time.sleep(0.5)
    character1 = selectItem("character1")
    time.sleep(0.5)
    character2 = selectItem("character2")
    time.sleep(0.5)
    adjective = selectItem("adjective")
    time.sleep(0.5)
    animal = selectItem("animal")
    time.sleep(0.5)
    emotion = selectItem("emotion")

    time.sleep(1)

    print("\n~~~~~~~~~~~~~~~ Marge Story ~~~~~~~~~~~~~~~\n")

    time.sleep(1.5)

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
    print("/      / ,'   /                \ \n\n")

    time.sleep(1)

    print(f"Kids we have visitors coming round for dinner so")
    print(f"I want you back from the {location} at 6pm.")
    print(f"Mmm-mmmmm I hope they like the {food} I have prepared,")
    print(f"I have spent {number} hours cooking this.")
    print(f"{character1} can sit next to Bart and I think I’ll") 
    print(f"place {character2} next to Homie.")
    print(f"I hope they don’t bring their {adjective} {animal}")
    print(f"or there won’t be enough food to go round.")
    print(f"I am so {emotion} to see them, the saddest thing")
    print(f"is seeing a family broken apart.\n\n")

    time.sleep(10)


def lisa_story():
    time.sleep(0.5)
    colour = selectItem("colour")
    time.sleep(0.5)
    subject = selectItem("subject")
    time.sleep(0.5)
    location = selectItem("location")
    time.sleep(0.5)
    transport = selectItem("transport")
    time.sleep(0.5)
    thing2 = selectItem("thing2")
    time.sleep(0.5)
    character2 = selectItem("character2")
    time.sleep(0.5)
    character1 = selectItem("character1")
    time.sleep(0.5)
    activity = selectItem("activity")
    time.sleep(0.5)
    thing1 = selectItem("thing1")

    time.sleep(1)

    print("\n~~~~~~~ Lisa Story ~~~~~~~~\n")

    time.sleep(1.5)

    print("         /\    /\ ")
    print("        /  \  /  \ ")
    print("    __ /    \/    \__ __ ")
    print("   \                   / ")
    print("    \                 / ")
    print("     :               /_ ")
    print("    /       \_| \_|   / ")
    print("   /       \/  \,  \ / ")
    print("   \       ( o  ) o ) ")
    print("    \ /c    \__, --. ")
    print("    | \_     ,     -' ")
    print("    :_ |    '\_______) ")
    print("      ||          _) ")
    print("       :         : ")
    print("       |         | ")
    print("       ooooooooooo ")
    print("      /           \ \n")

    time.sleep(1)

    print(f"Today my school teacher, Mrs {colour},") 
    print(f"announced that instead of studying {subject} today,")
    print(f"we are going on a class field trip to")
    print(f"{location}. Instead of going on the")
    print(f"school bus we are travelling by {transport}.")
    print(f"On the way there we did our English lessons, she read")
    print(f"a poem about {thing2} by {character2}.") 
    print(f"When we finally arrived our tour guide")
    print(f"{character1} showed us around. ")
    print(f"We learned how to {activity} and got to ")
    print(f"sketch pictures of {thing1}.\n\n")

    time.sleep(10)


def bart_story():
    time.sleep(0.5)
    thing2 = selectItem("thing2")
    time.sleep(0.5)
    colour = selectItem("colour")
    time.sleep(0.5)
    character2 = selectItem("character2")
    time.sleep(0.5)
    food = selectItem("food")
    time.sleep(0.5)
    number = selectItem("number")
    time.sleep(0.5)
    location = selectItem("location")
    time.sleep(0.5)
    character1 = selectItem("character1")

    time.sleep(1)

    print("\n~~~~~~~~~~~~~~~ Bart Story ~~~~~~~~~~~~~~~\n")

    time.sleep(1.5)

    print("            |\|\,'\,'\ ,.")
    print("            )        ;' |,'")
    print("           /              |,'|,.")
    print("          /                  ` /__")
    print("         ,'                    ,-'")
    print("        ,'                    :")
    print("       (_                     '")
    print("     ,'                      ;")
    print("     |---._ ,'     .        '")
    print("     :   o Y---.__  ;      ;")
    print("     /`,""-|     o`.|     /")
    print("    ,  `._  `.    ,'     ;")
    print("    ;         `""'      ;")
    print("   /                   -'.")
    print("   \                   G  )")
    print("    `-.__________,   `._,'")
    print("            (`   `     |)\ ")
    print("-hrr.      / `.       ,'  \ ")
    print("          /    `-----'     \ ")
    print("         /\n\n")

    time.sleep(1)

    print(f"Halloween in Springfield is my favourite time of year.")
    print(f"Me and Lisa went trick-or-teating as it went dark.")
    print(f"I dressed up as a scary {thing2} and ")
    print(f"Lisa dressed up as {colour} zombie. ")
    print(f"The first house was answered by ")
    print(f"{character2} who gave us {food}. ")
    print(f"The next few houses gave us candy, we had {number}") 
    print(f"in total. When we reached the spooky")
    print(f"{location} I tip-toed ")
    print(f"to the door and just as I was about to knock the door, ")
    print(f"{character1} answered the door. When I realised who") 
    print(f"it was I screamed “eat my shorts!”")
    print("and we ran back laughing the whole way home.\n\n")

    time.sleep(10)


main()
