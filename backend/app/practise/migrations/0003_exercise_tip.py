# Generated by Django 4.1.3 on 2023-02-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0002_alter_practice_related_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='tip',
            field=models.TextField(blank=True),
        ),
    ]