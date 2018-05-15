from django import forms
from django.utils.safestring import mark_safe
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from tp_subject.models.subject_consent import SubjectConsent


class SubjectConsentForm(SiteModelFormMixin, FormValidatorMixin,
                         forms.ModelForm):
    pass
