# Generated by Django 2.0.6 on 2018-12-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoryApp', '0005_auto_20181210_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterclassesmodel',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
