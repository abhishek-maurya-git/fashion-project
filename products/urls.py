from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:product_id>', views.details, name='details'),
    path('women/', views.women, name='women'),
    path('w_details/<int:product_id>', views.w_details, name='w_details'),
    path('fav/<int:fav_id>', views.fav, name='fav'),
#     path('kids/', views.kids, name='kids'),
]
