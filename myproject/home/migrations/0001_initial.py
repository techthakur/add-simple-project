# Generated by Django 3.2.4 on 2021-07-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('rollnumber', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=13)),
                ('desc', models.TextField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
