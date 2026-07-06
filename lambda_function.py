def lambda_handler(event, context):
    # Get the two numbers from the incoming event (input)
    num1 = event.get('num1')
    num2 = event.get('num2')
    
    # Basic validation - beginner-friendly error handling
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': 'Error: Please provide both num1 and num2'
        }
    
    # Calculate the sum
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': f'The sum of {num1} and {num2} is {result}'
    }