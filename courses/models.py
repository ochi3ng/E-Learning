from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username}'s Profile"
