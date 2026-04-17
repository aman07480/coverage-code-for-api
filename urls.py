from django.urls import path
from .views import (
    api_coverage_list,
    unused_apis,
    top_used_apis
)

urlpatterns = [

    path("coverage/", api_coverage_list),
    path("coverage/unused/", unused_apis),
    path("coverage/top/", top_used_apis),

]