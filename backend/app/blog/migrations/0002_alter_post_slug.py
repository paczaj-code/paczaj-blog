# Generated by Django 4.1.3 on 2022-12-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
