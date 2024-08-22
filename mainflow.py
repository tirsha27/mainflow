import pandas as pd
threshold_value=4
dataset = pd.read_csv("D:\\powerBi\\sampledata\\Book1.csv")
filtered_df = dataset[dataset['Rating'] > threshold_value]
df_filled = filtered_df.fillna(0)
summary_stats = df_filled.describe()

print(filtered_df.head())
print(summary_stats)
