from django.db import models

# Create your models here.
class TeachersClass(models.Model):
    class_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.class_name} taught by {self.teacher_name}"