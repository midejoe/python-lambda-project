import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def lambda_handler(event, context):
    # Create demo data
    d = {'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0],
         'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6],
         'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4],
         'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2],
         'target': [0, 0, 0, 0, 0]}
    df = pd.DataFrame(data=d)

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
