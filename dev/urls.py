from django.urls import path, re_path
from dev.views import *


urlpatterns = [
   re_path('tb/', TracebackRequest.as_view()),
]
