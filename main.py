import random
import time

# play again options for input in goAgain
playagain = [
    "yes",
    "y",
    "Y",
    "Yes",
    "again",
    "Again",
    "Play",
    "play"
]

# list of responses to give to the question.
responses = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes, definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"
]


def magic_8_ball():
    print("Welcome to the magic eight-ball!")
    # while loop to allow replay.
    while True:
        question = input("Please ask your question here: ")
        print("thinking...")
        time.sleep(0.4)
        # choosing response for the question from array.
        response = random.choice(responses)
        print(response)
        # Flagged play as false so they have a choice to go again.
        play = False
        go_again = input("Would you like to ask another question? yes / no.  ")
        # searching if their answer is in the array
        for phrase in playagain:
            # If true restart 8ball
            if phrase in go_again:
                play = True
                magic_8_ball()
            else:
                print("Thank you for using the magic eight-ball")
                exit()

magic_8_ball()


#if you wanted to make it ffrom random number in the array
#print(answers[random.randrange(0,len(answers) -1]))
#answesr is the array name