# Generated by Django 4.1.3 on 2022-12-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        ("practise", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="practice",
            name="related_posts",
            field=models.ManyToManyField(blank=True, to="blog.post"),
        ),
    ]
