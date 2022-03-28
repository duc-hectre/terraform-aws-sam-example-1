### Introduction

This is the sample project to describe how to initiate & provision a serverless platform on AWS cloud using Terraform & SAM.
The approach is:

- Use Terraform:
  - To initiate & provision all the required infrastructures such as IAM role, policy, lambda, sqs, dynamodb, code pipeline,...
  - Use AWS Code Pipeline to integrate with Terraform image in docker-hup for CI/CD action.
- Use SAM:
  - To develop, test & debug the source code of lambda function.
  - Build the lambda package used to deploy by Terraform.

### Sample architecture

This project is to build a simple Todo application which allow user to record their todo action with some simple description likes Todo, Desc & Status. The AWS structure is:

[](https://github.com/duc-hectre/duc-hectre/blob/main/TF-SAM-APPROACH-1.png?raw=true)

### Get started.

Regarding to this sample. The project structure looks like image below.

[](https://github.com/duc-hectre/duc-hectre/blob/main/tf_1_project_structure.png?raw=true)

In which, we have 3 main parts:

# Lambda Function part

First is the Lambda block which contains the definition of the lambda function including unit test, integration test if any. This is the main block for code logic which will be used to build the package & deploy to AWS Lambda.
If any new functions need to be develop, they will be define here.

# Terraform part

This is the part that contains all the terraform code to initiate & manage infrastructures needed for our application. All the services on AWS will be defined here such as Lambda function configuration, IAM Roles & policies, SQS, CloudWatch, AWS Code Pipeline,...

# SAM part

This is the part to defines SAM template which support us to run Lambda function locally for testing & debugging.
If any lambda function need to be debugged or troubleshooted, we create the corresponding a simple sam template and link the URI to the proper lambda code defined in Lambda Part, then configure the debug profiles to start debugging.
Try to keep the SAM template as simple as possible, mostly focus on Lambda config and input/trigger events of that lambda function only such as API gateway or SQS, cloudwatch. Regarding to details of configuration as well as surrounding services, they had already been defined in Terraform part.

Following the steps below to get the project start.

1. Install prerequisites

   - Install AWS CLI tool
     An AWS account with proper permission with the services we are intend to initiate & use.

   - Install AWS CLI tool [Installing or updating the latest version of the AWS CLI - AWS Command Line Interface ](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

   - Install AWS SAM CLI tool [Installing the AWS SAM CLI - AWS Serverless Application Model ](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

   - Install Docker - that use to simulate the AWS environment for debugging

   - Install some extensions for VS Code:

     - AWS Toolkit [AWS Toolkit for Visual Studio Code - AWS Toolkit for VS Code ](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)

     - Serverless IDE

2. Run locally
   To run the lambda locally. Using SAM CLI below:

```
sam local invoke -d 3000 -e event.json HelloWorldFunction
```

3. Debug
   To debug the lambda function.

4. Build

5. Deploy

6. Destroy
