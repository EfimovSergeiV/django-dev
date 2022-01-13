from django.urls import path
from dev.views import *

urlpatterns = [
   path('tb/', TracebackRequest.as_view()),
]
