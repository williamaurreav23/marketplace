# Generated by Django 2.0.5 on 2018-09-03 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0004_auto_20180830_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='supporter',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='token',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]