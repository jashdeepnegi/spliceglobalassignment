# Generated by Django 3.1.2 on 2020-11-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=250)),
                ('mobile_number', models.IntegerField()),
                ('telephone_number', models.IntegerField()),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('postal_zip', models.IntegerField()),
                ('country', models.IntegerField(choices=[(1, 'America'), (2, 'Germany'), (3, 'Australia'), (4, 'France')])),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
