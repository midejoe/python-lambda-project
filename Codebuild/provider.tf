#terraform provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.44.0"
    }
  }
}

#aws provider
provider "aws" {
  profile = "vscode"
  region  = "us-east-1"
}