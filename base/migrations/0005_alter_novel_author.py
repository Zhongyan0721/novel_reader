# Generated by Django 4.1 on 2024-05-12 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_novel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author'),
        ),
    ]
