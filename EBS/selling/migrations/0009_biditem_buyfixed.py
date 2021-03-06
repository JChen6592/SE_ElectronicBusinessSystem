# Generated by Django 2.1.5 on 2019-05-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0008_auto_20190511_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_bid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BuyFixed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('credit_card_number', models.CharField(default='', max_length=100)),
                ('credit_card_expiration_date', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
