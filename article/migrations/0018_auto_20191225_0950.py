# Generated by Django 2.1.7 on 2019-12-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20171019_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
