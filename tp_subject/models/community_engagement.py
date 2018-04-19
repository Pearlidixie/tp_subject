from django.db import models
from tp_subject.choices import YES_NO, HOW_ACTIVE, YES_NO_NA, YES_NO_DONTKNOW, PROBLEMS


class CommunityEngagement(models.Model):
    #print("models")
    how_active = models.CharField(
        max_length=10,
        choices=HOW_ACTIVE,
        verbose_name="How active are you in community activities such as burial"
                     " society, Motshelo, Syndicate, PTA, VDC(Village Developement"
                     " Committee), Mophato and development of the community that surrounds you??")

    voted = models.CharField(
        max_length=50,
        choices=YES_NO_NA,
        default='Other',
        verbose_name="Did you vote in the last local government election?",)

    #make a many to many
    major_problems = models.CharField(
        max_length=50,
        choices=PROBLEMS,
        default='Other',
        verbose_name="What are the major problems in this neighbourhood?")

    work_together = models.CharField(
        max_length=20,
        default='None',
        choices=YES_NO_DONTKNOW,
        verbose_name="If there is a problem in this neighborhood, do the"
                     " adults work together in solving it?"
        )

