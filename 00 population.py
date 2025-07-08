import pandas as pd

df = pd.read_csv('C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\WPP2024_TotalPopulationBySex.csv', low_memory=False)

filtered_df = df[
    (df['LocTypeName'] == 'Country/Area') &
    (df['Variant'].isin(['Zero migration', 'Medium'])) &
    (df['Time'] >= 1980) &
    (df['Time'] <= 2024)
]

sub_df = filtered_df[['Time', 'Location', 'LocTypeName', 'PopTotal']]

# Sort by Location A-Z, then Time ascending
sub_df = sub_df.sort_values(by=['Location', 'Time'], ascending=[True, True])

print(sub_df.head())

"""        Time     Location   LocTypeName   PopTotal
451600  1980  Afghanistan  Country/Area  13169.311
451601  1981  Afghanistan  Country/Area  11937.581
451602  1982  Afghanistan  Country/Area  10991.378
451603  1983  Afghanistan  Country/Area  10917.982
451604  1984  Afghanistan  Country/Area  11190.221"""


