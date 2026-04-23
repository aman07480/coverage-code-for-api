def detect_low_usage_apis(data, threshold=2):

    low_usage = []

    for api in data:
        if api["hit_count"] <= threshold:
            low_usage.append(api)

    return {
        "low_usage_apis": low_usage,
        "count": len(low_usage)
    }