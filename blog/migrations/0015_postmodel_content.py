# Generated by Django 2.1.7 on 2019-03-10 07:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_postmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
