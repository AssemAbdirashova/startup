# Generated by Django 3.1.1 on 2020-09-15 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
