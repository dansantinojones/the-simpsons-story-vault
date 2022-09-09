
words = {
    "character1": ["Mr Burns", "Ned Flanders", "Milhouse", "Barney", "Krusty the Clown"],
    "character2": ["Smithers", "Moe", "Principle Skinner", "Apu", "Cheif Wiggum"],
    "location": ["Springfield Elementary School", "Burns Manor", "Nuclear Power Plant", "Moe's Tavern", "Kwik-E-Mart"],
    "food": ["burger", "fried shrimp", "buttered noodles", "pork chops", "doghnuts"],
    "emotion": ["happy", "sad", "excited", "angry", "nervous",],
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
    "Celebrity": ["Donald Trump", "Johnny Depp", "Kim Kardashian", "Mark Zuckerberg", "Taylor Swift"], 
    "objects": ["candles", "flowers", "fruit", "pencils", "Sideshow Bob bobbleheads"],
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

introduction()


def main():
    # Displays the four story options and and exit option
    # Options will repeat if a number outside 1-5 is selected
    # While loop breaks if exit option (5) is selected
    while True: 
        print("Please select a character from the list below...")
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
            print("Goodbye")
            break

        else:
            print("Please enter valid option")



def homer_story():
    print("~~~~~~~~~~~~~~~ Homer Story ~~~~~~~~~~~~~~~")
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
    print("      \  -hrr-    \ `.  |    | ")


    print(f"I was woken up to a call from {celebrity} saying I have won {number} hundred dollars on the lottery")
    print("{number} hundred dollars on the lottery... But I don’t do the lottery... Oh well free money woo hoo!")
    print(f"When I first went down for breakfast my favourite {food} was replaced by {objects} 'Hmmm strange'.")
    print(f"D’oh my toothpaste had been replaced with {liquid}. After putting on my clothes I received another call,")
    print(f"this time from {character1} telling me I had the day off from work woo hoo! I then heard a familiar laugh…")
    print(" it was Bart, he shouted 'April fools!!!' I screamed 'why you little!' before choking him.")
    print(f"Boy did I feel {emotion}")



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

    print(f"Kids we have visitors coming round for dinner so I want you back from the {location} at 6pm.")
    print(f"Mmm-mmmmm I hope they like the {food} I have prepared, I have spent {number} hours cooking this.")
    print(f"{character1} can sit next to Bart and I think I’ll place {character2} next to Homer.")
    print(f"I hope they don’t bring their {adjective} {animal} or there won’t be enough food to go round.")
    print(f"I am so {emotion} to see them, the saddest thing is seeing a family broken apart. ")



def lisa_story():
    print("~~~~~~~ Lisa Story ~~~~~~~~")
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
    print("      /           \ ") 

    print(f"Today my school teacher, Mrs {food}, announced that instead of studying")
    print(f"{subject} today, we are going on a class field trip to {location}. Instead of going on the")
    print(f"school bus we are travelling by {transport}. On the way there we did our English lessons, ")
    print(f"she read a poem about {thing2} by {character2}. When we finally arrived our tour ")
    print(f"guide {character1} showed us around. We learned how to {activity} and got to sketch pictures of {thing1}.")




def bart_story():
    print("~~~~~~~~~~~~~~~ Bart Story ~~~~~~~~~~~~~~~")
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
    print("         /")

    print("Halloween in Springfield is my favourite time of year. Me and Lisa went trick-or-teating as it went dark.")
    print(f"I dressed up as a scary {thing2} and Lisa dressed up as {colour} zombie. The first house was answered by ")
    print(f"{character2} who gave us {food}. The next few houses gave us candy, we had {number} in total.")
    print(f"When we reached the spooky {location} I tip-toed to the door and just as I was about to knock the door, ")
    print(f"{character1} answered the door. When I realised who it was I screamed “eat my shorts!”")
    print("and we ran back laughing the whole way home.")



main()