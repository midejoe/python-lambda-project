#data for the python file
data "archive_file" "lambda" {
  type        = "zip"
  source_file = "lambda_function.py"
  output_path = "lambda_function_payload.zip"
}

#lambda function resource
resource "aws_lambda_function" "python_lambda_function" {
  architectures = [
    "x86_64",
  ]
  filename      = "lambda_function_payload.zip"
  function_name = "pandas-function"
  handler       = "lambda_function.lambda_handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  layers                         = []
  memory_size                    = 128
  package_type                   = "Zip"
  reserved_concurrent_executions = -1
  role                           = aws_iam_role.test_role.arn
  runtime                        = "python3.11"
  skip_destroy                   = false


  tags     = {}
  tags_all = {}
  timeout  = 3


  ephemeral_storage {
    size = 512
  }

  logging_config {
    log_format = "Text"
    log_group  = "/aws/lambda/pandas-function"
  }

  tracing_config {
    mode = "PassThrough"
  }
}

# aws_iam_role.test_role:
resource "aws_iam_role" "test_role" {
  assume_role_policy = jsonencode(
    {
      Statement = [
        {
          Action = "sts:AssumeRole"
          Effect = "Allow"
          Principal = {
            Service = "lambda.amazonaws.com"
          }
        },
      ]
      Version = "2012-10-17"
    }
  )
  force_detach_policies = false


  max_session_duration = 3600
  name                 = "pandas-function-role-y2l0sfbp"
  path                 = "/service-role/"
  tags                 = {}
  tags_all             = {}
}