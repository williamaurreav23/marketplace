# Generated by Django 2.0.5 on 2018-10-16 09:41

from django.db import migrations, models
import marketplace.core.files


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_auto_20181016_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='image',
            field=models.FileField(max_length=250, upload_to=marketplace.core.files.UploadToDir('recommendations', random_name=True)),
        ),
    ]
