from django.db import models
from tp_subject.choices import MARITAL_STATUS, LIVES_WITH, YES_NO, TYPE_WORK,  WORK_DONE, SALARY


class Education(models.Model):
    #print("models")
    working = models.CharField(
        max_length=10,
        choices=YES_NO,
        verbose_name="Are you currently working?")

    job_type = models.CharField(
        max_length=50,
        choices=TYPE_WORK,
        default='Other',
        verbose_name="In your main job, what type of work do you do?",)

    work_done = models.CharField(
        max_length=50,
        choices=WORK_DONE,
        default='Other',
        verbose_name="Describe the work that you do or did in your"
                     " most recent job. If you have more than one profession,"
                     " choose the one you spend the most time doing")

    salary = models.CharField(
        max_length=20,
        default='None',
        choices=SALARY,
        verbose_name="In the past month, how much money did you earn from work"
                     "you did or received in payment?"
        )

