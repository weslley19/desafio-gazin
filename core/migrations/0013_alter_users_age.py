# Generated by Django 3.2.4 on 2021-10-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_users_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(verbose_name='Idade'),
        ),
    ]
