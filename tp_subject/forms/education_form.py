from tp_subject.models.education import Education
from django import forms


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'