# Generated by Django 2.1.5 on 2019-05-11 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0007_auto_20190511_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='product_image',
            field=models.ImageField(default='default.jpg', upload_to='item_pics/'),
        ),
    ]