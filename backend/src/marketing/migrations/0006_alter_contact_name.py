# Generated by Django 4.0.5 on 2022-06-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
