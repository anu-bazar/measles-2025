import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:\\Users\\anuba\\Documents\\GitHub\\Medium\\Measles-March\\measles-allcountry.xlsx") 
df = data.drop(columns=['Disease'])

print(df)

# OUTPUT:
#                   Country / Region  2024    2023    2022   2021 2020   2019    2018  ...    1987    1986    1985    1984    1983    1982     1981    1980
# 0                      Afghanistan   NaN   2,792   5,166  2,900  640    353   2,012  ...  10,357   8,107  14,457  16,199  18,808  20,320   31,107  32,455
# 1                          Albania   NaN      13       1    NaN    4    488   1,469  ...       0       0       0       0      17       3      NaN     NaN
# 2                          Algeria   NaN     203      47    NaN  NaN  2,585   3,356  ...   2,500   3,975  20,114  22,553  22,126  29,584   20,849  15,527
# 3                   American Samoa   NaN     NaN     NaN    NaN  NaN    NaN     NaN  ...       1       2      28       0       0       2        3      16
# 4                          Andorra   NaN       0       0      0    0      0       0  ...     NaN     NaN     NaN     NaN     NaN     NaN      NaN     NaN
# ..                             ...   ...     ...     ...    ...  ...    ...     ...  ...     ...     ...     ...     ...     ...     ...      ...     ...
# 210              Wallis and Futuna   NaN     NaN     NaN    NaN  NaN    NaN       0  ...     NaN     NaN     NaN       4      65      87       18     342
# 211                          Yemen   NaN  49,755  23,941  4,904  298  1,161  10,640  ...  17,408  15,596  27,997  39,713  33,348  24,482   21,355  18,020
# 212                         Zambia   NaN   5,653   1,755     55  237     15      11  ...  14,793  23,866  51,000  36,881  51,140  73,499  184,210  98,659
# 213                       Zimbabwe   NaN   5,532   5,532    282    3      4       1  ...  17,675  20,388  22,290  21,662  36,253   4,941    4,995  23,650
# 214  Exported: 2025-31-3 14:12 UTC   NaN     NaN     NaN    NaN  NaN    NaN     NaN  ...     NaN     NaN     NaN     NaN     NaN     NaN      NaN     NaN