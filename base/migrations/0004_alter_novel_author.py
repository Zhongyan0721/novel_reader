# Generated by Django 4.1 on 2024-05-12 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_novel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]