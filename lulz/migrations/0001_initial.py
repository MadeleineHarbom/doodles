# Generated by Django 3.1.3 on 2020-11-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comic_id', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=20)),
            ],
        ),
    ]
