# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:19:57 2019

@author: skans
"""

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re   
import requests
import urllib
import pandas as pd

def creating_search_query(query, number):
    search_query = query
    search_query = urllib.parse.quote_plus(search_query) # Format into URL encoding
    number_result = number
    print("Search Query", search_query)
    print("Number Result", number_result)
    return search_query, number_result


def extracting_query_information(search_query, number_result):
    ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + search_query + "&num=" + str(number_result)
    response = requests.get(google_url, {"User-Agent": ua.random}) #Constants
    soup = BeautifulSoup(response.text, "html.parser") #Constants
    result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'}) #Constants
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href = True) #Constants
            title = r.find('div', attrs={'class':'vvjwJb'}).get_text() #Constants
            description = r.find('div', attrs={'class':'s3v9rd'}).get_text() #Constants
            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '': 
                links.append(link['href']) #Constants
                titles.append(title)
                descriptions.append(description)
        # Next loop if one element is not present
        except:
            continue
    return links, titles, descriptions

def clean_result_links(links, titles, descriptions):
    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa',l)
    
        # Anything that doesn't fit the above pattern will be removed
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))
    
    # Remove the corresponding titles & descriptions
#    for x in to_remove:
#        del titles[x]
#        del descriptions[x]
    return clean_links

def processing_links(search_query, number):
    search_query, number_result = creating_search_query(search_query, number)
    links, titles, descriptions = extracting_query_information(search_query, number_result)
    clean_links = clean_result_links(links, titles, descriptions)
    return clean_links


    