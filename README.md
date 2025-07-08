# MEASLES
Last updated: JULY 2025

Data sources: 
https://immunizationdata.who.int/global/wiise-detail-page/measles-reported-cases-and-incidence
Data Description: 1980-2024 only per country, deleted metadata sheets.
Saved to measles-allcountry.xlsx

https://population.un.org/wpp/downloads?folder=Standard%20Projections&group=CSV%20format 
Data Description: 'Time', 'Location', 'LocTypeName', 'PopTotal' columns taken if 'Variant' field was Zero Migration or Medium, AND 'LocTypeName' was 'Country/Area' within Time of 1980-2024.
Used throughout the Normalized Code and 00 population.py

https://immunizationdata.who.int/global/wiise-detail-page/measles-vaccination-coverage?GROUP=Countries&ANTIGEN=MCV1&YEAR=&CODE= 
Data Description: Official Coverage, All Countries, 1st dose, Second Dose, from 1980-2024
Cleaned with R and Python; analyzed with Python.


