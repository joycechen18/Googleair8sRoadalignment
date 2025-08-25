import pandas as pd
df = pd.read_csv('H:\Jiayao\Data8sMedian_20230830.csv')
df = df.iloc[:, 27:]
df = df.applymap(lambda x: str(x).replace('[', '').replace(']', '') if isinstance(x, str) else x)
print(df)
df.to_excel("Coordinates.xlsx", index=False, sheet_name="Cleaned Data")