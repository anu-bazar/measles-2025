import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter

# --- Load measles data ---
measles_df = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\measles-allcountry.xlsx")
measles_df = measles_df.drop(columns=['Disease'])
measles_df = measles_df.drop([214])  # drop any irrelevant row

# Clean measles data: convert year columns to numeric
def clean_and_convert(x):
    if isinstance(x, str):
        return pd.to_numeric(x.replace(',', ''), errors='coerce')
    return pd.to_numeric(x, errors='coerce')

year_columns = measles_df.columns[1:]
measles_df[year_columns] = measles_df[year_columns].applymap(clean_and_convert)
measles_df.fillna(0, inplace=True)

# Sum total cases per year (globally)
total_cases = measles_df[year_columns].sum(axis=0, skipna=True)
total_cases.index = total_cases.index.astype(int)  # convert index to int years

# --- Load population data ---
pop_df = pd.read_csv('C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\WPP2024_TotalPopulationBySex.csv', low_memory=False)

# Filter population data for countries, desired variants, and year range
pop_filtered = pop_df[
    (pop_df['LocTypeName'] == 'Country/Area') &
    (pop_df['Variant'].isin(['Zero migration', 'Medium'])) &
    (pop_df['Time'] >= 1980) &
    (pop_df['Time'] <= 2024)
]

# Sum total population globally per year
pop_by_year = pop_filtered.groupby('Time')['PopTotal'].sum()

# Confirm population unit (PopTotal is in thousands based on your example)
# Convert to absolute numbers (multiply by 1000)
pop_by_year = pop_by_year * 1000

# Ensure years match between measles and population
common_years = total_cases.index.intersection(pop_by_year.index)
total_cases = total_cases.loc[common_years]
pop_by_year = pop_by_year.loc[common_years]

# Calculate incidence per 100,000 people
incidence_per_100k = (total_cases / pop_by_year) * 100000

# --- Plot ---
plt.style.use('seaborn-v0_8-whitegrid')
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['axes.linewidth'] = 0.8
mpl.rcParams['axes.edgecolor'] = '#888888'
mpl.rcParams['grid.linewidth'] = 0.6
mpl.rcParams['grid.alpha'] = 0.3

fig, ax = plt.subplots(figsize=(12, 7.5), dpi=150)

years = list(common_years)

ax.plot(years, incidence_per_100k, marker='o', markersize=6,
        color='#1f77b4', linewidth=2.5, label='Global Measles per 100,000 people')

ax.fill_between(years, 0, incidence_per_100k, alpha=0.3, color='#9ecae1')

def human_readable_numbers(x, pos):
    return f'{x:.2f}'

ax.yaxis.set_major_formatter(FuncFormatter(human_readable_numbers))

# 5 year breaks on x-axis
xticks_positions = np.arange(0, len(years), 5)
xticks_labels = [str(years[i]) for i in xticks_positions]
ax.set_xticks([years[i] for i in xticks_positions])
ax.set_xticklabels(xticks_labels)

plt.title('Global Measles Incidence per 100,000 People (1980-2024)', fontsize=18, fontweight='bold', pad=20, color='#333333')
plt.xlabel('Year', fontsize=12, labelpad=10, color='#555555')
plt.ylabel('Cases per 100,000', fontsize=12, labelpad=10, color='#555555')

fig.text(0.95, 0.02, 'Data: WHO & UN Population Division', fontsize=8, color='#bbbbbb', ha='right', va='bottom')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=10, colors='#555555')

fig.patch.set_facecolor('#fafafa')
ax.set_facecolor('#fafafa')

ax.legend(loc='upper right', frameon=True, framealpha=0.9, facecolor='white', edgecolor='#dddddd')

plt.tight_layout()
plt.subplots_adjust(bottom=0.12, top=0.9)

plt.show()
