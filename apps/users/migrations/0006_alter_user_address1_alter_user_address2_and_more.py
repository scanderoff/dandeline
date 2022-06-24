# Generated by Django 4.0.5 on 2022-06-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, default='1999-12-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]
