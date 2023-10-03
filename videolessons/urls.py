from django.urls import path
from .views import *

urlpatterns = [
    path('api/lessons/', LessonProgressListView.as_view(), name='lesson_progress_list'),
    path('api/product/<int:id>/lessons/', ProductLessonsView.as_view(), name='product_list'),
    path('api/product-stats/', ProductStatsView.as_view(), name='product_stats'),
]

