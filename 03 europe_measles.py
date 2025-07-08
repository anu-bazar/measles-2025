import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter

# AES MASTER
plt.style.use('seaborn-v0_8-whitegrid')
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['axes.linewidth'] = 0.8
mpl.rcParams['axes.edgecolor'] = '#888888'
mpl.rcParams['grid.linewidth'] = 0.6
mpl.rcParams['grid.alpha'] = 0.3

# Data load
data = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\measles-allcountry.xlsx") 
df = pd.DataFrame(data)

# Data cleaning
df = df.drop(columns=['Disease'])
df = df.drop([214])

# European countries list - EUROPE
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

# Filter data for European countries only
df_europe = df[df['Country / Region'].isin(european_countries)]

# Numerical columns
def clean_and_convert(x):
    if isinstance(x, str):
        return pd.to_numeric(x.replace(',', ''), errors='coerce')
    return pd.to_numeric(x, errors='coerce')

year_columns = df_europe.columns[1:]
df_europe[year_columns] = df_europe[year_columns].applymap(clean_and_convert)
df_europe.fillna(0, inplace=True)

# 'Total' calculated for every column
numeric_columns = df_europe.select_dtypes(include=['number']).columns
total_values = df_europe[numeric_columns].sum(axis=0, skipna=True)

# 'Total' row creation
total_row = {'Country / Region': 'Total'}
total_row.update(total_values.to_dict())
df_europe = pd.concat([df_europe, pd.DataFrame([total_row])], ignore_index=True)

# MASTER VISUALIZATION
total_row = df_europe[df_europe['Country / Region'] == 'Total']
years = [int(year) for year in total_row.columns[1:]]
total_values = total_row.iloc[0, 1:].values
total_values = np.array(total_values, dtype=float)
fig, ax = plt.subplots(figsize=(12, 7.5), dpi=150) 

# MAIN LINE
main_line = ax.plot(years, total_values, marker='o', markersize=6, 
                   color='#1f77b4', linewidth=2.5, 
                   label='European Cases')

# FILL
ax.fill_between(years, 0, total_values, alpha=0.3, color='#9ecae1')

# ANNOTATION
max_year_idx = np.argmax(total_values)
min_year_idx = np.argmin(total_values[10:]) + 10 

# Max point
ax.annotate(f'{int(total_values[max_year_idx]):,}',
            xy=(years[max_year_idx], total_values[max_year_idx]),
            xytext=(10, 15), textcoords='offset points',
            fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='-', lw=1.2, color='#555555'))

# Min point
ax.annotate(f'{int(total_values[min_year_idx]):,}',
            xy=(years[min_year_idx], total_values[min_year_idx]),
            xytext=(10, -15), textcoords='offset points',
            fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='-', lw=1.2, color='#555555'))

# Formatting number to human readable
def human_readable_numbers(x, pos):
    if x >= 1000000:
        return f'{x/1000000:.1f}M'
    elif x >= 1000:
        return f'{x/1000:.0f}K'
    else:
        return f'{x:.0f}'

ax.yaxis.set_major_formatter(FuncFormatter(human_readable_numbers))

# 5 year breaks
xticks_positions = np.arange(0, len(years), 5)
xticks_labels = [str(years[i]) for i in xticks_positions]
ax.set_xticks([years[i] for i in xticks_positions])
ax.set_xticklabels(xticks_labels)

# Further styling for Title, axis-labels
plt.title('Measles Cases in Europe (1980-2024)', 
          fontsize=18, fontweight='bold', pad=20, color='#333333')
plt.xlabel('Year', fontsize=12, labelpad=10, color='#555555')
plt.ylabel('Number of Cases', fontsize=12, labelpad=10, color='#555555')

# Data source label
fig.text(0.95, 0.02, 'Data: WHO - Measles reported cases and incidences', 
         fontsize=8, color='#bbbbbb', ha='right', va='bottom')

# 2007 annotation
annotation_text = "Lowest point in 2007\n5 years earlier than global trends."
fig.text(0.60, 0.25, annotation_text, 
         fontsize=9, color='#555555', ha='left', va='bottom')

# Trend periods for Pre-vax era and Recent emergence
first_year, last_year = years[0], years[-1]
ax.axvspan(first_year, years[10], alpha=0.1, color='red', label='_nolegend_')
ax.axvspan(years[30], last_year, alpha=0.1, color='orange', label='_nolegend_')
fig.text(0.2, 0.75, "Pre-vaccination era", fontsize=12, color='#aa5555')
fig.text(0.8, 0.75, "Recent emergence", fontsize=12, color='#aa7755')

# AES
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=10, colors='#555555')

# BG COLOR
fig.patch.set_facecolor('#fafafa')
ax.set_facecolor('#fafafa')

# LEGEND
legend = ax.legend(loc='upper right', frameon=True, framealpha=0.9,
                  facecolor='white', edgecolor='#dddddd')

# LAYOUT
plt.tight_layout()
plt.subplots_adjust(bottom=0.12, top=0.9)

# Show the plot
plt.show()
