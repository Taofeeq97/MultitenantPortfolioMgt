# Generated by Django 4.2.4 on 2023-08-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_clientportfolio_client_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='clientportfolio',
            old_name='is_active',
            new_name='status',
        ),
        migrations.CreateModel(
            name='OrganizationalUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.organization')),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.organizationalunit')),
            ],
        ),
    ]