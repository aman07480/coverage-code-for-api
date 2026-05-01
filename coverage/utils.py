from .models import APICoverage

def track_api_hit(path, method):

    obj, created = APICoverage.objects.get_or_create(
        endpoint=path,
        method=method
    )

    obj.hit_count += 1
    obj.save()


from .models import APICoverage
# from .response_time_tracker import calculate_average_response_time

def track_api_hit(path, method, response_time=0.0):

    obj, created = APICoverage.objects.get_or_create(
        endpoint=path,
        method=method
    )

    obj.average_response_time = calculate_average_response_time(
        obj.average_response_time,
        obj.hit_count,
        response_time
    )

    if response_time > obj.slowest_response_time:
        obj.slowest_response_time = response_time

    obj.hit_count += 1
    obj.save()