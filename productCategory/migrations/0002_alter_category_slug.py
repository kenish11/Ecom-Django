# Generated by Django 4.0.3 on 2022-03-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productCategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
