from django import forms

from .models import SEMESTER_INFO, Semester_Last_CGPA, Students_Subjects_Marks


class Semester_Info_Form(forms.ModelForm):
    class Meta:
        model = SEMESTER_INFO
        fields = "__all__"
        exclude = ["user"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields[
                "user"
            ].widget = forms.HiddenInput()  # Hide the user field in the form
            self.fields["user"].initial = self.instance.user

        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.user = self.instance.user
            if commit:
                instance.save()
            return instance


class Semester_Last_CGPA_Form(forms.ModelForm):
    class Meta:
        model = Semester_Last_CGPA
        fields = "__all__"

        exclude = ["user"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields[
                "user"
            ].widget = forms.HiddenInput()  # Hide the user field in the form
            self.fields["user"].initial = self.instance.user

        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.user = self.instance.user
            if commit:
                instance.save()
            return instance


class Student_SUbjects_Marks_Form(forms.ModelForm):
    class Meta:
        model = Students_Subjects_Marks
        fields = "__all__"

        exclude = ["user"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields[
                "user"
            ].widget = forms.HiddenInput()  # Hide the user field in the form
            self.fields["user"].initial = self.instance.user

        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.user = self.instance.user
            if commit:
                instance.save()
            return instance
