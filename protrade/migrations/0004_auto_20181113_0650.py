# Generated by Django 2.1.2 on 2018-11-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protrade', '0003_exchangeitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeitems',
            name='exchange_item_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
