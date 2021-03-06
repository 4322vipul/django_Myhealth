# Generated by Django 2.1.2 on 2018-11-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protrade', '0002_auto_20181108_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_item_name', models.CharField(max_length=32)),
                ('exchange_item_price', models.CharField(max_length=8)),
                ('exchange_item_image', models.CharField(max_length=1000)),
                ('exchange_items_description', models.CharField(max_length=64)),
            ],
        ),
    ]
