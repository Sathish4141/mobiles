# Generated by Django 4.0.5 on 2023-09-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]