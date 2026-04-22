def analyze_api_usage(data):
    """
    Analyze API usage patterns
    """

    total_hits = sum(item["hit_count"] for item in data)

    most_used = max(data, key=lambda x: x["hit_count"], default=None)
    least_used = min(data, key=lambda x: x["hit_count"], default=None)

    return {
        "total_hits": total_hits,
        "most_used_api": most_used,
        "least_used_api": least_used
    }