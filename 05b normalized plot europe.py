import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter

# AES MASTER styling
plt.style.use('seaborn-v0_8-whitegrid')
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['axes.linewidth'] = 0.8
mpl.rcParams['axes.edgecolor'] = '#888888'
mpl.rcParams['grid.linewidth'] = 0.6
mpl.rcParams['grid.alpha'] = 0.3

# === Load measles data ===
data = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\measles-allcountry.xlsx")
df = pd.DataFrame(data)
df = df.drop(columns=['Disease'])
df = df.drop([214])  # drop problematic row

def clean_and_convert(x):
    if isinstance(x, str):
        return pd.to_numeric(x.replace(',', ''), errors='coerce')
    return pd.to_numeric(x, errors='coerce')

year_columns = df.columns[1:]
df[year_columns] = df[year_columns].applymap(clean_and_convert)
df.fillna(0, inplace=True)

# European countries list
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 
    'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 
    'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 
    'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 
    'Switzerland', 'Ukraine', 'United Kingdom'
]

# Filter measles data for Europe only
df_europe = df[df['Country / Region'].isin(european_countries)].copy()

# === Load population data ===
pop_df = pd.read_csv('C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\WPP2024_TotalPopulationBySex.csv', low_memory=False)

# Filter population data
pop_filtered = pop_df[
    (pop_df['LocTypeName'] == 'Country/Area') &
    (pop_df['Variant'] == 'Medium') & 
    (pop_df['Time'] >= 1980) &
    (pop_df['Time'] <= 2024) &
    (pop_df['Location'].isin(european_countries))
]

# Select and rename columns
pop_filtered = pop_filtered[['Time', 'Location', 'PopTotal']]
pop_filtered.rename(columns={'Location': 'Country / Region', 'Time': 'Year'}, inplace=True)

# === ✅ FIX: Convert PopTotal from thousands to actual count ===
pop_filtered['PopTotal'] *= 1000

# Melt measles dataframe
df_melted = df_europe.melt(id_vars=['Country / Region'], value_vars=year_columns,
                           var_name='Year', value_name='Cases')
df_melted['Year'] = df_melted['Year'].astype(int)

# Merge measles and population data
merged = pd.merge(df_melted, pop_filtered, how='inner', on=['Country / Region', 'Year'])

# Calculate incidence
merged['Cases_per_100k'] = merged['Cases'] / merged['PopTotal'] * 100_000

# Aggregate totals by year
agg = merged.groupby('Year').agg({'Cases': 'sum', 'PopTotal': 'sum'}).reset_index()
agg['Cases_per_100k'] = agg['Cases'] / agg['PopTotal'] * 100_000

# === Plotting ===
years = agg['Year'].values
cases_per_100k = agg['Cases_per_100k'].values

fig, ax = plt.subplots(figsize=(12, 7.5), dpi=150)

ax.plot(years, cases_per_100k, marker='o', markersize=6,
        color='#1f77b4', linewidth=2.5, label='European Cases per 100,000')
ax.fill_between(years, 0, cases_per_100k, alpha=0.3, color='#9ecae1')

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.1f}'))

xticks_positions = np.arange(0, len(years), 5)
ax.set_xticks(years[xticks_positions])
ax.set_xticklabels([str(years[i]) for i in xticks_positions])

plt.title('European Measles Cases per 100,000 Population (1980–2024)',
          fontsize=18, fontweight='bold', pad=20, color='#333333')
plt.xlabel('Year', fontsize=12, labelpad=10, color='#555555')
plt.ylabel('Cases per 100,000', fontsize=12, labelpad=10, color='#555555')

fig.text(0.95, 0.02, 'Data: WHO & UN Population Division', fontsize=8, color='#bbbbbb',
         ha='right', va='bottom')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=10, colors='#555555')
fig.patch.set_facecolor('#fafafa')
ax.set_facecolor('#fafafa')

ax.legend(loc='upper right', frameon=True, framealpha=0.9, facecolor='white', edgecolor='#dddddd')

plt.tight_layout()
plt.subplots_adjust(bottom=0.12, top=0.9)
plt.show()
