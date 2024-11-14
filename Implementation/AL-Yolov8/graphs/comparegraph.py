import pandas as pd
import matplotlib.pyplot as plt

# Read data from three CSV files (replace with actual file paths)
df1 = pd.read_csv('../csv/all_mAP50_values_with_index.csv')
df2 = pd.read_csv('../../ServerClient/csv/all_mAP50_values_with_index_NoneN.csv')
df3 = pd.read_csv('../../ServerClient/csv/all_mAP50_values_with_index_None.csv')
# df4 = pd.read_csv('../csv/all_mAP50_values_with_index_RandomF.csv')
# df5 = pd.read_csv('../csv/all_mAP50_values_with_index_NoneF.csv')

# Create line plots for each dataset
plt.plot(df1['Index'], df1['mAP50'], label='Central')
plt.plot(df2['Index'], df2['mAP50'], label='CS_None_A')
plt.plot(df3['Index'], df3['mAP50'], label='CS_None_R')
# plt.plot(df4['Index'], df4['mAP50'], label='CSRandomF')
# plt.plot(df5['Index'], df5['mAP50'], label='CSNoneF')

# Customize the plot
plt.xlabel('Epochs')
plt.ylabel('mAP50')

plt.grid(True)

# Add a custom legend
plt.legend()

plt.xticks(range(0, 220, 20))
# Show the plot
plt.grid(True)
plt.savefig('../graphs/compare_Epochs_Central_None.png')