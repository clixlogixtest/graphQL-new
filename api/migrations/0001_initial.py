# Generated by Django 3.2.2 on 2021-05-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('owner_info', models.CharField(max_length=150)),
                ('employee_size', models.IntegerField()),
            ],
        ),
    ]
