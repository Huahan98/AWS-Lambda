 provider "aws" {
   region = "us-east-1"
 }

 resource "aws_lambda_function" "example" {
   function_name = "pythonHelloWorld"
   s3_bucket = "python-function"
   s3_key    = "v1.0.0/pythonFunction.zip"

   handler = "HelloWorld.lambda_handler"
   runtime = "python3.6"

   role = aws_iam_role.lambda_exec.arn
 }

resource "aws_iam_role" "lambda_exec"{
  name = "serverless-example-lambda"
  assume_role_policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
     {
       "Action": "sts:AssumeRole",
       "Principal":{
         "Service": "lambda.amazonaws.com"
       },
       "Effect": "Allow",
       "Sid": ""
     }
   ]
}
  EOF
}
