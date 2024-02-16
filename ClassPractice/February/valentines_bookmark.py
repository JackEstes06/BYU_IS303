# Jack Estes
#
# I need to create a word map from a list for a bookmark for
# my wife. This takes a list of words, and generates a paragraph
# of those words at random frequencies.
import random

moreImportantWordList = [
    "Beautiful", "Amazing", "Funny", "Patient", "BFF", "Hot",
    "Understanding", "Kind", "Loving", "Loyal"
]
wordList = [
    "Kind-hearted", "Compassionate", "Intelligent",
    "Beautiful", "Supportive", "Generous", "Funny", "Creative",
    "Strong", "Brave", "Loving", "Caring", "Thoughtful",
    "Patient", "Understanding", "Trustworthy", "Loyal",
    "Passionate", "Adventurous", "Determined", "Empathetic",
    "Optimistic", "Resilient", "Genuine", "Inspiring", "Talented",
    "Grateful", "Affectionate", "Encouraging", "Motivated",
    "Warm-hearted", "Enthusiastic", "Elegant", "Graceful",
    "Radiant", "Charming", "Devoted", "Hardworking", "Dedicated",
    "Innovative", "Sophisticated", "Stylish", "Nurturing", "Wise",
    "Confident", "Selfless", "Joyful", "Spirited", "Captivating",
    "Irreplaceable", "Sexy", "Hilarious", "Silly", "Dingy",
    "Bootyful"
]
paragraph = ""

for i in range(0, 500):
    importantRandIndex = random.randint(0,len(moreImportantWordList)-1)
    paragraph += (moreImportantWordList[importantRandIndex] + " ")
    randIndex = random.randint(0,len(wordList)-1)
    paragraph += (wordList[randIndex] + " ")

print(paragraph)
