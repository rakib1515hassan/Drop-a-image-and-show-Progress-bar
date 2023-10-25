from django.urls import path, include
from .views import test_view, upload_image

urlpatterns = [
    path('', test_view, name='test_view'),
    path('upload_image/', upload_image, name='upload_image'),

]
