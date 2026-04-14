from .models import APICoverage

def track_api_hit(path, method):

    obj, created = APICoverage.objects.get_or_create(
        endpoint=path,
        method=method
    )

    obj.hit_count += 1
    obj.save()