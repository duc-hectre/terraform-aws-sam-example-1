### Introduction

This is the sample project to describe how to initiate & provision a serverless platform on AWS cloud using Terraform & SAM.
The approach is:

- Use Terraform:
  - To initiate & provision all the required infrastructures such as IAM role, policy, lambda, sqs, dynamodb, code pipeline,...
  - Use code pipeline to integrate with Terraform image in docker-hup for CI/CD action.
- Use SAM:
  - To develop, test & debug the source code of lambda function.
  - Build the lambda package used to deploy by Terraform.

### Sample architecture

### Get started.

Following the steps below to get the project start.

1. Install prerequisites

2. Run locally

3. Debug

4. Build

5. Deploy

6. Destroy
