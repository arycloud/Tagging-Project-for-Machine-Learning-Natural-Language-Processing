# Generated by Django 2.1.7 on 2019-03-10 08:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_postmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]