from rest_framework import serializers
from .models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonProgressSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = LessonProgress
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAccessSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductAccess
        fields = '__all__'


class ProductStatsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    lessons_watched_count = serializers.IntegerField()
    total_time_watched = serializers.IntegerField()
    students_count = serializers.IntegerField()
    acquisition_percentage = serializers.FloatField()




























