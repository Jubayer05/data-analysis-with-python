import matplotlib
matplotlib.use('TkAgg')  # Set an interactive backend
import matplotlib.pyplot as plt

import pandas as pd

# Load the data
data = pd.read_csv('Salary_Data.csv')

# Plot the data
data.plot(kind='line', x="YearsExperience", y="Salary", marker="o", ls=":")

# Add labeling
plt.xlabel('Years of Experience')
plt.ylabel('Salary in Taka')
plt.title('Experience vs Salary')


# Save the plot as an image file
plt.show()

