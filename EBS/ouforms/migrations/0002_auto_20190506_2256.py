# Generated by Django 2.1.5 on 2019-05-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouforms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouform',
            name='username',
        ),
        migrations.AlterField(
            model_name='ouform',
            name='author',
            field=models.CharField(max_length=100, unique=True, verbose_name='Author username'),
        ),
    ]