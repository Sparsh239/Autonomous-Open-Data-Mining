# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:59:52 2019

@author: skans
"""
import os
import sys
import pandas as pd

sys.path.append('C:/Users/skans/Documents/Github/Research-Assistantship-')
from Automated_Open_Data_Mining_Project.platforms.distributing_links_on_platforms.distributing_links_on_platforms import (
    distributing_links_no_platforms)
from Automated_Open_Data_Mining_Project.platforms.socrata.socrata_metadata_excel import (
    socrata_metadata_excel)
from Automated_Open_Data_Mining_Project.platforms.CKAN.ckan_metadata_excel import Ckan
from Automated_Open_Data_Mining_Project.datasets.dataset_divison_links_nolinks.dataset_division_links_nolinks import \
    dataset_divison_links_nolinks
from Automated_Open_Data_Mining_Project.open_data_portal_links.updating_city_with_available_links.updating_city_with_available_links import (
    updating_city_with_available_links)
from Automated_Open_Data_Mining_Project.open_data_portal_links.updating_city_with_available_links_closest.updating_city_closest_available_links import (
    updating_city_closest_available_links)
from Automated_Open_Data_Mining_Project.open_data_portal_links.updating_city_with_no_available_links.updating_city_with_no_available_links import (
    updating_city_with_no_available_links)


def main():
    city_with_no_links = pd.read_csv("C://Users//skans//Desktop//Datasets//city_with_no_links.csv",
                                     encoding='unicode_escape')
    city_with_links = pd.read_csv("C://Users//skans//Desktop//Datasets//Saved_Datasets.csv", encoding='unicode_escape')
    arc_gis_links = pd.read_csv("C://Users//skans//Desktop//Datasets//arc_gis_datasets.csv", encoding='unicode_escape')
    socrata, ckan, junar, opendatasoft, opengov, ownapi, datasd = distributing_links_no_platforms(city_with_links) 
#    junar.to_csv("junar.csv")
    # ckan.to_csv("ckan.csv")
    print(ckan)
    ckan_dataset = Ckan(ckan)
    ckan_dataset.add_specific_characters()
    ckan_dataset.ckan_dataset_information()
#    ckan_datalinks_information.to_csv("ckan_dataset.csv")
    # socrata_authentication_token = "mGG8Ql7JuPvd1uZXhZYFSc3ls"
    # socrata_datalinks_information = socrata_metadata_excel(socrata, socrata_authentication_token)
    # socrata_datalinks_information.to_excel("C://Users//skans//Desktop//Datasets//Socrata_Datasets_Information.xlsx")


#
#    combined_links = pd.concat([city_with_links,arc_gis_links])
#    number_of_search_results = 10
#    available_links_dataset_updated = updating_city_closest_available_links(
#         combined_links, number_of_search_results)
#    available_links_dataset_updated.to_excel("C://Users//skans//Desktop//Datasets//Updated_Research_Assistantship_Dataset_Files_Available_links_data.xlsx")
#    updated_no_links_dataset = updating_city_with_no_available_links(available_links_dataset_updated,city_with_no_links,number_of_search_results)
#    available_links_dataset_updated.to_excel("C://Users//skans//Desktop//Datasets//Updated_Research_Assistantship_Dataset_Files_Available_links_data.xlsx")
#    updated_no_links_dataset.to_excel("C://Users//skans//Desktop//Datasets//Updated_Research_Assistantship_Dataset_Files_No_links_data.xlsx")

if __name__ == "__main__":
    main()
