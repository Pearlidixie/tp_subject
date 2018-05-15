from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from .constants import MARRIED
from faker import Faker
from model_mommy.recipe import Recipe

from .models import Demographic
from tp_subject.constants import NOT_APPLICABLE

fake = Faker()

demographic = Recipe(
    Demographic,
    marital_status=MARRIED,
    number_wives=1,
    number_husbands=NOT_APPLICABLE,
    lives_with=40)
