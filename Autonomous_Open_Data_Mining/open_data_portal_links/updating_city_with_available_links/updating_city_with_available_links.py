# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:16:07 2019

@author: skans
"""
from Automated_Open_Data_Mining_Project.open_data_portal_links.google_search_for_links.google_search_results import (
        processing_links)
from datetime import datetime
from difflib import SequenceMatcher
import time



def updating_city_with_available_links(links_dataset, number_of_search_results):
    available_links = links_dataset['website_url'].tolist()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    new_column_name_dt = "updated_website_links"+ "(" + dt_string + ")"
    for index,row in links_dataset.iterrows():
        google_query = getattr(row, 'city') + " " + (
                              getattr(row, "state_abbreviations") + " City Open Data Portal")
        search_results = processing_links(google_query, number_of_search_results)
        first_link = search_results[0]
        orignal_link_in_data = getattr(row, 'website_url')
        if first_link in available_links:
            links_dataset.loc[index, new_column_name_dt] = first_link
            seq = SequenceMatcher(a = orignal_link_in_data, b= first_link)
            links_dataset.loc[index,'Similarity Percentage'] = seq.ratio()
        else:
            links_dataset.loc[index, new_column_name_dt] = first_link
            seq = SequenceMatcher(a = orignal_link_in_data, b= first_link)
            links_dataset.loc[index,'Similarity Percentage'] = seq.ratio()
    return links_dataset
            
        
        