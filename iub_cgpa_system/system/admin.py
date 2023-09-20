from django.contrib import admin

from .models import SEMESTER_INFO, Semester_Last_CGPA, Students_Subjects_Marks

# Register your models here.


@admin.register(SEMESTER_INFO)
class Semester_info_Admin(admin.ModelAdmin):
    list_display = ["user", "id", "semester", "name", "roll_no", "email", "phone"]


@admin.register(Semester_Last_CGPA)
class Semester_Last_CGPA_Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "last_semester_cgpa",
    ]


@admin.register(Students_Subjects_Marks)
class Student_Subjects_Marks_Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "subject_1",
        "subject_2",
        "subject_3",
        "subject_4",
        "subject_5",
        "subject_6",
        "subject_7",
        "subject_8",
        "subject_9",
        "credit_hour_1",
        "credit_hour_2",
        "credit_hour_3",
        "credit_hour_4",
        "credit_hour_5",
        "credit_hour_6",
        "credit_hour_7",
        "credit_hour_8",
        "credit_hour_9",
        "obtained_marks_1",
        "obtained_marks_2",
        "obtained_marks_3",
        "obtained_marks_4",
        "obtained_marks_5",
        "obtained_marks_6",
        "obtained_marks_7",
        "obtained_marks_8",
        "obtained_marks_9",
        "total_marks_1",
        "total_marks_2",
        "total_marks_3",
        "total_marks_4",
        "total_marks_5",
        "total_marks_6",
        "total_marks_7",
        "total_marks_8",
        "total_marks_9",
    ]
