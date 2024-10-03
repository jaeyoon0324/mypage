from django.db import models

# Create your models here.

class test_file(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.title}'