# Generated by Django 2.1.5 on 2019-05-02 03:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OUForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('OU', 'Apply for Ordinary User')], max_length=100, verbose_name='Subject')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('username', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(default=0, verbose_name='Status')),
                ('author', models.CharField(max_length=100, unique=True, verbose_name='Author email')),
            ],
        ),
    ]
