# Generated by Django 2.0.6 on 2018-12-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoryApp', '0007_auto_20181218_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterclassesmodel',
            name='movement',
            field=models.IntegerField(default=0, null=True),
        ),
    ]