# Generated by Django 2.1.5 on 2019-04-23 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protrade', '0008_image_name_malaria_malaria_image_predicted_label'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='image_name_malaria',
            new_name='image_name_monia',
        ),
        migrations.RenameModel(
            old_name='malaria_image',
            new_name='monia_image',
        ),
        migrations.RenameField(
            model_name='image_name_monia',
            old_name='name_of_image_malaria',
            new_name='name_of_image_monia',
        ),
        migrations.RenameField(
            model_name='monia_image',
            old_name='image_given_malaria',
            new_name='image_given_monia',
        ),
    ]