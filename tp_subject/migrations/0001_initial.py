# Generated by Django 2.0.4 on 2018-04-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=10)),
                ('number_wives', models.IntegerField(verbose_name='If subject is a woman, how many wives does the husband have (traditional wives and subject included)')),
                ('number_wives_men', models.IntegerField(verbose_name='If subject is a man, how many wives does he have (traditional marriage included)?')),
                ('lives_with', models.CharField(choices=[('alone', 'Alone'), ('partner or spouse', 'Partner or spouse?'), ('siblings', 'Siblings'), ('other', 'Other'), ('do not want to say', 'Do not want to say')], max_length=10, verbose_name='Who do you currently live with?')),
            ],
        ),
    ]
