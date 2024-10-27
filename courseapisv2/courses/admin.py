from django.contrib import admin
from courses.models import Category, Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id','subject','active','created_date']
    search_fields = ['subject']
    list_filter = ['id','subject','created_date']
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)

# Register your models here.
