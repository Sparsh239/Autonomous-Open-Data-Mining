                                                                                                                                                                                                                                                                                                                                                                                                                                                                            # -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:09:41 2020

@author: skans
"""

import numpy as np
import pandas as pd

def distributing_links_no_platforms(links_dataset):
    socrata = links_dataset[links_dataset['platform'] == 'socrata']
    ckan = links_dataset[links_dataset['platform'] == 'ckan']
    junar = links_dataset[links_dataset['platform'] == 'junar']
    opendatasoft = links_dataset[links_dataset['platform'] == 'opendatasoft']
    opengov = links_dataset[links_dataset['platform'] == 'opengov']
    ownapi = links_dataset[links_dataset['platform'] == 'ownapi']
    datasd = links_dataset[links_dataset['platform'] == 'datasd']
    return socrata,ckan,junar,opendatasoft,opengov,ownapi,datasd
    