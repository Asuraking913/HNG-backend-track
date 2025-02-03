from django.urls import path
from .views import CustomView, HandleNumberView

urlpatterns = [
    path("", CustomView.as_view(), name="Custom View"), 
    path("api/classify-number", HandleNumberView.as_view(), name='number view')
]