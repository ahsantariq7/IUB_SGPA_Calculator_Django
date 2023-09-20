from django.urls import path

from .views import (
    SEMESTER_PAGE,
    SUBJECT_PAGE,
    Final_result,
    Home,
    Semeseter_Data_Subjects,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("info/", SEMESTER_PAGE.as_view(), name="info"),
    path("subjects/", SUBJECT_PAGE.as_view(), name="subject"),
    path(
        "subjects/semester_data/",
        Semeseter_Data_Subjects.as_view(),
    ),
    path("subjects/semester_data/final_result/", Final_result.as_view()),
]
