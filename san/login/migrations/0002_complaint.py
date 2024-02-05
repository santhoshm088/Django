# Generated by Django 4.2 on 2023-05-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rollno', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('complaint_type', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('describe', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
    ]
