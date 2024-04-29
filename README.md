# CI/CD Project: Lambda Function Deployment

![Terraform](https://img.shields.io/badge/Terraform-v0.14.7-blue?logo=terraform)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws)
![AWS CodeBuild](https://img.shields.io/badge/AWS-CodeBuild-yellow?logo=amazon-aws)
![Amazon ECR](https://img.shields.io/badge/Amazon-ECR-green?logo=amazon-aws)

This project demonstrates the implementation of a CI/CD pipeline for deploying AWS Lambda functions with Python libraries. By leveraging AWS services such as CodeBuild and ECR, developers can automate the process of updating Lambda functions, streamlining software development workflows.

## Project Overview

Continuous Integration and Continuous Deployment (CI/CD) practices have become essential in modern software development, facilitating automation of build, test, and deployment processes. This project focuses on integrating CI/CD pipelines with AWS Lambda, allowing developers to efficiently manage and deploy serverless functions.

## Features

- Automate building, testing, and deploying Lambda functions with CodeBuild
- Utilize Docker containers for packaging Lambda function code and dependencies
- Version control and collaboration using GitHub repositories
- Infrastructure provisioning and management with Terraform

## Prerequisites

- AWS account with Access and Secret Key
- Basic knowledge of AWS services
- Basic understanding of Git and GitHub
- Familiarity with Terraform for infrastructure as code

## Usage

1. Clone the GitHub repository containing the project code.
2. Configure AWS credentials and permissions for CodeBuild and ECR.
3. Set up a CodeBuild project to build and push Docker images to ECR.
4. Provision Lambda function infrastructure using Terraform.
5. Update Lambda function with the latest Docker image from ECR.
6. Test Lambda function functionality and monitor logs for errors.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.