from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/details', views.details, name='details'),
]
