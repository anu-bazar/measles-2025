import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
df = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\Measles vaccination coverage.xlsx")

# --- Filter Conditions ---
df = df[
    (df['YEAR'].between(2000, 2024)) &
    (df['COVERAGE_CATEGORY'].str.upper() == 'OFFICIAL') &
    (df['ANTIGEN'].isin(['MCV1', 'MCV2'])) &
    (df['NAME'].isin(['United States of America', 'Germany']))
]

# Convert coverage to numeric, blank -> NaN
df['COVERAGE'] = pd.to_numeric(df['COVERAGE'], errors='coerce')

# Keep only required columns
df = df[['NAME', 'YEAR', 'ANTIGEN', 'COVERAGE']].copy()

# --- Plotting ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

for i, country in enumerate(['United States of America', 'Germany']):
    ax = axes[i]
    country_data = df[df['NAME'] == country]

    # Use seaborn lineplot, which breaks on NaN
    sns.lineplot(
        data=country_data,
        x='YEAR',
        y='COVERAGE',
        hue='ANTIGEN',
        ax=ax,
        linewidth=2,
        marker='o',
        palette='Set1'
    )

    ax.axhline(95, color='red', linestyle='--', label='95% Threshold')
    ax.set_title(f"{country}: MCV1 vs. MCV2")
    ax.set_xlabel("Year")
    if i == 0:
        ax.set_ylabel("Coverage (%)")
    else:
        ax.set_ylabel("")
    ax.legend()

plt.suptitle("MCV1 and MCV2 Coverage (2014–2024, OFFICIAL): U.S. and Germany", fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
