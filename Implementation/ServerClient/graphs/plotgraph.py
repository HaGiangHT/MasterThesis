import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Load data from a CSV file
data = pd.read_csv('../csv/all_mAP50_values_with_index_30.csv')


x = data['Index']
y = data['mAP50']

# Plotting the line graph
plt.plot(x, y)

# Adding title and labels
plt.title('CS30')
plt.xlabel('Number of epochs')
plt.ylabel('mAP50')

#plt.xticks(range(1000, 11000, 1000))


# Display the plot
plt.grid(True)
plt.savefig('../graphs/mAP50xEpochs_central_30.png')
