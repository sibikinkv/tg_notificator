def success_response(body):
    if not isinstance(body, str):
        body = str(body)

    return {
        'status': True,
        'message': body
    }


def failure_response(body):
    if not isinstance(body, str):
        body = str(body)

    return {
        'status': False,
        'message': body
    }
