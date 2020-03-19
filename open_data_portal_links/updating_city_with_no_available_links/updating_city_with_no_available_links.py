                                                                                                                                                                                                                                                                                # -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:33:52 2019

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

def updating_city_with_no_available_links(links_dataset,no_links_dataset, number_of_search_results):
    available_links = links_dataset['website_url'].tolist() #Initial Dataset and the colun with Website URL
    now = datetime.now() #Curernt Date and Time
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    new_column_name_dt = "closest_updated_website_links"+ "(" + dt_string + ")" #Name of the new Column
    for index,row in no_links_dataset.iterrows():
        google_query = "City of " + getattr(row, 'city') + " " + (
                              getattr(row, "state_abbreviations") + "Open Data Portal") #Getting all the information to make a search query
        search_results = processing_links(google_query, number_of_search_results) #Getting the search results from t
        first_ten_link = search_results #First Ten Google Searches 
        google_searched_link = first_ten_link[0]
#        orignal_link_in_data = getattr(row, 'website_url') # The orignal Website link
#        closest_matched_link = get_close_matches(
#               orignal_link_in_data, first_ten_link, n=1, cutoff=0.1)  #What is the closest link, this is a list
#        closest_matched_link = closest_matched_link[0]  #The first link goes in here
        if google_searched_link in available_links:
            no_links_dataset.loc[index, new_column_name_dt] = None
#            links_dataset.loc[index, 'Indicator'] = "Yes link in orignal data"
#            seq = SequenceMatcher(a = orignal_link_in_data, b= closest_matched_link) # Matches the orignal link to the closest new search link
#            links_dataset.loc[index,'Closest_Similarity Percentage'] = seq.ratio() #What is the similarity percentage
        else:
            no_links_dataset.loc[index, new_column_name_dt] = google_searched_link
#           no_links_dataset.loc[index, 'Indicator'] = "No, link is not orignal data"
#            seq = SequenceMatcher(a = orignal_link_in_data, b= closest_matched_link)
#            links_dataset.loc[index,'Closest_Similarity Percentage'] = seq.ratio()

    return no_links_dataset
    