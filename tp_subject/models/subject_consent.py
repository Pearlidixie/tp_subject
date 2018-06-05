from edc_consent.model_mixins import ConsentModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_identifier.model_mixins import UniqueSubjectIdentifierModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_consent.field_mixins.vulnerability_fields_mixin import VulnerabilityFieldsMixin
from edc_consent.field_mixins.sample_collection_fields_mixin import SampleCollectionFieldsMixin
from edc_consent.field_mixins.review_fields_mixin import ReviewFieldsMixin
from edc_consent.field_mixins.identity_fields_mixin import IdentityFieldsMixin
from django.db import models
from ..constants import NOT_APPLICABLE, NO
from ..choices import YES_NO
from django.apps import apps as django_apps
from edc_search.model_mixins import SearchSlugManager
from edc_consent.managers import ConsentManager
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(ConsentModelMixin, SiteModelMixin, 
                     UpdatesOrCreatesRegistrationModelMixin, PersonalFieldsMixin,
                     UniqueSubjectIdentifierModelMixin,
                     SampleCollectionFieldsMixin, VulnerabilityFieldsMixin,
                     ReviewFieldsMixin, IdentityFieldsMixin, BaseUuidModel):

    """ A model completed by the user that captures the ICF.
    """

    subject_screening_model = 'tp_screening.subjectscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        default=None,
        max_length=50)

    completed_by_next_of_kin = models.CharField(
        max_length=10,
        default=NO,
        choices=YES_NO,
        editable=False)

    objects = SubjectConsentManager()
    consent = ConsentManager()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        subject_screening = self.get_subject_screening()
        self.gender = subject_screening.gender
        self.subject_type = 'subject'
        self.citizen = NOT_APPLICABLE
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_subject_screening(self):
        """Returns the subject screening model instance.

        Instance must exist since SubjectScreening is completed
        before consent.
        """
        model_cls = django_apps.get_model(self.subject_screening_model)
        return model_cls.objects.get(
            screening_identifier=self.screening_identifier)

    @property
    def registration_unique_field(self):
        """Required for UpdatesOrCreatesRegistrationModelMixin.
        """
        return 'subject_identifier'

    class Meta(ConsentModelMixin.Meta):
        unique_together = (
            ('subject_identifier', 'version'),
            ('subject_identifier', 'screening_identifier'),
            ('first_name', 'dob', 'initials', 'version'))