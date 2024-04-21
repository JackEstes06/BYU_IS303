# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
# Project 3 -

# Project imports
import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plot
import sqlalchemy
from sqlalchemy import create_engine, text

# Database connection parameters
database_name = "talks"
db_user = "postgres"
db_password = "3210Jte10!"
db_host = "localhost"
db_port = "5432"
# Connects to postgres database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
engine.connect()


# create a class to keep track of talks as they happen
class Talk:
    def __init__(self, speaker, talkName, kicker):
        self.speaker = speaker
        self.talkName = talkName
        self.kicker = kicker
        self.standard_work_dict = {'Speaker_Name': speaker, 'Talk_Name': talkName, 'Kicker': kicker, 'Matthew': 0,
                                   'Mark': 0, 'Luke': 0, 'John': 0, 'Acts': 0, 'Romans': 0, '1 Corinthians': 0,
                                   '2 Corinthians': 0, 'Galatians': 0, 'Ephesians': 0, 'Philippians': 0,
                                   'Colossians': 0, '1 Thessalonians': 0, '2 Thessalonians': 0, '1 Timothy': 0,
                                   '2 Timothy': 0, 'Titus': 0, 'Philemon': 0, 'Hebrews': 0, 'James': 0, '1 Peter': 0,
                                   '2 Peter': 0, '1 John': 0, '2 John': 0, '3 John': 0, 'Jude': 0, 'Revelation': 0,
                                   'Genesis': 0, 'Exodus': 0, 'Leviticus': 0, 'Numbers': 0, 'Deuteronomy': 0,
                                   'Joshua': 0, 'Judges': 0, 'Ruth': 0, '1 Samuel': 0, '2 Samuel': 0, '1 Kings': 0,
                                   '2 Kings': 0, '1 Chronicles': 0, '2 Chronicles': 0, 'Ezra': 0, 'Nehemiah': 0,
                                   'Esther': 0, 'Job': 0, 'Psalm': 0, 'Proverbs': 0, 'Ecclesiastes': 0,
                                   'Song of Solomon': 0, 'Isaiah': 0, 'Jeremiah': 0, 'Lamentations': 0, 'Ezekiel': 0,
                                   'Daniel': 0, 'Hosea': 0, 'Joel': 0, 'Amos': 0, 'Obadiah': 0, 'Jonah': 0, 'Micah': 0,
                                   'Nahum': 0, 'Habakkuk': 0, 'Zephaniah': 0, 'Haggai': 0, 'Zechariah': 0, 'Malachi': 0,
                                   '1 Nephi': 0, '2 Nephi': 0, 'Jacob': 0, 'Enos': 0, 'Jarom': 0, 'Omni': 0,
                                   'Words of Mormon': 0, 'Mosiah': 0, 'Alma': 0, 'Helaman': 0, '3 Nephi': 0,
                                   '4 Nephi': 0, 'Mormon': 0, 'Ether': 0, 'Moroni': 0, 'Doctrine and Covenants': 0,
                                   'Moses': 0, 'Abraham': 0, 'Joseph Smith—Matthew': 0, 'Joseph Smith—History': 0,
                                   'Articles of Faith': 0}

    def updateData(self, scrapedScriptureRefs):
        scriptureRefs = ""
        for ref in scrapedScriptureRefs:
            refStr = ref.text
            scriptureRefs += refStr
        for key in self.standard_work_dict:
            self.standard_work_dict[key] = scriptureRefs.count(key)
        self.standard_work_dict["Speaker_Name"] = self.speaker  # .replace('\xa0', ' ')
        self.standard_work_dict["Talk_Name"] = self.talkName
        self.standard_work_dict["Kicker"] = self.kicker


def webScraper(urlPath):
    # Grab the href of the talk link
    # Navigate to the talk's link and scrape the html for data
    oScrapeResponse = requests.get(f"{baseURL}{urlPath}")
    scrapedSoup = BeautifulSoup(oScrapeResponse.content, 'html.parser')
    # Get the talk's title if it exists
    scrapedTitle = scrapedSoup.find("h1", attrs={"id": "title1"})
    # Get the talk's speaker and calling if they exist
    scrapedAuthor = scrapedSoup.find("p", attrs={"id": "author1"})
    scrapedAuthorCalling = scrapedSoup.find("p", attrs={"id": "author2"})
    # Get the kicker
    scrapedKicker = scrapedSoup.find("p", attrs={"id": "kicker1"})
    oTalk = Talk(scrapedAuthor.text, scrapedTitle.text, scrapedKicker.text)
    # Get the talk's related content
    scrapedRelatedContent = scrapedSoup.findAll("a", attrs={"class": "scripture-ref"})
    if scrapedRelatedContent:
        oTalk.updateData(scrapedRelatedContent)
        talk_list.append(oTalk)
    else:
        print("related content not found")


user_input = input("If you want to scrape data, enter 1. If you want to see summaries of stored data, enter 2. "
                   "Enter any other value to exit the program: ")
talk_list = []

if user_input == "1":
    # Base URL
    baseURL = "https://www.churchofjesuschrist.org"
    # Store the response object for the website we want to scrape data from
    oResponse = requests.get(f"{baseURL}/study/general-conference/2023/10?lang=eng")
    # Create a collection of all the HTML tags and data
    soup = BeautifulSoup(oResponse.text, 'html.parser')
    # Search for specific tags that have the data you want to process
    all_talks = soup.findAll("a", attrs={"class": "list-tile"})
    # Talks to ignore
    talksToRemove = []
    # print(talk_links)
    for link in all_talks:
        # Call a function that parses through the talk link for data that we want
        hrefStr = link["href"].upper()
        # Ignore any sessions links
        if ("/STUDY/GENERAL-CONFERENCE/2023/10/21EYRING?LANG=ENG" in hrefStr) or ("-SESSION" in hrefStr):
            talksToRemove.append(link)
        else:
            webScraper(link["href"])
            print(f"trying to scrape url: {baseURL}{link["href"]} ")
    # Remove special session talk tiles
    for talk in talksToRemove:
        all_talks.remove(talk)

    myList = []
    for talk in talk_list:
        myList.append(talk.standard_work_dict)
    df = pd.DataFrame(myList)
    df.to_sql('general_conference', engine, if_exists='replace', index=False)

    print("You've scraped the data to your postgres database.")

elif user_input == '2':
    # make_talk_list()
    sql_query = 'select * from general_conference'
    all_talks = pd.read_sql_query(sql_query, engine)
    df_sums = all_talks.drop(['Speaker_Name', 'Talk_Name', "Kicker"], axis=1).sum()
    df_sums_filtered = df_sums[df_sums > 2]

    summary_input = input("You selected to see summaries. Enter 1 to see a summary of all talks. Enter 2 to select a "
                          "specific talk. Enter anything else to exit: ")
    if summary_input == '1':

        # create and display bar chart
        df_sums_filtered.plot(kind="bar")
        # assign title
        plot.title("Standard Works Referenced in General Conference")
        # create x-axis label
        plot.xlabel("Standard Works Books")
        # create y-axis label
        plot.ylabel("# Times Referenced")
        plot.show()

    elif summary_input == '2':
        sql_query = f"SELECT * FROM general_conference"
        df_from_postgres = pd.read_sql_query(sql_query, engine)
        df_sums = df_from_postgres.drop(['Speaker_Name', 'Talk_Name', "Kicker"], axis=1).sum()
        df_sums_filtered = df_sums[df_sums > 1]

        # Display the list of speakers and their talks
        print("The following are the names of speakers and their talks:")
        for index, talk in enumerate(df_from_postgres.itertuples(), start=1):
            print(f"{index}: {talk.Speaker_Name} - {talk.Talk_Name}")

        # Take user input to determine which talk to summarize
        choose_talk = int(input("Which talk would you like to choose? "))

        # Retrieve the chosen talk from the DataFrame
        chosen_talk = df_from_postgres.iloc[choose_talk - 1]

        # Filter the DataFrame to include only the chosen talk
        df_sums_filtered = df_from_postgres.iloc[choose_talk - 1].drop(
            ['Speaker_Name', 'Talk_Name', 'Kicker']).to_frame().T

        # Create and display bar chart for the chosen talk
        df_sums_filtered.T.plot(kind="bar")
        # Assign title
        plot.title(f"Standard Works Referenced in {chosen_talk['Talk_Name']}")
        # Create x-axis label
        plot.xlabel("Standard Works Books")
        # Create y-axis label
        plot.ylabel("# Times Referenced")
        plot.show()

else:
    print("Closing the program")
