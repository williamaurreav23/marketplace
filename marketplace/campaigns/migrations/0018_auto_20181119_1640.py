# Generated by Django 2.0.5 on 2018-11-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0017_auto_20181114_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='color',
            field=models.CharField(max_length=6, null=True, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='rating',
            field=models.FloatField(default=4.0),
        ),
    ]