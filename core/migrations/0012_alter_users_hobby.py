# Generated by Django 3.2.4 on 2021-10-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_users_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='hobby',
            field=models.TextField(max_length=255, verbose_name='Hobby'),
        ),
    ]
