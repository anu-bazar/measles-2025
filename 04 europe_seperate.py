import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
df = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\Measles vaccination coverage.xlsx")

# List of European countries to keep
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
    'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
    'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
    'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
    'Switzerland', 'United Kingdom'
]

# --- Filter Conditions ---
df = df[
    (df['YEAR'].between(2000, 2024)) &
    (df['COVERAGE_CATEGORY'].str.upper() == 'OFFICIAL') &
    (df['ANTIGEN'] == 'MCV1') &
    (df['NAME'].isin(european_countries))
]

# Convert coverage to numeric, blank -> NaN
df['COVERAGE'] = pd.to_numeric(df['COVERAGE'], errors='coerce')

# Drop rows with missing coverage
df = df.dropna(subset=['COVERAGE'])

# --- Plotting ---
plt.figure(figsize=(18, 10))
sns.set(style="whitegrid")

sns.lineplot(
    data=df,
    x='YEAR',
    y='COVERAGE',
    hue='NAME',
    linewidth=1.5,
    marker='o',
    legend=False  # Set to True if you want to show the country legend
)

# Reference line
plt.axhline(95, color='red', linestyle='--', label='95% Herd Immunity Threshold')

plt.title("MCV1 Coverage in Europe (2000–2024, OFFICIAL)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Coverage (%)")
plt.tight_layout()
plt.show()
