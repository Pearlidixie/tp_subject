from django.apps import AppConfig
from django.conf import settings
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig


class AppConfig(AppConfig):
    name = 'tp_subject'
    verbose_name = 'TP Subject'
    admin_site_name = 'tp_subject_admin'


if settings.APP_NAME == 'tp_subject':

    import os

    from datetime import datetime
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_constants.constants import FAILED_ELIGIBILITY
    from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_visit_tracking.constants import MISSED_VISIT
    from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from dateutil.tz import gettz
    from edc_appointment.appointment_config import AppointmentConfig

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP092'
        protocol_number = '092'
        protocol_name = 'Training'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'tp_subject': ('subject_visit', 'tp_subject.subjectvisit')}

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '092'

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'tp_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        # app_label = 'ambition_subject'
        default_appt_type = 'hospital'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='tp_subject.subjectvisit')
        ]

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
