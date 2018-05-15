from tp_subject.models.demographic import Demographic
#from tp_subject_form_validators.form_validators.demographic import Demo
from django import forms


class DemographicForm(forms.ModelForm):

    #form_validator_cls = DemographicFormValidator

    class Meta:
        model = Demographic
        fields = '__all__'