
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    hours = models.PositiveIntegerField(default=72)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name="courses"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=20)

    birth_date = models.DateField(null=True, blank=True)

    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.group})"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
