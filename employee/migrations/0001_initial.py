# Generated by Django 2.2.5 on 2019-09-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_firstname', models.CharField(max_length=25)),
                ('emp_lastname', models.CharField(max_length=25)),
                ('emp_username', models.CharField(max_length=50)),
                ('emp_phone_number', models.IntegerField()),
            ],
        ),
    ]
