from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT
from edc_constants.constants import OTHER, NOT_APPLICABLE


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

ID_TYPE = (
    ('country_id', 'Country ID number'),
    ('drivers', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('hospital_no', 'Hospital number'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OTHER, 'Other'),
)


MARITAL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
)

LIVES_WITH = (
    ('alone', 'Alone'),
    ('partner or spouse', 'Partner or spouse?'),
    ('siblings', 'Siblings'),
    ('other', 'Other'),
    ('do not want to say', 'Do not want to say'),
)

YES_NO = (
    ('yes', 'Yes'),
    ('no', 'No')
)

TYPE_WORK = (
    ('occassional or Casual',
     'Occassional or Casual employment (piece job)'),
    ('seasonal employment', 'Seasonal employment'),
    ('formal wage employment (full-time)',
     'Formal wage employment (full-time)'),
    ('formal wage employment (part-time)',
     'Formal wage employment (part-time)'),
    ('self-employed in agriculture', 'Self-employed in agriculture'),
    ('self-employed making money, full time',
     'Self-employed making money, full time'),
    ('self-employed making money, part time',
     'Self-employed making money, part time'),
    ('don\'t want to answer', 'DNWA'),
    ('other', 'Other'),
)

WORK_DONE = (
    ('farmer (own land)', 'Farmer (own land)'),
    ('farm work on employers land', 'Farm work on employers land'),
    ('domestic worker', 'Domestic worker'),
    ('work in bar/ hotel/ guest house/ entertainment venue',
     'Work in bar/ hotel/ guest house/ entertainment venue'),
    ('fishing', 'Fishing'),
    ('mining', 'Mining'),
    ('Tourism/game parks', 'Tourism/game parks'),
    ('working in shop / small business', 'Working in shop / small business'),
    ('informal selling', 'Informal selling'),
    ('commercial sex work', 'Commercial sex work'),
    ('transport (trucker/ taxi driver)', 'Transport (trucker/ taxi driver)'),
    ('factory worker', 'Factory worker'),
    ('guard (security company)', 'Guard (security company)'),
    ('police/ Soldier', 'Police/ Soldier'),
    ('clerical and office work', 'Clerical and office work'),
    ('government worker', 'Government worker'),
    ('teacher', 'Teacher'),
    ('health care worker', 'Health care worker'),
    ('other professional', 'Other professional'),
    ('don\'t want to answer', 'Don\'t want to answer'),
    ('other', 'Other'),
)

SALARY = (
    ('none', 'No income'),
    ('1-199 pula', '1-199 pula'),
    ('200-499 pula', '200-499 pula'),
    ('500-999 pula', '500-999 pula'),
    ('1000-4999 pula', '1000-4999 pula'),
    ('5000-10,000 pula', '5000-10,000 pula'),
    ('more than 10,000 pula', 'More than 10,000 pula'),
    ('don\'t want to answer', 'Don\'t want to answer'),
)

HOW_ACTIVE = (
    ('very active', 'Very active'),
    ('somewhat active', 'Somewhat active'),
    ('not active', 'Not active'),
    ('don\'t want to answer', 'Don\'t want to answer'),
)

YES_NO_NA = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('N/A', 'NOT_APPLICABLE'),
)

YES_NO_DONTKNOW = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('don\'t know', 'Don\'t know'),
    ('don\'t want to answer', 'Don\'t want to answer'),
)

PROBLEMS = (
    ('HIV/AIDS', 'HIV/AIDS'),
    ('Schools', 'Schools'),
    ('Sewer', 'Sewer'),
    ('Unemployment', 'Unemployment'),
    ('Roads', 'Roads'),
    ('Water', 'Water'),
    ('House', 'House'),
    ('Malaria', 'Malaria'),
    )

INFO_SOURCE = (
    ('hospital_notes', 'Hospital notes'),
    ('outpatient_cards', 'Outpatient cards'),
    ('patient', 'Patient'),
    ('collateral_history',
     'Collateral History from relative/guardian'),
    (OTHER, 'Other'),
)

VISIT_UNSCHEDULED_REASON = (
    ('patient_unwell_outpatient', 'Patient unwell (outpatient)'),
    ('recurrence_symptoms', 'Recurrence of symptoms'),
    ('raised_icp_management', 'Raised ICP management'),
    ('art_initiation', 'ART initiation'),
    ('patient_hospitalised', 'Patient hospitalised'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not applicable'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled'),
    (UNSCHEDULED, 'Not scheduled'),
    (MISSED_VISIT, 'Missed'),
)
