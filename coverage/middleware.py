import time
from .utils import track_api_hit

class APICoverageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        execution_time = round(time.time() - start_time, 4)

        if request.path.startswith("/api/"):
            track_api_hit(
                request.path,
                request.method,
                execution_time
            )

        return response