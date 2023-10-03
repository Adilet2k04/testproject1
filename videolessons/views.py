from django.db.models import Sum
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class LessonProgressListView(generics.ListAPIView):
    serializer_class = LessonProgressSerializer

    def get_queryset(self):
        user = self.request.user
        return LessonProgress.objects.filter(user=user)


class ProductLessonsView(generics.ListAPIView):
    serializer_class = LessonProgressSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['id']

        # Проверяем доступ пользователя к продукту
        access = get_object_or_404(ProductAccess, user=user, product__id=product_id, can_view=True)

        # Получаем список уроков, связанных с продуктом
        lessons = Lesson.objects.filter(products__id=product_id)

        # Фильтруем уроки, которые пользователь уже прогрессировал
        lesson_progress = LessonProgress.objects.filter(user=user, lesson__in=lessons)

        return lesson_progress


class ProductStatsView(APIView):

    def get(self, request):
        products = Product.objects.all()
        product_stats = []

        for product in products:
            lessons_watched_count = LessonProgress.objects.filter(lesson__products=product, is_completed=True).count()
            total_time_watched = LessonProgress.objects.filter(lesson__products=product, is_completed=True).aggregate(
                Sum('watched_duration_seconds'))['watched_duration_seconds__sum']
            students_count = ProductAccess.objects.filter(product=product, can_view=True).count()

            # Рассчитайте процент приобретения продукта
            total_users_count = User.objects.count()
            acquisition_percentage = (students_count / total_users_count) * 100

            statistics_data = {
                "product_id": product.id,
                "product_name": product.name,
                "lessons_watched_count": lessons_watched_count,
                "total_time_watched": total_time_watched,
                "students_count": students_count,
                "acquisition_percentage": acquisition_percentage
            }

            product_stats.append(statistics_data)

        serializer = ProductStatsSerializer(product_stats, many=True)
        return Response(serializer.data)
