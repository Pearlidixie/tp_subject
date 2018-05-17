import arrow
from datetime import datetime

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

subjectconsent_v1 = Consent(
    'tp_subject.subjectconsent',
    version='1',
    start=arrow.get(datetime(2017, 5, 17)).datetime,
    end=arrow.get(datetime(2018, 6, 17)).datetime,
    age_min=16,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE])

site_consents.register(subjectconsent_v1)