# Generated by Django 2.0.5 on 2018-10-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0006_user_citizenship")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="promotion",
            field=models.BooleanField(verbose_name=_("promotion"),default=True)
        )
    ]
