import pandas as pd
import matplotlib.pyplot as plt

# Read data from three CSV files (replace with actual file paths)
df1 = pd.read_csv('../csv/all_mAP50_values_with_index_30N.csv')
df2 = pd.read_csv('../csv/all_mAP50_values_with_index_60N.csv')
df3 = pd.read_csv('../csv/all_mAP50_values_with_index_90N.csv')
df4 = pd.read_csv('../csv/all_mAP50_values_with_index_RandomN.csv')
df5 = pd.read_csv('../csv/all_mAP50_values_with_index_NoneN.csv')

# Create line plots for each dataset
plt.plot(df1['Index'], df1['mAP50'], label='CS_30_A')
plt.plot(df2['Index'], df2['mAP50'], label='CS_60_A')
plt.plot(df3['Index'], df3['mAP50'], label='CS_90_A')
plt.plot(df4['Index'], df4['mAP50'], label='CS_Rand_A')
plt.plot(df5['Index'], df5['mAP50'], label='CS_None_A')

# Customize the plot
plt.xlabel('Used Data')
plt.ylabel('mAP50')

plt.grid(True)
plt.xticks(range(0, 220, 20))
#plt.xticks(range(0, 11000, 1000))
# Add a custom legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('../graphs/compare_Epochs_306090N.png')