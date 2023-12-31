# Generated by Django 4.2.4 on 2023-08-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(max_length=100)),
                ('client_last_name', models.CharField(max_length=100)),
                ('client_profile_picture', models.ImageField(upload_to='media')),
                ('client_email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('client_security_question', models.CharField(max_length=100)),
                ('client_security_answer', models.CharField(max_length=100)),
            ],
        ),
    ]
