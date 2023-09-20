from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import (
    Semester_Info_Form,
    Semester_Last_CGPA_Form,
    Student_SUbjects_Marks_Form,
)
from .models import SEMESTER_INFO, Semester_Last_CGPA, Students_Subjects_Marks


class Home(TemplateView):
    template_name = "home.html"


class SEMESTER_PAGE(LoginRequiredMixin, CreateView):
    form_class = Semester_Info_Form
    template_name = "semester_page.html"
    # success_url = "subjects/"
    queryset = SEMESTER_INFO.objects.all()

    def form_valid(self, form):
        semester_name = form.cleaned_data["semester"]
        self.request.session["semester"] = semester_name
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("subject")


class SUBJECT_PAGE(LoginRequiredMixin, CreateView):
    form_class = Semester_Last_CGPA_Form
    template_name = "subject_page.html"
    queryset = Semester_Last_CGPA.objects.all()
    success_url = "semester_data/"

    def form_valid(self, form):
        last_semester = form.cleaned_data["last_semester_cgpa"]
        self.request.session["last_semester_cgpa"] = last_semester

        print(last_semester)
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


def custom_round(number, decimal_places):
    factor = 10**decimal_places
    rounded_number = int(number * factor + 0.5) / factor
    return rounded_number


class Semeseter_Data_Subjects(LoginRequiredMixin, CreateView):
    form_class = Student_SUbjects_Marks_Form
    template_name = "student_semester_data.html"
    queryset = Students_Subjects_Marks.objects.all()
    success_url = "final_result/"

    def form_valid(self, form):
        import math

        obtained_marks = {}
        credit_hours = {}
        subjects = {}
        total_marks = {}

        for i in range(1, 10):
            obtained_marks[f"obtained_marks_{i}"] = form.cleaned_data.get(
                f"obtained_marks_{i}", 0
            )
            credit_hours[f"credit_hour_{i}"] = form.cleaned_data.get(
                f"credit_hour_{i}", 0
            )
            subjects[f"subject_{i}"] = form.cleaned_data.get(f"subject_{i}", "")
            total_marks[f"total_marks_{i}"] = form.cleaned_data.get(
                f"total_marks_{i}", 0
            )

        print(obtained_marks, credit_hours, subjects, total_marks)

        grading_scale = {
            100: {"grade_point": 4.0, "remark": "A+ Excellent"},
            99: {"grade_point": 4.0, "remark": "A+ Excellent"},
            98: {"grade_point": 4.0, "remark": "A+ Excellent"},
            97: {"grade_point": 4.0, "remark": "A+ Excellent"},
            96: {"grade_point": 4.0, "remark": "A+ Excellent"},
            95: {"grade_point": 4.0, "remark": "A+ Excellent"},
            94: {"grade_point": 4.0, "remark": "A Very Good"},
            93: {"grade_point": 4.0, "remark": "A Very Good"},
            92: {"grade_point": 4.0, "remark": "A Very Good"},
            91: {"grade_point": 4.0, "remark": "A Very Good"},
            90: {"grade_point": 4.0, "remark": "A Very Good"},
            89: {"grade_point": 4.0, "remark": "A Very Good"},
            88: {"grade_point": 4.0, "remark": "A Very Good"},
            87: {"grade_point": 4.0, "remark": "A Very Good"},
            86: {"grade_point": 4.0, "remark": "A Very Good"},
            85: {"grade_point": 4.0, "remark": "A Very Good"},
            84: {"grade_point": 3.9, "remark": "B+ Good"},
            83: {"grade_point": 3.9, "remark": "B+ Good"},
            82: {"grade_point": 3.8, "remark": "B+ Good"},
            81: {"grade_point": 3.7, "remark": "B+ Good"},
            80: {"grade_point": 3.7, "remark": "B+ Good"},
            79: {"grade_point": 3.6, "remark": "B Good"},
            78: {"grade_point": 3.5, "remark": "B Good"},
            77: {"grade_point": 3.5, "remark": "B Good"},
            76: {"grade_point": 3.4, "remark": "B Good"},
            75: {"grade_point": 3.3, "remark": "B Good"},
            74: {"grade_point": 3.3, "remark": "B Good"},
            73: {"grade_point": 3.2, "remark": "B Good"},
            72: {"grade_point": 3.1, "remark": "B Good"},
            71: {"grade_point": 3.1, "remark": "B Good"},
            70: {"grade_point": 3.0, "remark": "B Good"},
            69: {"grade_point": 2.9, "remark": "C Satisfactory"},
            68: {"grade_point": 2.8, "remark": "C Satisfactory"},
            67: {"grade_point": 2.7, "remark": "C Satisfactory"},
            66: {"grade_point": 2.6, "remark": "C Satisfactory"},
            65: {"grade_point": 2.5, "remark": "C Satisfactory"},
            64: {"grade_point": 2.4, "remark": "C Satisfactory"},
            63: {"grade_point": 2.3, "remark": "C Satisfactory"},
            62: {"grade_point": 2.2, "remark": "C Satisfactory"},
            61: {"grade_point": 2.1, "remark": "C Satisfactory"},
            60: {"grade_point": 2.0, "remark": "C Satisfactory"},
            59: {"grade_point": 1.9, "remark": "D Poor"},
            58: {"grade_point": 1.8, "remark": "D Poor"},
            57: {"grade_point": 1.7, "remark": "D Poor"},
            56: {"grade_point": 1.6, "remark": "D Poor"},
            55: {"grade_point": 1.5, "remark": "D Poor"},
            54: {"grade_point": 1.4, "remark": "D Poor"},
            53: {"grade_point": 1.3, "remark": "D Poor"},
            52: {"grade_point": 1.2, "remark": "D Poor"},
            51: {"grade_point": 1.1, "remark": "D Poor"},
            50: {"grade_point": 1.0, "remark": "D Poor"},
            49: {"grade_point": 0.0, "remark": "F Fail"},
        }

        for semester in range(1, 10):
            print(f"Subject: {semester}")
            semester_grade_points = 0
            semester_credit_hours = 0

        for i in range(1, 10):
            credit_hour = credit_hours[f"credit_hour_{i}"]
            marks = obtained_marks[f"obtained_marks_{i}"]
            subject = subjects[f"subject_{i}"]
            total = total_marks[f"total_marks_{i}"]

            if credit_hour is None:
                credit_hour = 0
            if marks is None:
                marks = 0
            if total is None:
                total = 0

            if total != 0:  # Check if total is not zero to avoid ZeroDivisionError
                percentage = (marks / total) * 100
                rounded_percentage = math.ceil(percentage)

                if rounded_percentage in grading_scale:
                    grade_point = grading_scale[rounded_percentage]["grade_point"]
                    remark = grading_scale[rounded_percentage]["remark"]
                elif rounded_percentage < 49:
                    grade_point = 0.0
                    remark = "F Fail"
                else:
                    grade_point = 0.0
                    remark = ""

                quality_point = grade_point * credit_hour

                semester_grade_points += quality_point
                semester_credit_hours += credit_hour

                print(
                    f"Subject: {subject}, Credit Hours: {credit_hour}, Marks: {marks}, Percentage: {percentage}%, Rounded Percentage: {rounded_percentage}, Grade Point: {grade_point}, Remark: {remark}, Quality Point: {quality_point}"
                )
                """
            else:
                print(
                    f"Subject: {subject}, Credit Hours: {credit_hour}, Marks: {marks}, Percentage: N/A (Total is zero)"
                )
                """

        if semester_credit_hours != 0:
            semester_gpa = semester_grade_points / semester_credit_hours
            semester_gpa = custom_round(semester_gpa, 2)
            print(f"SGPA for Semester : {semester_gpa}\n")
            self.request.session["semester_gpa"] = semester_gpa
        else:
            semester_gpa = 0.0
            print("SGPA for Semester : N/A (Zero Credit Hours)\n")
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = [i + 1 for i in range(0, 9)]
        return context


class Final_result(LoginRequiredMixin, TemplateView):
    template_name = "final_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last = self.request.session.get("last_semester_cgpa")
        print(last)
        semester_gpa = self.request.session.get("semester_gpa")
        print(semester_gpa)
        context["last"] = last
        context["semester_gpa"] = semester_gpa
        context["final"] = custom_round((last + semester_gpa) / 2, 2)

        return context
