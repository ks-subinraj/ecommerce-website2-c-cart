# Generated by Django 3.1.5 on 2021-01-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(),
        ),
    ]
