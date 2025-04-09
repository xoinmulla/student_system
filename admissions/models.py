from django.db import models

class Student(models.Model):
    first_name     = models.CharField(max_length=100)
    last_name      = models.CharField(max_length=100)
    email          = models.EmailField(unique=True)
    date_of_birth  = models.DateField()
    course         = models.CharField(max_length=200)  # Consider later linking this to the Course model via a ForeignKey.
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField()
    credits     = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    # Many-to-Many relationship: one instructor can teach multiple courses and vice versa.
    courses    = models.ManyToManyField(Course, related_name="instructors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
