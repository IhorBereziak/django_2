from django.urls import path
from .views import OfficeViev

urlpatterns = [
    path('', OfficeViev.as_view())
]
