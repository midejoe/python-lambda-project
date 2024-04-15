# import pandas as pd
# import numpy as np

# def handler(event, context):
#     # Create a DataFrame with random data
#     data = {
#         'A': np.random.randint(0, 100, 10),
#         'B': np.random.rand(10),
#         'C': np.random.choice(['X', 'Y', 'Z'], 10)
#     }
#     df = pd.DataFrame(data)

#     # Display the DataFrame
#     print("Original DataFrame:")
#     print(df)

#     # Perform some basic operations on the DataFrame
#     print("\nDataFrame Operations:")
#     print("Sum of column 'A':", df['A'].sum())
#     print("Mean of column 'B':", df['B'].mean())
#     print("Number of occurrences of each value in column 'C':")
#     print(df['C'].value_counts())

#     # Add a new column to the DataFrame
#     df['D'] = df['A'] * df['B']
#     print("\nUpdated DataFrame with a new column 'D':")
#     print(df)

#     # Return a response (if this function is used in an AWS Lambda context)
#     return {
#         'statusCode': 200,
#         'body': 'Lambda function executed successfully'
#     }

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def handler(event, context):
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Split dataset into features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    return {
        'statusCode': 200,
        'body': f'Accuracy: {accuracy}'
    }

