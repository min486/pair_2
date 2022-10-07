from django.db import models

# Create your models here.

class Review(models.Model):
    movie_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title