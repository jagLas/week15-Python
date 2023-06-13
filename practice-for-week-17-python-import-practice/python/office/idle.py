from random import randint
# Your code here
"""
const getWater = () => {
    console.log("Getting water...");
    console.log("That was refreshing.");
}


"""

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[randint(0, len(coworkers) - 1)]
    print("Chatting with " + chatee + "...")
    print("Done")


def useSocialMedia():
    social_media = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = social_media[randint(0, len(social_media) - 1)]
    print("Using " + choice + "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")