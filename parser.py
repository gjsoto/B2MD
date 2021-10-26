#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:41:55 2021

@author: gabrielsoto
"""

import bibtexparser as btp

with open('bib_sample.bib') as f:
    bib_str = f.read()

bib_data = btp.loads(bib_str)

# in authors list, check first for "and" keyword. 
#    if no "and", split by ","