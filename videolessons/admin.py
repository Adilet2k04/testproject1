from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductAccessAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class LessonProgressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAccess, ProductAccessAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonProgress, LessonProgressAdmin)

