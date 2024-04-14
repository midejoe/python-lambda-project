import pandas as pd
import numpy as np

# Create a DataFrame with random data
data = {
    'A': np.random.randint(0, 100, 10),
    'B': np.random.rand(10),
    'C': np.random.choice(['X', 'Y', 'Z'], 10)
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Perform some basic operations on the DataFrame
print("\nDataFrame Operations:")
print("Sum of column 'A':", df['A'].sum())
print("Mean of column 'B':", df['B'].mean())
print("Number of occurrences of each value in column 'C':")
print(df['C'].value_counts())

# Add a new column to the DataFrame
df['D'] = df['A'] * df['B']
print("\nUpdated DataFrame with a new column 'D':")
print(df)
