# Generated by Django 4.0.4 on 2023-05-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_page_hits', '0002_auto_20201012_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagehit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
