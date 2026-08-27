# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 2018

@author: Francesco

"""

# ELABORAZIONE DATI JSON

import json
from pprint import pprint 

## carica un oggetto da un file
with open("Domini_min.json") as in_json:
    data_json = json.load(in_json)

pprint(data_json["listaDomini"][0])