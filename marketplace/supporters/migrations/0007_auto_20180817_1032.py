# Generated by Django 2.0.5 on 2018-08-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporters', '0006_auto_20180605_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='following',
            field=models.ManyToManyField(blank=True, limit_choices_to={'state': 'APPROVED'}, related_name='supporters', to='athletes.Athlete', verbose_name='following'),
        ),
    ]