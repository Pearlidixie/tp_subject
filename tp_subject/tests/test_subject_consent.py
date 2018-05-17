import re

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test.utils import override_settings
from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from tp_subject.models.subject_consent import SubjectConsent


class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'tp_screening.subjectscreening')

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('tp_subject.subjectconsent', **options)
        self.assertFalse(
            re.match(
                UUID_PATTERN,
                SubjectConsent.objects.all()[0].subject_identifier))
