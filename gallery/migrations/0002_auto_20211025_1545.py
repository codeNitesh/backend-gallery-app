# Generated by Django 3.2.8 on 2021-10-25 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='ImgDetails',
            new_name='imgDetails',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='ImgId',
            new_name='imgId',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='ImgName',
            new_name='imgName',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='ImgURL',
            new_name='imgURL',
        ),
    ]
