# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
# Project 3 -

import pandas as pd
from bs4 import BeautifulSoup
import requests


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
            print(refStr)

        for key in self.standard_work_dict:
            self.standard_work_dict[key] = scriptureRefs.count(key)

        self.standard_work_dict["Speaker_Name"] = self.speaker  # .replace('\xa0', ' ')
        self.standard_work_dict["Talk_Name"] = self.talkName
        self.standard_work_dict["Kicker"] = self.kicker
        print()


def webScraper(urlPath):
    # Grab the href of the talk link
    print(f"Href: {urlPath}\n")

    # Navigate to the talk's link and scrape the html for data
    oScrapeResponse = requests.get(f"{baseURL}{urlPath}")
    scrapedSoup = BeautifulSoup(oScrapeResponse.content, 'html.parser')

    # Get the talk's title if it exists
    scrapedTitle = scrapedSoup.find("h1", attrs={"id": "title1"})
    if scrapedTitle:
        print(f"Title: {scrapedTitle.text}")

    # Get the talk's speaker and calling if they exist
    scrapedAuthor = scrapedSoup.find("p", attrs={"id": "author1"})
    scrapedAuthorCalling = scrapedSoup.find("p", attrs={"id": "author2"})
    if scrapedAuthor:
        print(f"Author: {scrapedAuthor.text}")
    if scrapedAuthorCalling:
        print(f"Calling: {scrapedAuthorCalling.text}\n\n")

    # Get the kicker
    scrapedKicker = scrapedSoup.find("p", attrs={"id": "kicker1"})
    if scrapedKicker:
        print(f"Kicker: {scrapedKicker.text}")
    oTalk = Talk(scrapedAuthor.text, scrapedTitle.text, scrapedKicker.text)

    # Get the talk's related content
    scrapedRelatedContent = scrapedSoup.findAll("a", attrs={"class": "scripture-ref"})
    if scrapedRelatedContent:
        oTalk.updateData(scrapedRelatedContent)
    else:
        print("related content not found")


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
    print(f"a tag: {link}")
    # Call a function that parses through the talk link for data that we want
    hrefStr = link["href"].upper()
    print(hrefStr)

    # Ignore any sessions links
    if ("/STUDY/GENERAL-CONFERENCE/2023/10/21EYRING?LANG=ENG" in hrefStr) or ("-SESSION" in hrefStr):
        print("Found a session to ignore\n")
        talksToRemove.append(link)
    else:
        webScraper(link["href"])

# Remove special session talk tiles
for talk in talksToRemove:
    all_talks.remove(talk)
print(len(all_talks))
