#Author: Galen Flanagan
#Fun Fact: A photo of mine is a famous internet meme template.
import random
topics = ["education", "hobbies", "family", "favorite foods", "recursion", "random"]
def intro():
    print("Hi my name is Galen Flanagan. I have a background in Computer Science from Virginia Tech.\n I also have a strong insert in Sports and board games")
    print("Would you like to know more about my educational background, my hobbies, my family, or my favorite foods?")
    aboutMe()

def aboutMe():
    userInput = ""
    while userInput != "stop":
        userInput = input("What other topics would you want to learn about. As a reminder the topics are: " + str(topics) + "\n say stop to stop").lower
        while(userInput not in topics):
            print("I\'m sorry I don't want to talk about"+ userInput + "right now\n")
            input("possible topics are: " + str(topics))
        if userInput == "random":
            print("you have chosen a random topic, spinning wheel\n")
            userInput = topics[random.randint(0,4)]
            print("the wheel has landed on" + userInput + "!\n")
        if userInput == "education":
            print("as previously mentioned I have a bachelors degree in computer science from Virginia Tech.\n")
            print("This degree was focused on Data centric computing which I often refer to as being a glorified statistics minor\n")
            print("Speaking of minors I have two minors from my Undergraduate, those being Political Science and Quantum information science and engineering\n")
        elif userInput == "hobbies":
            print("as previously mentioned I enjoy sports and board games.\n")
            print("My favorite sport is biking and I enjoy regularly biking to class. It's a good way to both get  physical exercise and transport myself quickly\n")
            print("As for board games, I enjoy all kinds of games, but my favorites are engine builder games like terraforming mars or wingspan\n")
        elif userInput == "family":
            print("I have two younger brothers, the older one is just starting a career as a teacher, well the younger is only just starting High School")
            print("My father is an electrical engineer who works for the MITRE corporation, well my Mom is a veterinarian\n")
            print("We also have two kittens, Marshmallow and Peanut. (I didn't choose the names) Peanut is blind but very cute\n")
            print("In addition to the two cats we have a whole host of other pets, including three chickens (yummy eggs), 6 geese, and 10 fuzzy lawnmowers on feet. (AKA sheep)\n")
        elif userInput == "favorite food":
            print("I like lots of foods and generally enjoy something in every cuisine, but my favorite food is probably injera.\n")
            print("for those who don't know injera is an Ethiopian sourdough made with teff flower (making it naturally gluten free) and it is delicious")
            print("another food I enjoy a lot are arepas, which are a type of fried flatbread made from maize that is stuffed with various foods.\n They are a common staple of Columbian and Venezuelan cuisine\n")
            print("If you haven't tried either of these foods I highly recommend you try one asap, you won't be disappointed.\n")
        else :
            print("Ah, you have chosen recursion, I must warn you that this will go on forever if you don't answer no")
            recursion()
def recursion():
    userInput = input("recursion is fun, do you think recursion is fun?\n").lower
    if userInput == "no":
        print("recursion terminated, very sad")
    print("you also like recursion, well then you will surely enjoy what's coming next!\n")
    recursion()