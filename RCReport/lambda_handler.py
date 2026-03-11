def lambda_handler(event, context):

    print("RCReport Lambda executed")

    print("Event:", event)

    return {
        "statusCode": 200,
        "body": "RCReport Lambda is working"
    }