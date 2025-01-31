from django.urls import path
from .views import CustomView

urlpatterns = [
    path("", CustomView.as_view(), name="Custom View")
]