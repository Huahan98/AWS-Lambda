 provider "aws" {
   region = "us-east-1"
 }

resource "aws_lambda_function" "holiday" {
   function_name = "pythonHelloHoliday"
   s3_bucket = "python-function"
   s3_key    = "v2/Holiday.zip"

   handler = "Holiday.lambda_handler"
   runtime = "python3.6"

   role = aws_iam_role.lambda_exec_holiday.arn
}


resource "aws_iam_role" "lambda_exec_holiday"{
  name = "serverless-holiday-response"
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


resource "aws_lambda_permission" "apigw" {
   statement_id  = "AllowAPIGatewayInvoke"
   action        = "lambda:InvokeFunction"
   function_name = aws_lambda_function.holiday.function_name
   principal     = "apigateway.amazonaws.com"

   # The "/*/*" portion grants access from any method on any resource
   # within the API Gateway REST API.
   source_arn = "${aws_api_gateway_rest_api.lambdaGateway.execution_arn}/*/*"
}
