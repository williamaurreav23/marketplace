# Generated by Django 2.0.5 on 2018-11-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0019_auto_20181119_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='rating',
            field=models.FloatField(default=5.0),
        ),
        migrations.AlterField(
            model_name='sport',
            name='color',
            field=models.CharField(max_length=6, verbose_name='color'),
        ),
    ]
