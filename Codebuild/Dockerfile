# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the code and requirements.txt file into the container
COPY lambda_function.py requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Lambda function
CMD ["python", "lambda_function.py"]
