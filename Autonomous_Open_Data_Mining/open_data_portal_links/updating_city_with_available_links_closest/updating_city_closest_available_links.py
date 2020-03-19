# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:07:19 2019

@author: skans
"""

from Automated_Open_Data_Mining_Project.open_data_portal_links.google_search_for_links.google_search_results import (
        processing_links)
from Automated_Open_Data_Mining_Project.open_data_portal_links.checking_functioning_website.checking_functioning_website import (
        checking_functioning_website)
from difflib import get_close_matches
from datetime import datetime
from difflib import SequenceMatcher
import time

def updating_city_closest_available_links(links_dataset, number_of_search_results):
    available_links = links_dataset['website_url'].tolist() #Initial Dataset and the colun with Website URL
    now = datetime.now() #Curernt Date and Time
    dt_string = now.strftime("%d/%m/%Y")
    new_column_name_dt = "closest_updated_website_links"+ "(" + dt_string + ")" #Name of the new Column
    for index,row in links_dataset.iterrows():
        google_query = "City of " + getattr(row, 'city') + " " + (
                              getattr(row, "state_abbreviations") + "Open Data Portal") #Getting all the information to make a search query
        search_results = processing_links(google_query, number_of_search_results) #Getting the search results from t
        first_ten_link = search_results #First Ten Google Searches 
        orignal_link_in_data = getattr(row, 'website_url') # The orignal Website link
#        orignal_link_in_data_code =  checking_functioning_website(orignal_link_in_data)
#        if orignal_link_in_data_code == 200:
#            links_dataset.loc[index, 'Functionality_Orignal_Link'] = "Working"
#        else:
#            links_dataset.loc[index, 'Functionality_Orignal_Link'] = "Non Working" 
        closest_matched_link = get_close_matches(
               orignal_link_in_data, first_ten_link, n=1, cutoff=0.1)  #What is the closest link, this is a list
        closest_matched_link = closest_matched_link[0]  #The first link goes in here
#        closest_matched_link_code = checking_functioning_website(closest_matched_link)
        #if closest_matched_link_code == 200 :
        if closest_matched_link in available_links:
            links_dataset.loc[index, new_column_name_dt] = closest_matched_link
            links_dataset.loc[index, 'Indicator'] = "Yes link in orignal data"
#            links_dataset.loc[index, 'Functionality_Updated_link'] = "Working"
            seq = SequenceMatcher(a = orignal_link_in_data, b= closest_matched_link) # Matches the orignal link to the closest new search link
            links_dataset.loc[index,'Closest_Similarity Percentage'] = seq.ratio() #What is the similarity percentage
        else:
            links_dataset.loc[index, new_column_name_dt] = closest_matched_link
            links_dataset.loc[index, 'Indicator'] = "No, link is not orignal data"
#            links_dataset.loc[index, 'Functionality_Updated_link'] = "Working"
            seq = SequenceMatcher(a = orignal_link_in_data, b= closest_matched_link)
            links_dataset.loc[index,'Closest_Similarity Percentage'] = seq.ratio()
        #else:
            #links_dataset.loc[index, 'Functionality_Updated_link'] = "Not Working"
    return links_dataset
    