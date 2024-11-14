import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
class_mAP50_df = pd.read_csv('../csv/class_mAP50_values.csv')

# Plotting the mAP50 values for each class
plt.figure(figsize=(10, 6))
for cls in class_mAP50_df.columns:
    plt.plot(class_mAP50_df.index + 1, class_mAP50_df[cls], label=cls)

# Adding title and labels
plt.title(' Central')
plt.xlabel('Iteration')
plt.ylabel('mAP50')
plt.legend()
plt.grid(True)
plt.xticks(range(1, 10, 1))

# Display the plot
plt.tight_layout()
plt.savefig('../graphs/class_mAP50_values_central.png')
