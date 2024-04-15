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

# import pandas as pd
# import numpy as np

# def generate_random_dataframe(num_rows=10):
#     """
#     Generate a DataFrame with random data.

#     Parameters:
#         num_rows (int): Number of rows in the DataFrame.

#     Returns:
#         pd.DataFrame: DataFrame with random data.
#     """
#     data = {
#         'A': np.random.randint(0, 100, num_rows),
#         'B': np.random.rand(num_rows),
#         'C': np.random.choice(['X', 'Y', 'Z'], num_rows)
#     }
#     return pd.DataFrame(data)

# def perform_dataframe_operations(df):
#     """
#     Perform basic operations on the DataFrame.

#     Parameters:
#         df (pd.DataFrame): Input DataFrame.

#     Returns:
#         pd.DataFrame: Updated DataFrame with a new column 'D'.
#     """
#     # Display the DataFrame
#     print("Original DataFrame:")
#     print(df)

#     # Perform basic operations on the DataFrame
#     print("\nDataFrame Operations:")
#     print("Sum of column 'A':", df['A'].sum())
#     print("Mean of column 'B':", df['B'].mean())
#     print("Number of occurrences of each value in column 'C':")
#     print(df['C'].value_counts())

#     # Add a new column to the DataFrame
#     df['D'] = df['A'] * df['B']
#     print("\nUpdated DataFrame with a new column 'D':")
#     print(df)

# def handler(event, context):
#     """
#     Lambda handler function.

#     Parameters:
#         event: Event data passed to the handler.
#         context: Runtime information about the Lambda function execution.

#     Returns:
#         dict: Response object.
#     """
#     try:
#         # Generate random DataFrame
#         df = generate_random_dataframe()

#         # Perform DataFrame operations
#         perform_dataframe_operations(df)

#         # Return a response
#         return {
#             'statusCode': 200,
#             'body': 'Lambda function executed successfully'
#         }
#     except Exception as e:
#         # Log any errors
#         print("An error occurred:", str(e))
#         # Return an error response
#         return {
#             'statusCode': 500,
#             'body': 'Internal server error: ' + str(e)
#         }

import pandas as pd
import numpy as np

def generate_product_inventory(num_products=10):
    """
    Generate a DataFrame representing a product inventory with random data.

    Parameters:
        num_products (int): Number of products in the inventory.

    Returns:
        pd.DataFrame: DataFrame representing the product inventory.
    """
    # Generate random data for the product inventory
    product_ids = range(1, num_products + 1)
    product_names = [f"Product {i}" for i in product_ids]
    quantities = np.random.randint(1, 100, num_products)
    prices = np.random.uniform(10.0, 100.0, num_products)

    # Create the DataFrame
    data = {
        'ProductID': product_ids,
        'ProductName': product_names,
        'Quantity': quantities,
        'Price': prices
    }
    return pd.DataFrame(data)

def perform_product_operations(df):
    """
    Perform various operations on the product inventory DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame representing the product inventory.

    Returns:
        dict: Dictionary containing the results of the operations.
    """
    # Operations
    total_products = len(df)
    total_quantity = df['Quantity'].sum()
    average_price = df['Price'].mean()
    most_bought_product = df.loc[df['Quantity'].idxmax(), 'ProductName']
    highest_priced_product = df.loc[df['Price'].idxmax(), 'ProductName']

    # Results
    results = {
        'TotalProducts': total_products,
        'TotalQuantity': total_quantity,
        'AveragePrice': average_price,
        'MostBoughtProduct': most_bought_product,
        'HighestPricedProduct': highest_priced_product
    }
    return results

def handler(event, context):
    """
    Lambda handler function.

    Parameters:
        event: Event data passed to the handler.
        context: Runtime information about the Lambda function execution.

    Returns:
        dict: Response object.
    """
    try:
        # Generate product inventory DataFrame
        product_inventory = generate_product_inventory()

        # Perform various operations on the product inventory DataFrame
        results = perform_product_operations(product_inventory)

        # Log the results
        print("Product Inventory Operations:")
        for key, value in results.items():
            print(f"{key}: {value}")

        # Return a response
        return {
            'statusCode': 200,
            'body': 'Lambda function executed successfully'
        }
    except Exception as e:
        # Log any errors
        print("An error occurred:", str(e))
        # Return an error response
        return {
            'statusCode': 500,
            'body': 'Internal server error: ' + str(e)
        }


