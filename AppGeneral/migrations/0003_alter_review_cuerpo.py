# Generated by Django 4.1.4 on 2023-01-29 22:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGeneral', '0002_rename_post_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cuerpo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
