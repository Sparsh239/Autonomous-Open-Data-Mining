# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:58:00 2019

@author: skans
"""

import pandas as pd

def dataset_divison_links_nolinks(data):
    no_links_dataset = data[pd.isna(data['website_url'])] #Constants
    links_dataset = data.dropna()
    return no_links_dataset, links_dataset
