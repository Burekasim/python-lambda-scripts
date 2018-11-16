from datetime import datetime
from urllib.request import ssl, socket


def lambda_handler(event, context):
    # TCP connection should be fast, so let's set a timeout of 10 seconds
    tcp_connection_timeout = 10
    # Handle query strings to avoid "Internal server error" from API Gateway
    if event['queryStringParameters']:
        if 'url' in event['queryStringParameters']:
            base_url = event["queryStringParameters"]['url']
    else:
        response = {
            "statusCode": 200,
            "isBase64Encoded": False,
            "body": "Usage: ?url=domain.com&port=443"
        }
        return response
    # use port 443 if client didn't send port query string
    if 'port' in event['queryStringParameters']:
        port = int(event["queryStringParameters"]['port'])
    else:
        port = 443

    context = ssl.create_default_context()
    try:
        with socket.create_connection((base_url, port), timeout=tcp_connection_timeout) as sock:
            with context.wrap_socket(sock, server_hostname=base_url) as ssock:
                data = ssock.getpeercert()
    except Exception as e:
        response = {
            "statusCode": 200,
            "isBase64Encoded": False,
            "body": f'Error: {e}'
        }
        return response

    # format ssl end date date output to mm/dd/YYYY
    ssl_end_date_format = datetime.strptime(data['notAfter'], '%b %d %X %Y %Z').strftime('%m/%d/%Y')
    response = {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": ssl_end_date_format
    }
    return response
