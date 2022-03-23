terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws",
      version = "~> 3.27"
    }
  }
  # backend "s3" {
  #   region  = "ap-southeast-1"
  #   profile = "srvadm"
  #   bucket = "tf_demo_bucket"
  # }
}

provider "aws" {
  profile = "srvadm"
  region  = "ap-southeast-1"
}

#dynamodb

resource "aws_dynamodb_table" "_" {
  name           = "tf_sam_todo_table"
  hash_key       = "id"
  read_capacity  = 1
  write_capacity = 1

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_sqs_queue" "_" {
  name                      = "rf_sam_todo_queue"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  # redrive_policy = jsonencode({
  #   deadLetterTargetArn = aws_sqs_queue.terraform_queue_deadletter.arn
  #   maxReceiveCount     = 4
  # })
  # redrive_allow_policy = jsonencode({
  #   redrivePermission = "byQueue",
  #   sourceQueueArns   = ["${aws_sqs_queue.terraform_queue_deadletter.arn}"]
  # })

  tags = {
    Environment = "production"
  }
}

module "lambda_api_todo" {
  source = "./modules/lambda_api_todo"

  environment       = var.environment
  region            = var.region
  resource_tag_name = var.resource_tag_name

  lambda_name       = "tf-sam-lambda-todo-handler"
  api_name          = "tf-sam-api-todo"
  queue_arn         = aws_sqs_queue._.arn
  dynamo_table_arn  = aws_dynamodb_table._.arn
  queue_url         = aws_sqs_queue._.url
  dynamo_table_name = aws_dynamodb_table._.name
}

module "lambda_persist_todo" {
  source = "./modules/lambda_persist_todo"

  environment       = var.environment
  region            = var.region
  resource_tag_name = var.resource_tag_name

  lambda_name       = "tf-sam-lambda-todo-persist"
  dynamo_table_arn  = aws_dynamodb_table._.arn
  source_arn        = aws_sqs_queue._.arn
  dynamo_table_name = aws_dynamodb_table._.name
}
