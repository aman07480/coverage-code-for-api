from .utils import track_api_hit

class APICoverageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        # track only API routes
        if request.path.startswith("/api/"):
            track_api_hit(request.path, request.method)

        return response