def update_error_stats(obj, status_code):

    # 4xx client errors
    if 400 <= status_code < 500:
        obj.client_error_count += 1

    # 5xx server errors
    elif 500 <= status_code < 600:
        obj.server_error_count += 1

    return obj