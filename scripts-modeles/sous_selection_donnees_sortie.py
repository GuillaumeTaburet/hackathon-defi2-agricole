# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 12:17:37 2025

@author: Brise_Fer
"""

import geopandas as gpd

# SHP région Occitanie
shp_occitanie = 'hackathon-defi2-agricole/shp_Occitanie/Occitanie_based_NUTS.shp' 
shp_data = # Data à analyser/représenter

shp_data_subset = shp_data.overlay(shp_occitanie, how = 'intersection')

'''
code intermédiaire
'''
# plot des frontières de l'Occitanie
shp_occitanie.boundary.plot(ax=ax, color='orange')
