from tp_subject.models.demographic import Demographic
from django import forms


class DemographicForm(forms.ModelForm):
    class Meta:
        model = Demographic
        fields = '__all__'