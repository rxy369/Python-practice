# gets the input fom the player based on what they want to do
# prints the specific response based on input and then loops back to input
textInput = 9;
while textInput != 0:
    try:
        textInput = int(input("Hello! I'm a little robot. What would you like to know?\n"
                              "1. What's your favorite movie?\n"
                              "2. What's your favorite game?\n"
                              "3. What's your dream/goal in life?\n"))
    except ValueError:
        print("ERROR: please input number value.")
        textInput = 9
    # print specific response or ask again if invalid value was entered
    if textInput == 1:
        print("\nI haven't watched many movies, but recently I've fallen back in love with"
              " the first Pirates of the Carribean movie!\n")
    elif textInput == 2:
        print("\nXenoblade Chronicles is my all time favorite, with Kid Icarus: Uprising as a close"
              " second!\n")
    elif textInput == 3:
        print("\nI want to make games that are impossible not to enjoy. I want to learn as much as I can"
              " so that I can have complete creative freedom.\nThough I'll need some help every now and"
              " then, and I should try to take in as much media as I can so I can boost my creativity!\n")
    else:
        print("\nI didn't catch that. Can you say that again?\n")