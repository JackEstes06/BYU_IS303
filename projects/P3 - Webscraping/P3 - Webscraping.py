# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
# Project 3 -

import pandas as pd
from bs4 import BeautifulSoup
import requests


def webScraper(urlPath):
    # Grab the href of the talk link
    print(f"Href: {urlPath}\n")

    # Navigate to the talk's link and scrape the html for data
    oScrapeResponse = requests.get(f"{baseURL}{urlPath}")
    scrapedSoup = BeautifulSoup(oScrapeResponse.text, 'html.parser')

    # Get the talk's title if it exists
    scrapedTitle = scrapedSoup.find("h1", attrs={"id": "title1"})
    if scrapedTitle:
        # Ignore the sustaining sessions otherwise continue to scrape
        if "Sustaining of General Authorities" in scrapedTitle.text:
            return
        else:
            print(f"Title: {scrapedTitle.text}")

    # Get the talk's speaker and calling if they exist
    scrapedAuthor = scrapedSoup.find("p", attrs={"id": "author1"})
    scrapedAuthorCalling = scrapedSoup.find("p", attrs={"id": "author2"})
    if scrapedAuthor:
        print(f"Author: {scrapedAuthor.text}")
    if scrapedAuthorCalling:
        print(f"Calling: {scrapedAuthorCalling.text}\n\n")


# Base URL
baseURL = "https://www.churchofjesuschrist.org"
# Store the response object for the website we want to scrape data from
oResponse = requests.get(f"{baseURL}/study/general-conference/2023/10?lang=eng")

# Create a collection of all the HTML tags and data
soup = BeautifulSoup(oResponse.text, 'html.parser')

# Search for specific tags that have the data you want to process
all_talks = soup.findAll("a", attrs={"class": "list-tile"})

# print(talk_links)
for link in all_talks:
    print(f"{link}")
    # Call a function that parses through the talk link for data that we want
    hrefStr = link["href"].upper()
    print(hrefStr)

    # Ignore any sessions links
    if ("AFTERNOON-SESSION" in hrefStr) or ("MORNING-SESSION" in hrefStr):
        print("Found a session to ignore")
    else:
        webScraper(link["href"])
print(len(all_talks))
