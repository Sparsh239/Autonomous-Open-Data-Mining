# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:54:34 2019

@author: skans
"""

from urllib.request import urlopen
import re

def checking_functioning_website(link):
    code = urlopen(link).getcode()
    return code