# Generated by Django 2.0.5 on 2018-06-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0007_auto_20180615_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='date_of_birth',
            field=models.DateField(verbose_name='date of birth'),
        ),
    ]