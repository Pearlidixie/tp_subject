# Generated by Django 2.0.4 on 2018-04-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_subject', '0003_auto_20180419_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='working',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=10, verbose_name='Are you currently working?'),
        ),
    ]
