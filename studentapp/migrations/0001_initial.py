# Generated by Django 3.1.6 on 2023-06-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batchbooking',
            fields=[
                ('batchid', models.IntegerField()),
                ('admissionno', models.AutoField(primary_key=True, serialize=False)),
                ('admissiondate', models.DateField()),
                ('emailid', models.CharField(max_length=40)),
            ],
        ),
    ]
