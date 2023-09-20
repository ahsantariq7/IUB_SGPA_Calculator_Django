from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SEMESTER_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
)

CREDIT_HOURS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
)


SUBJECTS = (
    ("THEORY", "THEORY"),
    ("THOERY_LAB", "THEORY_LAB"),
    ("WORKSHOP", "WORKSHOP"),
    ("PRACTICAL", "PRACTICAL"),
    ("LAB", "LAB"),
)

TOTAL_MARKS = (
    (25, 25),
    (50, 50),
    (100, 100),
    (150, 150),
    (200, 200),
    (250, 250),
    (300, 300),
)


class SEMESTER_INFO(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, default="full name")
    roll_no = models.CharField(max_length=100, default="...@iub.edu.pk")
    email = models.EmailField(default="xyz@gmail.com")
    phone = models.IntegerField(default=0)
    semester = models.IntegerField(default=1, choices=SEMESTER_CHOICES)

    class Meta:
        verbose_name = "Semester_Info"
        verbose_name_plural = "Semester_Info's"


class Semester_Last_CGPA(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    last_semester_cgpa = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = "Semester_Subjects_Info"
        verbose_name_plural = "Semester_Subjects_Info's"


class Students_Subjects_Marks(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    subject_1 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_2 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_3 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_4 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_5 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_6 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_7 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_8 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    subject_9 = models.CharField(max_length=50, blank=True, null=True, choices=SUBJECTS)
    credit_hour_1 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_2 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_3 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_4 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_5 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_6 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_7 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_8 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    credit_hour_9 = models.IntegerField(
        blank=True, null=True, default=0, choices=CREDIT_HOURS
    )
    obtained_marks_1 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_2 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_3 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_4 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_5 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_6 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_7 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_8 = models.IntegerField(blank=True, null=True, default=0)
    obtained_marks_9 = models.IntegerField(blank=True, null=True, default=0)
    total_marks_1 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_2 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_3 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_4 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_5 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_6 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_7 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_8 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
    total_marks_9 = models.IntegerField(
        blank=True, null=True, default=0, choices=TOTAL_MARKS
    )
