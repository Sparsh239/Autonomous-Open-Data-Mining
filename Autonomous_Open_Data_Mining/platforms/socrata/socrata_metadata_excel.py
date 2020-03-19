# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:57:09 2020

@author: skans
"""

import pandas as pd
import numpy as np
from sodapy import Socrata


def socrata_metadata_excel(socrata_dataset, authentication_token):
    print(socrata_dataset.info())
    socrata = remove_characters(socrata_dataset)
    list_datasets = []
    for index, row in socrata.iterrows():
        website_link = getattr(row, 'website_url')
        print("Link:", website_link)
        client = Socrata(website_link, authentication_token)
        print(getattr(row, 'city'))
        dataframe = pd.DataFrame(client.datasets())
        resource = dataframe['resource'].apply(pd.Series)
        print("Resource Columns:",resource.columns)
        classification = dataframe['classification'].apply(pd.Series)
        print("\n Classification Columns:",classification.columns)
        link = dataframe['link'].apply(pd.Series)
        print("\n Links Columns:", link.columns)
        metadata = dataframe['metadata'].apply(pd.Series)
        print("\n Metadata Columns:", metadata.columns)
        owner = dataframe['owner'].apply(pd.Series)
        print("\n Owner Columns:",owner.columns )
        permalink = dataframe['permalink'].apply(pd.Series)
        print("\n Permalink Columns:", permalink.columns)
        print(" All Function are working")
        final_dataset = pd.concat([resource, classification, link, metadata, owner, permalink], axis=1)
        list_datasets.append(final_dataset)
    excel_dataset = pd.concat(list_datasets, axis=0)
    return excel_dataset


def remove_characters(socrata):
    socrata['website_url'] = socrata['website_url'].str.replace('https://', '')
    socrata['website_url'] = socrata['website_url'].str.replace('http://', '')
    socrata['website_url'] = socrata['website_url'].str.replace('/', '')
    return socrata
