# MEASLES  
**Last updated:** July 2025

---

### Data Sources & Descriptions

1. **Measles Reported Cases and Incidence**  
   URL: https://immunizationdata.who.int/global/wiise-detail-page/measles-reported-cases-and-incidence  
   - Data range: 1980–2024 (per country)  
   - Metadata sheets removed  
   - Saved as: measles-allcountry.xlsx

2. **Population Data (UN World Population Prospects)**  
   URL: https://population.un.org/wpp/downloads?folder=Standard%20Projections&group=CSV%20format  
   - Selected columns: Time, Location, LocTypeName, PopTotal  
   - Filters applied:  
     - Variant = Zero Migration or Medium  
     - LocTypeName = Country/Area  
     - Time: 1980–2024  
   - Used throughout the Normalized Code and 00_population.py

3. **Measles Vaccination Coverage**  
   URL: https://immunizationdata.who.int/global/wiise-detail-page/measles-vaccination-coverage?GROUP=Countries&ANTIGEN=MCV1&YEAR=&CODE=  
   - Official coverage data, all countries  
   - Includes: 1st dose and 2nd dose, 1980–2024  
   - Data cleaning: R and Python  
   - Analysis: Python

---

### Related Article

Read the corresponding article here:  
https://medium.com/@anubazarragchaa_25172/measles-cases-are-on-the-rise-b36d058e5466
