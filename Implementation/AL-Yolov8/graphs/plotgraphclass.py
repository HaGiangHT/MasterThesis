import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from the CSV file
class_mAP50_df = pd.read_csv('../../ServerClient/csv/class_mAP50_values_RandomF.csv')

# Plotting the mAP50 values for each class
plt.figure(figsize=(10, 6))
for cls in class_mAP50_df.columns:
    plt.plot(class_mAP50_df.index + 1, class_mAP50_df[cls], label=cls)

# Adding title and labels
plt.title('CS_Rand_AF')
plt.xlabel('Iteration')
plt.ylabel('mAP50')
plt.legend()
plt.grid(True)
plt.xticks(range(1, 11, 1))
plt.yticks(np.arange(0.3, 0.85, 0.05))

# Display the plot
plt.tight_layout()
plt.savefig('../graphs/class_mAP50_values_RandomAF.png')
