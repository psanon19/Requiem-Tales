# Generated by Django 2.0.6 on 2018-12-10 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=257)),
                ('email', models.EmailField(max_length=200)),
                ('nameFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='StoryApp.PlayerCharacterModel')),
            ],
        ),
    ]
