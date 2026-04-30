from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import APICoverage


@api_view(["GET"])
def api_coverage_list(request):

    data = APICoverage.objects.all().values()

    return Response({
        "total_apis": len(data),
        "data": data
    })


@api_view(["GET"])
def unused_apis(request):

    data = APICoverage.objects.filter(hit_count=0).values()

    return Response({
        "unused_apis": list(data)
    })


@api_view(["GET"])
def top_used_apis(request):

    data = APICoverage.objects.order_by("-hit_count")[:5].values()

    return Response({
        "top_apis": list(data)
    })

    @api_view(["GET"])
def slow_apis(request):

    data = APICoverage.objects.order_by(
        "-average_response_time"
    ).values(
        "endpoint",
        "method",
        "average_response_time",
        "slowest_response_time",
        "hit_count"
    )[:10]

    return Response({
        "slowest_apis": list(data)
    })