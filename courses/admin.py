from django.contrib import admin
from .models import Course, Enrollment, Lesson, Profile

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Profile)
