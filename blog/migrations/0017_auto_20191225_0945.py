# Generated by Django 2.1.7 on 2019-12-25 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190310_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.CommentModel'),
        ),
    ]
