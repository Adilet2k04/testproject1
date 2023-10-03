from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} Access"


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name


class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched_duration_seconds = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    last_watched_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.name} Progress"

    def save(self, *args, **kwargs):
        # Пересчитываем значение is_completed при сохранении объекта
        if self.watched_duration_seconds >= (self.lesson.duration_seconds * 80 / 100):
            self.is_completed = True
        else:
            self.is_completed = False
        self.last_watched_date = timezone.now()
        super().save(*args, **kwargs)

