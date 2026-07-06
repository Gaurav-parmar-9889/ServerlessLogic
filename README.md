#  The Serverless Logic

## Scenario
Build a "Cost Calculator" API without running a server 24/7. 
The solution should only execute code when triggered, keeping cost at 
zero when idle.

## Solution
- Created an AWS Lambda function (`costCalculatorFunction`) using Python 3.12.
- The function takes two numbers (`num1`, `num2`) as input and returns their sum.
- Includes basic input validation for missing values.
- Tested using multiple test events (positive numbers, negative numbers, 
  decimals, missing input) to verify accuracy.
- (Optional) Exposed the function as an HTTP API using API Gateway.

## Tools Used
AWS Lambda, API Gateway (optional)

## Files
- `lambda_function.py` - Lambda function source code
- `screenshots/` - Proof of function creation, deployment, and test results

## Outcome
Function executes in milliseconds and incurs zero cost when idle, 
fully satisfying the serverless requirement.
